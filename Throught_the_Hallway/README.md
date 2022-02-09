
# Gioco: _Through the Hallway_
#### [___Avallone Enrico___](https://github.com/EnricoAvallone); [___Ippolito Gabriele___](https://github.com/gabrielecoding); [___Lastrucci Davide___](https://github.com/davidelastrucci)


***
## Indice
1. [Scopo del gioco](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#scopo-del-gioco)
2. [Trama](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#trama)
3. [Svolgimento del gioco](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#svolgimento-del-gioco)
4. [Comandi di gioco](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#comandi-di-gioco)
4. [Power-up](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#power-up)
5. [Utilizzo coniche](https://github.com/EnricoAvallone/GiocoMate.py/tree/AvallonePy/Gioco%20-%20Throught%20the%20Hallway#utilizzo-coniche)

</br>
</br>


***
## Scopo del gioco: 
    Eliminare i nemici e resistere più tempo possibile
</br>

***
## Trama: 
    Ad "X", agente dei servizi segreti, è stata assegnata una missione di spionaggio nella casa bianca, poiché l'FBI sospetta che il presidente voglia usare delle armi nucleari per minacciare la Cina.
    Mentre "X" sta origliando le trattative del presidente con delle persone poco affidabili, viene scoperto, e si ritrova a dover scappare per i corridoi della casa bianca ed affrontare i sistemi di sicurezza della casa bianca, inseguito dalle guardie.
</br>

***
## Svolgimento del gioco: 
    Il personaggio corre in un corridoio infinito e dovrà affrontare varie difese presenti nella casa bianca, se verrà colpito da una difesa morirà e verrà catturato dalle guardie.
    
    Durante la corsa potrà raccogliere i power-up che gli forniranno abilità particolari.
</br>

***
## Comandi di gioco:
</br>

+ __Space-bar__ → salta
+ __J__ → jetpack (massimo 4 secondi poi si deve ricaricare)
+ __F__ → fire(spara)
+ __P__ → powerup
+ __R__ → restart
+ __E__ → (easter-egg)
</br>
</br>

***
## Power-up:
* #### __Palla di neve:__ 
  il colpo successivo all’attivazione lancerà una palla di neve che rimbalzando sul terreno travolgerà tutti i nemici

* #### __Scudo:__ 
  per 10 secondi dall’attivazione si avrà uno scudo che proteggerà dai nemici

* #### __Amico drone:__ 
  arriva un drone che ti aiuta nell’eliminazione dei nemici per 10 secondi
</br>
</br>

***

</br></br></br>
# Utilizzo coniche



## Retta: 
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

## Parabola: 

* __Traiettoria nemici__
(ci saranno dei nemici che per muoversi seguiranno delle lista di punti di parabole)
</br></br>
* __Traiettoria palla di neve__
(con il power-up si potrà lanciare una palla di neve che rimbalzerà seguendo i punti di delle parabole)
</br></br>
***
</br>

## Circonferenza:

* __Movimento nemici__
(ci sarà un tipo di nemico che per muoversi seguirà delle liste di punti di circonferenze)
</br></br>
* __Scudo__
(il power up dello scudo eliminerà tutti quei colpi che raggiungeranno le coordinate della circonferenza che ha per centro le coordinate del personaggio)
</br></br>


***
