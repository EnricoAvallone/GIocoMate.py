#importo le librerie
from typing import Counter
import pygame
from pygame.locals import *
import random
import os
from pygame.time import Clock

#indirizzo il percorso alla cartella dove sono presenti le immagini
os.chdir ("Throught_the_Hallway/gioco/images")

#avvio le librerie
pygame.init()
random.seed()


##definisco i gruppi di sprites##
all_powerup = pygame.sprite.Group()#gli sprite dei powerups
all_help = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()#gli sprite dei proiettili amici
all_enemies1 = pygame.sprite.Group()#gli sprite dei nemici
all_enemies2 = pygame.sprite.Group()#gli sprite dei nemici 2
proiettili_all_enemies = pygame.sprite.Group()#gli sprite dei proiettili nemici
personaggio = pygame.sprite.Group()#lo sprite del personaggio
uccello = pygame.sprite.Sprite(personaggio)#assegno lo sprite al gruppo
spr_scudo = pygame.sprite.Sprite(all_help)


##ricavo le immagini necessarie##
sfondo_iniziale1 = pygame.image.load("Sfondo_iniziale_1.png")
sfondo_iniziale2 = pygame.image.load("Sfondo_iniziale_2.png")
sfondo = pygame.image.load("Sfondo_corridoio_1.png")
base = pygame.image.load("base_corridoio.png")
game_over = pygame.image.load("game_over.png")
vita100 = pygame.image.load("vita_100%.png")
vita50 = pygame.image.load("vita_50%.png")
vita75 = pygame.image.load("vita_75%.png")
vita25 = pygame.image.load("vita_25%.png")
palla_di_neve = pygame.image.load("PalladiNeve.png")
drone = pygame.image.load("Drone.png")
scudo = pygame.image.load("Scudo.png")

uccello.image = pygame.image.load("Protagonista con Jetpack.png") #assegno l'immagine in questo modo poichè il personaggio è sottoforma di sprite
uccello.rect = uccello.image.get_rect()
uccello.rect.update(50,0,50,187)

spr_scudo.image = pygame.image.load("scudoamico.png")
spr_scudo.rect = spr_scudo.image.get_rect()
spr_scudo.rect.update(0,0,300,300)


#Costanti globali
SCHERMO = pygame.display.set_mode((1400,800))
FPS = 180
VEL_AVANZ = 12




def inizializza(): 
    ##creo/inizializzo quasi tutte le variabili che andrò ad usare nel codice 
    ## questa funzione serve anche a resettare tutte le variabili una volta restartato il gioco

    ##le rendo sempre accessibili##
    # - global power-up
    global power_up, shuffle_pu, powerup_dict, n_M, all_powerup, allpowerup, spawn, type_powerup, timerdrone, timerpalladineve, timerscudo, timerdrone_, timerpalladineve_, timerscudo_, droppalladineve, dropdrone, dropscudo, scudo
    # - global uccello
    global uccellox, uccelloy, proiettili_dict, salto, gravity, n_salti, counter_salti, dimensioni
    # - global sfondo
    global basex, sfondox
    # - global nemici 
    global  nemico, allsprites, allenemies2, nemici_dict, n_N, all_enemies1, nemici_life, n_K, all_enemies2, nemici2_dict, nemici2_life
    # - global orologi
    global clock_nemici1, clock_jetpack, orologio_j,tempo, tempo_spawn1, clk_spawn_pu, tempo_spawn2, clock_nemici2
    # - global proiettili nemici
    global nemici_proiettili_dict, nemici_allsprites, nemici_firerate, sparo_nemici, proiettili_all_enemies, nemici_n_proiettile
    # - global proiettili amici
    global n_P, all_sprites, punti_dict, traiettoria, n_list

    global surf_text, fnt, past

    
    uccelloy = 500 #posizione personaggio ad inizio gioco
    basex = 0
    sfondox = 0
    proiettili_dict = {}
    nemici_proiettili_dict = {}
    nemici_dict = {}
    nemici_life = {}
    nemici2_dict = {}
    nemici2_life = {}
    nemico = False
    salto = False
    allsprites= "vuoto"
    nemici_allsprites = "vuoto"
    allenemies2= "vuoto"
    all_sprites.empty()
    all_enemies1.empty()
    all_enemies2.empty()
    proiettili_all_enemies.empty()
    nemici_proiettili_dict.clear()
    nemici_dict.clear()
    nemici_life.clear()
    proiettili_dict.clear()
    nemici2_life.clear()
    
    ##TIMER##
    pygame.time.set_timer(pygame.USEREVENT, 1000) #ogni secondo avviene USEREVENT, utilizzo questo evento per far funzionare tutti i timer
    clock_nemici1 = 0 #per determinare ogni quanto spawnino i nemici
    clock_nemici2 = 0 #per determinare ogni quanto spawnino i nemici
    clock_jetpack = 0 #per determinare il tempo di utilizzo del jetpack
    tempo = 0 #tempo generale che fornisce il punteggio
    nemici_firerate = 0#per determinare il tempo che passa tra gli spari nemici
    orologio_j = False #variabile per far attivare e disattivare il jetpack
    timerscudo = False
    timerpalladineve = False
    timerdrone = False
    timerscudo_ = 0
    timerpalladineve_ = 0
    timerdrone_ = 0
    
    ##NOMI DICT##
    ##utilizzo delle variabili per dare un nome agli elementi da inserire nei dizionari
    n_P= 0 #nome proiettile 
    n_N= 0 #nome nemico 
    n_M = 0 #nome power-up
    n_K = 0 #nome nemici 2

    gravity=0 #la velocità con cui il personaggio cade inizialmente
    sparo_nemici = False #quando diventa True (tramite "nemici_firerate") i nemici sparano
    nemici_n_proiettile= 0
    n_list = 0
    punti_dict = {}
    traiettoria = 200
    tempo_spawn1 = 0
    tempo_spawn2 = 7
    powerup_dict = {}
    powerup_dict.clear()
    allpowerup = "Vuoto"
    all_powerup.empty()
    power_up = [palla_di_neve, drone, scudo]
    shuffle_pu = random.choice(power_up)
    clk_spawn_pu = 0
    spawn = False
    past = False
    type_powerup = {}
    dropscudo = False
    dropdrone = False
    droppalladineve = False
    n_salti = 0
    counter_salti = False
    dimensioni = 0
    scudo = False
    ##definisco il font e la grandezza dei testi##
    fnt = pygame.font.SysFont("Times New Roman", 40) #numeri punteggio in alto a destra
    


    

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
#200
#9000
def disegna_oggetti():
    SCHERMO.blit(sfondo, (sfondox,0))
    SCHERMO.blit(base, (basex,200))
    
    uccello.rect.topright = ( 200 , uccelloy)
    personaggio.draw(SCHERMO)

    surf_text = fnt.render(str(tempo), True, (255, 255, 0), None)
    SCHERMO.blit(surf_text, (600, 10))

    if dropdrone == True:
        all_help.draw(SCHERMO)
    else:
        pass

    if droppalladineve == True:
        all_help.draw(SCHERMO)
    else:
        pass

    if dropscudo == True:
        all_help.draw(SCHERMO)
    else:
        pass

    for hp in nemici_dict:
        nemico_attivo = nemici_dict[hp]

        if nemico_attivo.alive()== True:
            pos_x = nemico_attivo.rect.x
            pos_y = nemico_attivo.rect.y

            if nemici_life[hp] == 4:
                SCHERMO.blit(vita100, (pos_x +4, pos_y-5))
            elif nemici_life[hp] == 3:
                SCHERMO.blit(vita75, (pos_x +4, pos_y-5))
            elif nemici_life[hp] == 2:
                SCHERMO.blit(vita50, (pos_x +4, pos_y-5))
            elif nemici_life[hp] == 1:
                SCHERMO.blit(vita25, (pos_x +4, pos_y-5))

    for hp in nemici2_dict:
        nemico2_attivo = nemici2_dict[hp]

        if nemico2_attivo.alive()== True:
            pos_x = nemico2_attivo.rect.x
            pos_y = nemico2_attivo.rect.y

            if nemici2_life[hp] == 4:
                SCHERMO.blit(vita100, (pos_x +4, pos_y-5))
            elif nemici2_life[hp] == 3:
                SCHERMO.blit(vita75, (pos_x +4, pos_y-5))
            elif nemici2_life[hp] == 2:
                SCHERMO.blit(vita50, (pos_x +4, pos_y-5))
            elif nemici2_life[hp] == 1:
                SCHERMO.blit(vita25, (pos_x +4, pos_y-5))
    
    if scudo == True:
        spr_scudo.rect.topright = (300, uccelloy-100)
    elif scudo == False:
        spr_scudo.remove


    if allsprites == "vuoto":
        all_sprites.empty()
        pass
    else:
        all_sprites.draw(SCHERMO)

    if allpowerup == "vuoto":
        all_powerup.empty()
        pass
    else:
        all_powerup.draw(SCHERMO)


    if allenemies2 == "vuoto":
        all_enemies2.empty()
        pass
    else:
        all_enemies2.draw(SCHERMO)


    if nemici_allsprites == "vuoto" and sparo_nemici == False:
        proiettili_all_enemies.empty()
        pass
    else:
        proiettili_all_enemies.draw(SCHERMO)



    
    all_enemies1.draw(SCHERMO)
    all_enemies2.draw(SCHERMO)


def hai_perso():
    pygame.mixer.music.load("sus.mp3")
    pygame.mixer.music.play(1, 0)
    SCHERMO.blit(game_over, (0,0))
    scritta_punteggio = "      total score: "+str(tempo)+"       "
    print(scritta_punteggio)
    surf_text = fnt.render(scritta_punteggio, True, (0, 0, 0), (255, 255, 0))
    SCHERMO.blit(surf_text, (150, 270))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                inizializza()
                ricominciamo = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()

#inizializzo Variabili
### Ciclo Principale ###
def start():
    global ricominciamo, fnt

    SCHERMO.blit(sfondo_iniziale1, (0, 0))

    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                if 613 <  mouse[0] < 784:#x
                    if 243 <  mouse[1] < 333:#y
                        SCHERMO.blit(sfondo_iniziale2, (0, 0))

                        inizializza()
                        aggiorna()
                        disegna_oggetti()
                        ricominciamo = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()


start()




























if ricominciamo == True:
    while True:
        basex -= VEL_AVANZ
        sfondox -= VEL_AVANZ
        if sfondox < -4200: sfondox = 0
        if basex < -2100: basex = 0
        


        keys=pygame.key.get_pressed()
    

        if uccelloy == 530:
            uccelloy = 530
        elif uccelloy < 530: 
            uccelloy += gravity
            gravity = 14
    

        if uccelloy > 528:
            n_salti = 0
            

        
    
        if keys[K_ESCAPE]:
            pygame.quit()

        
        if keys[K_j]:
    
            if clock_jetpack < 3:
                orologio_j = True
                if uccelloy == 0:
                    uccelloy = 0
                if uccelloy > 0:
                    gravity =-5
                    uccelloy += gravity
                 
            
        

        if tempo == 0:
            tempo_spawn1 = 10
        if tempo == 51:
            tempo_spawn1 = 4
        if tempo == 100:
            tempo_spawn1 = 3
        if tempo == 300:
            tempo_spawn1 = 2

    

        if clock_nemici1 == tempo_spawn1:
            clock_nemici1= 0
            n_N += 1
            hp = 4
            spr_ghost = pygame.sprite.Sprite(all_enemies1)
            spr_ghost.image = pygame.image.load("Nemico.png")
            
            spr_ghost.rect = spr_ghost.image.get_rect()
            spr_ghost.rect.topright= (SCHERMO.get_width()-30, random.randrange(440, 600))

            nemici_dict.update({n_N: spr_ghost})
            nemici_life.update({n_N: hp})
        
        else:
            pass

        if clock_nemici2 == tempo_spawn2:
            clock_nemici2= 0
            n_K += 1
            hp = 4
            spr_enemies = pygame.sprite.Sprite(all_enemies2)
            spr_enemies.image = pygame.image.load("Nemico.png")
            spr_enemies.rect = spr_enemies.image.get_rect()
            spr_enemies.rect.topright= (SCHERMO.get_width()-30, random.randrange(340, 640))

            nemici2_dict.update({n_K: spr_enemies})
            nemici2_life.update({n_K: hp})
        
        else:
            pass


        if nemici_firerate == 3:
            sparo_nemici = True
    
        if sparo_nemici == True:

            for b in nemici_dict:
                nemico_attivo = nemici_dict[b]
                if nemico_attivo.alive() == True:
                    nemici_n_proiettile += 1
                    spr_proiettile = pygame.sprite.Sprite(proiettili_all_enemies)
                    spr_proiettile.image = pygame.image.load("proiettile_nemico.png")
                    spr_proiettile.rect = spr_proiettile.image.get_rect()
                    spr_proiettile.rect.topright = (nemici_dict[b].rect.x, nemici_dict[b].rect.y)

                    nemici_proiettili_dict.update({nemici_n_proiettile: spr_proiettile})
                    nemici_firerate = 0
                    sparo_nemici = False

        if counter_salti == True:
            if n_salti == 0:          
                dimensioni = uccelloy-190
            if n_salti == 1:          
                dimensioni = uccelloy-120
            n_salti +=1
            salto = True

            counter_salti = False

        if salto == True:
            if uccelloy > dimensioni:
                gravity = -15
                uccelloy += gravity
            else:
                dimensioni = 0
                salto = False




        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and n_salti < 2:
                counter_salti =True
            
       
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            
                pygame.mixer.music.load("sparo.mp3")
                pygame.mixer.music.play(1, 0)
                n_P += 1
                spr_proiettile = pygame.sprite.Sprite(all_sprites)
                spr_proiettile.image = pygame.image.load("proiettile.png")
                spr_proiettile.rect = spr_proiettile.image.get_rect()
            

                for i in range(700):
                    n_list += 1
                    traiettoria += 1
                    tupla = [traiettoria , uccelloy+65]
                    punti_dict.update({n_list: tupla})

            #print(punti_dict)
                punti_dict.clear()
                n_list = 0

                spr_proiettile.rect.topright = (250, uccelloy+65)
                proiettili_dict.update({n_P: spr_proiettile})


            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    inizializza()
        
            if event.type == pygame.QUIT:
                    pygame.quit()

            if event.type == pygame.USEREVENT: 
                clk_spawn_pu += 1
                tempo += 1
                clock_nemici1 += 1
                nemici_firerate += 1
                clock_nemici2 += 1
                if orologio_j == True:
                    clock_jetpack += 1
                    if clock_jetpack == 10:
                        clock_jetpack = 0
                        orologio_j = False
        
                if timerdrone == True:
                    timerdrone_+=1

                if timerpalladineve == True:
                    timerpalladineve_ += 1

                if timerscudo == True:
                    timerscudo_ += 1




                   


        
        
        
    
        for i in proiettili_dict:
 
            proiettile_attivo = proiettili_dict[i]
            for a in nemici_dict:
                nemico_attivo = nemici_dict[a]
           
                if nemico_attivo.alive()== True:
                    nemico_attivo = nemici_dict[a]
            
                    if pygame.sprite.spritecollide(nemico_attivo, all_sprites, True):
                        if nemici_life:
                            nemici_life[a] -= 2
                            if nemici_life[a] == 0:
                                nemico_attivo.kill()
                                nemici_life.pop(a)
                    
                    else:
                        pass

            for b in nemici2_dict:
                nemico2_attivo = nemici2_dict[b]
                if nemico2_attivo.alive()== True:
                    nemico2_attivo = nemici2_dict[b]
            
                    if pygame.sprite.spritecollide(nemico2_attivo, all_sprites, True):
                        if nemici2_life:
                            nemici2_life[b] -= 2
                            if nemici2_life[b] == 0:
                                nemico2_attivo.kill()
                                nemici2_life.pop(b)
                    
                    else:
                        pass
                
                
                else:
                    pass

            if proiettile_attivo.rect.x < SCHERMO.get_width()-10:
                allsprites = "pieno"
                proiettile_attivo.rect.x += 30
                    
            else:
                allsprites = "vuoto"



        if timerdrone_ > 0 and timerdrone_ < 10:
            dropdrone = True
            spr_drone = pygame.sprite.Sprite(all_help)
            spr_drone.image = pygame.image.load("DroneAmico.png")
            spr_drone.rect = spr_drone.image.get_rect()
            spr_drone.rect.topright = (50, 50)
        elif timerdrone_ == 10:
            dropdrone = False
            timerdrone = False
            timerdrone_ = 0
            all_powerup.empty()

        if timerpalladineve_ > 0 and timerpalladineve_ < 10:
            droppalladineve = True
        elif timerpalladineve_ == 10:
            droppalladineve = False
            timerpalladineve = False
            timerpalladineve_ = 0
            all_powerup.empty()        
        
        if timerscudo == 1:
            dropscudo = True
            scudo = True
            

            
            

        if timerscudo_ == 15:
            scudo = False
            dropscudo = False 
            timerscudo = False
            timerscudo_ = 0

        if clk_spawn_pu== 30:
            clk_spawn_pu = 0
            n_M += 1
            spr_powerup = pygame.sprite.Sprite(all_powerup)

            #u = int(random.randrange(1,4))
            u = 1
            if u == 1:
                spr_powerup.image = pygame.image.load("Scudo.png")
                type_powerup.update({n_M: "scudo"})
            elif u == 2:
                spr_powerup.image = pygame.image.load("Drone.png")
                type_powerup.update({n_M: "drone"})
            elif u == 3:
                spr_powerup.image = pygame.image.load("PalladiNeve.png")
                type_powerup.update({n_M: "palladineve"})
            spr_powerup.rect = spr_powerup.image.get_rect()
            spr_powerup.rect.topright= (SCHERMO.get_width()-10, random.randrange(300, 720))
        

            powerup_dict.update({n_M: spr_powerup})


        for e in powerup_dict:
            powerup_attivo = powerup_dict[e]

            if powerup_attivo.alive()== True:
                
                if pygame.sprite.spritecollide(uccello, all_powerup , True):
                    if type_powerup[e] == "palladineve":
                        timerpalladineve = True
                        powerup_attivo.kill()
                    elif type_powerup[e] == "drone":
                        timerdrone = True
                        powerup_attivo.kill()
                    elif type_powerup[e] == "scudo":
                        timerscudo = True
                        powerup_attivo.kill()
                        
            else:
                pass
            
            if powerup_attivo.rect.x > 0:
                allpowerup = "pieno"
                powerup_attivo.rect.x -= 5                
            else:
                allpowerup = "vuoto"
                powerup_attivo.kill()
        

        
                                
        
        for t in nemici2_dict:
            nemico2_attivo = nemici2_dict[t]
            
            if nemico2_attivo.rect.x > 0:
                allenemies2 = "pieno"
                nemico2_attivo.rect.x -= 10
            else:
                allenemies2 = "vuoto"
                nemico2_attivo.kill()
   

        for n in nemici_proiettili_dict:
            nemici_proiettile_attivo = nemici_proiettili_dict.get(n)
            if not nemici_proiettile_attivo == None:


                if nemici_proiettile_attivo.rect.x > 0:
                    nemici_allsprites = "pieno"
                    nemici_proiettile_attivo.rect.x -= 25
            
                        
                else:
                    nemici_allsprites = "vuoto"
                    nemici_proiettile_attivo.kill()

                if scudo == True and pygame.sprite.spritecollide(spr_scudo, proiettili_all_enemies, True):
                    nemici_proiettile_attivo.rect.x = 0

                
                if scudo == True and pygame.sprite.spritecollide(spr_scudo, all_enemies2, True):
                    pass

                if pygame.sprite.spritecollide(uccello, proiettili_all_enemies, True) or pygame.sprite.spritecollide(uccello, all_enemies2, True):
                    nemici_proiettile_attivo.rect.x = 0
                    hai_perso()
                

                else:
                    pass

        
                    
    


        aggiorna()
        disegna_oggetti()
        