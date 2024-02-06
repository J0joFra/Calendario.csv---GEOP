# Calendario.csv---GEOP
Ho modificato il codice di **https://github.com/Dadezana** per poter importare le lezioni dal registro elettronico GEOP in un calendario di formato csv. In questo modo questo Calendario.csv può essere importato in applicazioni terze, come Google Calendar e visualizzare i propri impegni comodamente.
Sotto ho scritto la procedura per impostare il codice e per poi importarlo su Google Calendar

-----------------------------------------------------------------------------------------------------------------------------
1 **LIBRERIE DA INSTALLARE ED IMPORTARE**

'**requests**' potrebbe richiedere un'installazione tramite pip (pip install requests), ma è possibile che requests sia già installato nell'ambiente Python. 
'**datetime**' è una libreria standard di Python, fornisce classi per la gestione delle date e delle ore.
'**timedelta**' è una parte di datetime e non richiede un'installazione separata, viene utilizzata per rappresentare la differenza tra due date o orari.
'**calendar**' è una libreria standard di Python e non richiede l'installazione, fornisce funzionalità per lavorare con calendari.
'**csv**' è una libreria standard di Python e non richiede l'installazione separata, viene utilizzata per la lettura e la scrittura di file CSV (Comma-Separated Values), che sono comunemente utilizzati per archiviare dati tabulari.

-----------------------------------------------------------------------------------------------------------------------------
2 **FILE DA CREARE** (Calendario.csv)

Per poter salvare le informazioni ottenute dal registro elettronico, devi avere un file di formato .csv che verrà importato dentro Google Calendar.
Per far ciò devi prima controllare le impostazioni del proprio dispositivo in particolare bisogna attivare per modificare l'estensione dei file:

	SISTEMA > Per sviluppatori > Mostra estensione file
	Nuovo documento di testo -> Calendario.txt
	Selezionare .txt e rinominare .csv
	Confermare di modificare l'estensione

-----------------------------------------------------------------------------------------------------------------------------
3 **MODIFICHE NECESSARIE**

Il codice richiede alcune modifiche molto semplice all'interno del codice, poichè esso è settato in base alle mie credenziali e alla mia cartella dove ho salvato i file.
a] Vai in fondo al codice nella condizione '**if __name__ == "__main__":**'
b] Sostituire user e psw con le proprie credenziali
c] Cerca il file Calendario.csv creato precedentemente, selezionalo e clicca 'COPIA COME PERCORSO'
d] Torna nel codice e scendi di qualche riga a 'csv_file_path = r"percorso\Calendario.csv"
e] Sostituire "percorso\Calendario.csv" con il percorso copiato nel punto precedente*

*Controllare che il percorso sia stato copiato correttamente

-----------------------------------------------------------------------------------------------------------------------------
4 **ESECUZIONE E IMPORTAZIONE FILE SU GOOGLE CALENDAR**

Se avete seguito tutti i punti precedenti, dovreste avere tutto pronto per creare il file-calendario.

a] ESEGUI IL CODICE, se tutto andato bene dovrebbe restituirti in terminale la RISPOSTA DEL SERVER, lo STATUS CODE e la RESPONSE TEXT 

b] APRI GOOGLE CALENDAR > Menù principale > Altri calendari > "+" (aggiungi altri calendari) > Importa
   Seleziona il file dal computer > (selezionare Calendario.csv) > Importa

se tutto è andato bene dovrebbe comparirti un avviso con quanti eventi ha trovato (ed aumaticamente inserito) all'interno del file. Torna sulla pagina principale e di Google Calendar e dovresti poter vedere il calendario inserito.






