import datetime
from requests import Session, ConnectionError
from datetime import date, timedelta, datetime
import calendar
import csv

EXCEPTION_LOG_FILE = "exceptions.txt"

class Register:
    user = ""
    psw = ""
    session = None

    WRONG_PSW = -3
    CONNECTION_ERROR = -2
    ERROR = -1

    site = "https://itsar.registrodiclasse.it"

    def __init__(self, user="", psw=""):
        self.set_credential(user, psw)

    def set_credential(self, user, psw):
        self.user = user
        self.psw = psw
        self.session = Session()

    def requestGeop(self, start_date="", end_date=""): #richiesta a GEOP
        start_date, end_date = self.correct_dates(start_date, end_date)
        lessons_url = f"/geopcfp2/json/fullcalendar_events_alunno.asp?Oggetto=idAlunno&idOggetto=2578&editable=false&z=1665853136739&start={start_date}&end={end_date}&_=1665853136261"

        try:
            if not self.can_login(self.user, self.psw):
                return self.WRONG_PSW

            MAX_ATTEMPTS = 3
            oldDB = ""
            url = self.site + lessons_url
            for attempt in range(MAX_ATTEMPTS):
                try:
                    res = self.session.get(url)
                except ConnectionError as e:
                    print("ConnectionError", e)
                    if(attempt == MAX_ATTEMPTS-1):
                        return self.CONNECTION_ERROR
                except Exception as e:
                    print("Exception", e)
                    if(attempt == MAX_ATTEMPTS-1):
                        return self.ERROR
                    continue

            oldDB = self.extract_info(res.json())
            print("Risposta del server:", oldDB)
            print("Status Code:", res.status_code)
            print("Response Text:", res.text)
            return oldDB

        except ConnectionError as e:
            print("Failed to connect. Check your internet connection")

            with open(EXCEPTION_LOG_FILE, "a") as log:
                log.write( f"# ---- {str(datetime.today())[:-7]} ---- #\n" )
                log.write("Failed to connect. Cannot fetch register.")

            return self.CONNECTION_ERROR
        
        except Exception as e:
            print("Something went wrong")

            with open(EXCEPTION_LOG_FILE, "a") as log:
                log.write( f"# ---- {str(datetime.today())[:-7]} ---- #\n" )
                log.write(str(e))

            return self.ERROR

    def correct_dates(self, start_date, end_date):
        if start_date == "":
            start_date = date.today()

        if end_date == "":
            end_date = start_date + timedelta(days=5*30) #5 mesi da oggi

        return start_date, end_date

    def extract_info(self, info):
        WEEKDAY = [
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ]

        lessons = []

        for _lesson in info:
            lesson = {}
            lesson["subject"] = _lesson["title"].split(" - ")[1].strip().replace("Ã", "à")
            lesson["start_date"] = _lesson["start"].split("T")[0]
            lesson["start_time"] = _lesson["start"].split("T")[1][:-3].strip()
            lesson["end_date"] = _lesson["end"].split("T")[0]
            lesson["end_time"] = _lesson["end"].split("T")[1][:-3].strip()
            lesson["location"] = _lesson.get("room", "Aula non disponibile")
            teacher = _lesson["tooltip"].split("Docente:")[1].split("<br>")[0].strip()
            room = _lesson["tooltip"].split("Aula:")[1].split("<br>")[0].strip()
            lesson["description"] = f"Docente: {teacher}, Aula: {room}"
            lessons.append(lesson)

        return lessons

    def can_login(self, username, psw): #verifica login
        login_url = "/geopcfp2/update/login.asp?1=1&ajax_target=DIVHidden&ajax_tipotarget=login"
        body = {'username': username, 'password': psw}

        url = self.site + login_url
        res = self.session.post(url, data=body)

        if res.status_code == 200:
            if "Username e password non validi" in res.text:
                return False
            return True
        else:
            print(str(res.status) + " " + res.reason)
        
        return False

    def export_to_csv(self, csv_file):
        events = self.requestGeop()
        if events == self.WRONG_PSW or events == self.CONNECTION_ERROR or events == self.ERROR:
            print("Errore durante la richiesta degli eventi dal registro.")
            return

        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Location', 'Description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for event in events:
                writer.writerow({
                    'Subject': event['subject'],
                    'Start Date': event['start_date'],
                    'Start Time': event['start_time'],
                    'End Date': event['end_date'],
                    'End Time': event['end_time'],
                    'Location': event['location'],
                    'Description': event['description']
                })

if __name__ == "__main__":
    #Credenziali
    user = "Propria mail" #da inserire
    psw = "Propria password" #da inserire
    register = Register(user, psw)

    # Estrarre gli eventi dal registro e salvarli nel file CSV
    csv_file_path = r"percorso\Calendario.csv" #da inserire
    register.export_to_csv(csv_file_path)





























































































