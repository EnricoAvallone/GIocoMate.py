
# Gioco: _Through the Hallway_
#### [___Avallone Enrico___](https://github.com/EnricoAvallone); [___Ippolito Gabriele___](https://github.com/gabrielecoding); [___Lastrucci Davide___](https://github.com/davidelastrucci)


***
## Indice
1. [Scopo del gioco](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#scopo-del-gioco)
2. [Trama](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#trama)
3. [Svolgimento del gioco](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#svolgimento-del-gioco)
4. [Comandi di gioco](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#comandi-di-gioco)
5. [Power-up](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#power-up)
6. [Funzionamento blocchi](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#funzionamento-blocchi)
7. [Salvataggio dati](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#salvataggio-dati)
8. [Utilizzo coniche](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#utilizzo-coniche)

</br>
</br>


***
## Scopo del gioco 
    Eliminare i nemici e resistere più tempo possibile
</br>

***
## Trama
    Ad "X", agente dei servizi segreti, è stata assegnata una missione di spionaggio nella casa bianca, poiché l'FBI sospetta che il presidente voglia usare delle armi nucleari per minacciare la Cina.
    Mentre "X" sta origliando le trattative del presidente con delle persone poco affidabili, viene scoperto, e si ritrova a dover scappare per i corridoi della casa bianca ed affrontare i sistemi di sicurezza della casa bianca, inseguito dalle guardie.
</br>

***
## Svolgimento del gioco 
    Il personaggio corre in un corridoio infinito e dovrà affrontare varie difese presenti nella casa bianca, se verrà colpito da una difesa morirà e la partità verrà terminata.
    
    Durante la corsa potrà raccogliere dei power-up che gli forniranno abilità particolari.
    Il punteggio finale sarà dato dal tempo durante cui si è riusciti a sopravvivere.
</br>

***
## Comandi di gioco
</br>

+ __Space-bar__ → salta
+ __Space-bar__ + __Space-bar__ → doppio salto
+ __J__ → jetpack (massimo 4 secondi poi si deve ricaricare)
+ __F__ → fire(spara)
+ __R__ → restart
+ __escape__ → esc(chiusura del gioco)
</br>
</br>

***
## Power-up
* #### __Palla di neve:__ 
  il colpo successivo all’attivazione lancerà una palla di neve che rimbalzando sul terreno travolgerà tutti i nemici

* #### __Scudo:__ 
  per 10 secondi dall’attivazione si avrà uno scudo che proteggerà dai nemici

* #### __Amico drone:__ 
  arriva un drone che ti aiuta nell’eliminazione dei nemici per 10 secondi
</br>
</br>

***

## Funzionamento blocchi

### Start
    La prima funzione, che è poi quella che avvia tutto, è "start". Start carica sullo schermo l'immagine di sfondo iniziale e l'immagine del pulsante di avvio del gioco.
    Se l'immagine del pulsante di avvio viene premuta con il tasto sinistro, grazie a start, si avvierà il gioco, verranno infatti eseguite le funzioni "inizializza", "disegna_oggetti" ed "aggiorna".
    Inoltre la variabile "ricominciamo" passerà da "False" a "True", facendo così eseguere al programma il ciclo con tutte le funzioni interne del gioco.

### Inizializza
    La funzione "inizializza" serve ad impostare le variabili globali che sono state usate in tutto il codice. 
    Prima vengono definite con la funzione "globale" che le rende richiamabili in tutto il codice, e poi, in base al tipo, viene associato un valore ad ogni variabile.

### Aggiorna e disegna_oggetti
    "aggiorna" e "disegna_oggetti" sono le due funzioni più importanti per il programma. La prima, nonostante sia semplice, serve ad aggiornare in continuazione lo schermo, mentre la seconda serve a far capire al programma quali immagini debbano comparire sullo schermo.
    Queste due funzioni sono quindi complementari perché la prima è indispensabile affinché la seconda possa far apparire le immagini e creare quindi i movimenti che compongono il gioco.

### Sconfitta
    La funzione "sconfitta" viene eseguita nel momento in cui lo sprite del personaggio comandato dal giocatore entra in contatto con uno sprite nemico. Questo avvenimento cambia la variabile "ricominciamo" da "True" a "False, interrompendo così il ciclo iniziato dalla funzione "start" e passando alla schermata di game over.
    Nella schermata di game over viene poi mostrato, sempre dalla funzione "sconfitta", il punteggio totalizzato nella partita ed mostrerà anche la classifica personale e quella globale.


</br>

***

## Salvataggio dati
    I dati che verranno salvati nel gioco sono: nome del giocatore e punteggio del giocatore.
    Nome del giocatore e punteggio del giocatore verranno salvati da remoto su un database. Il primo verrà salvato nella funzione "start", mentre il secondo nella funzione "sconfitta".
    Il salvataggio da remoto di suddetti dati permetterà la creazione di una classifica globale di tutti i giocatori.
    I punteggi del giocatore verranno salvati anche in locale per creare una classifica personale dei migliori punteggi ottenuti.
</br>

</br></br>
# Utilizzo coniche



## Retta
 * __Traiettoria dei proiettili__
(i proiettili seguiranno i punti di una retta parallela alla base e con origine la y del personaggio nel momento in cui ha sparato)
</br></br>
* __Traiettoria proiettili drone__
(i proiettili del drone ottenuto grazie al power up seguiranno i punti di una retta passante per le coordinate del drone (P1) e del nemico (P2)
</br></br>
* __Traiettoria nemici__
(i nemici si muoveranno nel verso opposto al personaggio seguendo una retta parallela al pavimento che ha la coordinata della y generata casualmente, in base a dove si trova il personaggio)
</br></br>
* __Salto__
(il salto del personaggio segue i punti di una retta perpendicolare alla base)
</br></br>
***
</br>

## Parabola

* __Traiettoria nemici__
(ci saranno dei nemici che per muoversi seguiranno delle lista di punti di parabole)
</br></br>
* __Traiettoria palla di neve__
(con il power-up si potrà lanciare una palla di neve che rimbalzerà seguendo i punti di delle parabole)
</br></br>
***
</br>

## Circonferenza

* __Movimento nemici__
(ci sarà un tipo di nemico che per muoversi seguirà delle liste di punti di circonferenze)
</br></br>
* __Scudo__
(il power up dello scudo eliminerà tutti quei colpi che raggiungeranno le coordinate della circonferenza che ha per centro le coordinate del personaggio)
</br></br>


***
