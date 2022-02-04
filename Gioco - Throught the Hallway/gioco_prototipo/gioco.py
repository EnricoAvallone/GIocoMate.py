#importo le librerie
import pygame
from pygame.locals import *
import random
import os
from pygame.time import Clock

#indirizzo il percorso alla cartella dove sono presenti le immagini
os.chdir ("Gioco - Throught the Hallway/gioco_prototipo")

#avvio le librerie
pygame.init()
random.seed()


##definisco i gruppi di sprites##
all_powerup = pygame.sprite.Group()#gli sprite dei powerups
all_sprites = pygame.sprite.Group()#gli sprite dei proiettili amici
all_enemies = pygame.sprite.Group()#gli sprite dei nemici
proiettili_all_enemies = pygame.sprite.Group()#gli sprite dei proiettili nemici
personaggio = pygame.sprite.Group()#lo sprite del personaggio
uccello = pygame.sprite.Sprite(personaggio)#assegno lo sprite al gruppo


##ricavo le immagini necessarie##
sfondo = pygame.image.load("sfondo_luna.png")
base = pygame.image.load("base_corridoio.png")
game_over = pygame.image.load("game_over.png")
vita100 = pygame.image.load("vita_100%.png")
vita50 = pygame.image.load("vita_50%.png")
vita75 = pygame.image.load("vita_75%.png")
vita25 = pygame.image.load("vita_25%.png")
palla_di_neve = pygame.image.load("PalladiNeve.png")
drone = pygame.image.load("Drone.png")
scudo = pygame.image.load("Scudo.png")
uccello.image = pygame.image.load("uccello.png") #assegno l'immagine in questo modo poichè il personaggio è sottoforma di sprite


##definisco il font e la grandezza dei testi##
fnt = pygame.font.SysFont("Times New Roman", 40) #numeri punteggio in alto a destra


#Costanti globali
SCHERMO = pygame.display.set_mode((700,400))
FPS = 60
VEL_AVANZ = 9



def inizializza(): 
    ##creo/inizializzo quasi tutte le variabili che andrò ad usare nel codice 
    ## questa funzione serve anche a resettare tutte le variabili una volta restartato il gioco

    ##le rendo sempre accessibili##
    # - global power-up
    global power_up, shuffle_pu, powerup_dict, n_pu, all_powerup, allpowerup, spawn
    # - global uccello
    global uccellox, uccelloy, proiettili_dict, salto, gravity
    # - global sfondo
    global basex, sfondox
    # - global nemici 
    global  nemico, allsprites, allenemies, nemici_dict, n_N, all_enemies, nemici_life
    # - global orologi
    global clock_nemici, clock_jetpack, orologio_j,tempo, tempo_spawn, clk_spawn_pu
    # - global proiettili nemici
    global nemici_proiettili_dict, nemici_allsprites, nemici_firerate, sparo_nemici, proiettili_all_enemies, nemici_n_proiettile
    # - global proiettili amici
    global n_P, all_sprites, punti_dict, traiettoria, n_list

    
    uccellox, uccelloy = 60,150 #posizione personaggio ad inizio gioco
    basex = 0
    sfondox = 0
    proiettili_dict = {}
    nemici_proiettili_dict = {}
    nemici_dict = {}
    nemici_life = {}
    nemico = False
    salto = False
    allsprites= "vuoto"
    nemici_allsprites = "vuoto"
    allenemies= ""
    all_sprites.empty()
    all_enemies.empty()
    proiettili_all_enemies.empty()
    nemici_proiettili_dict.clear()
    nemici_dict.clear()
    nemici_life.clear()
    proiettili_dict.clear()
    
    pygame.time.set_timer(pygame.USEREVENT, 1000) #ogni secondo avviene USEREVENT, utilizzo questo evento per far funzionare tutti i timer
    clock_nemici = 0 #per determinare ogni quanto spawnino i nemici
    clock_jetpack = 0 #per determinare il tempo di utilizzo del jetpack
    tempo = 0 #tempo generale che fornisce il punteggio
    nemici_firerate = 0#per determinare il tempo che passa tra gli spari nemici
    orologio_j = False #variabile per far attivare e disattivare il jetpack
    
    ##utilizzo delle variabili per dare un nome agli elementi da inserire nei dizionari
    n_P= 0 #nome proiettile 
    n_N= 0 #nome nemico 
    n_pu = 0 #nome power-up

    gravity=7 #la velocità con cui il personaggio cade inizialmente
    
    sparo_nemici = False
    nemici_n_proiettile= 0
    n_list = 0
    punti_dict = {}
    traiettoria = uccellox
    tempo_spawn = 5
    powerup_dict = {}
    powerup_dict.clear()
    allpowerup = "Vuoto"
    all_powerup.empty()
    power_up = [palla_di_neve, drone, scudo]
    shuffle_pu = random.choice(power_up)
    clk_spawn_pu = 0
    spawn = False
    
    aggiorna()
    

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def disegna_oggetti():
    SCHERMO.blit(sfondo, (sfondox,-1550))
    SCHERMO.blit(base, (basex,0))
    SCHERMO.blit(surf_text, (600, 10))
    #SCHERMO.blit(shuffle_pu, (350, 250))

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


    uccello.rect = uccello.image.get_rect()
    uccello.rect.topright = ( 60 , uccelloy)
    personaggio.draw(SCHERMO)


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
    

    if nemici_allsprites == "vuoto" and sparo_nemici == False:
        proiettili_all_enemies.empty()
        pass
    else:
        proiettili_all_enemies.draw(SCHERMO)
    
    all_enemies.draw(SCHERMO)



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
    global ricominciamo
    SCHERMO.blit(sfondo, (-800, -700))
    scritta_punteggio = " Per giocare clicca il tasto sinistro "+"       "
    surf_text = fnt.render(scritta_punteggio, True, (0, 0, 0), (50, 50, 255))
    SCHERMO.blit(surf_text, (35, 190))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                inizializza()
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
        if sfondox < -3328: sfondox = 0
        if basex < -2800: basex = 0
        surf_text = fnt.render(str(tempo), True, (255, 255, 0), None)


        keys=pygame.key.get_pressed()
    

        if uccelloy == 320:
            gravity = 320
            uccelloy = gravity
        elif uccelloy < 320: 
            uccelloy += gravity
            gravity = 8
    
    


        if keys[K_SPACE] and uccelloy > 319:
            salto =True
    
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
                 
            
        
        if salto == True:

            if uccelloy > 240:
                gravity = -7
                uccelloy += gravity
            else:
                gravity = 8
                salto = False
    
        if tempo == 51:
            tempo_spawn = 4
        if tempo == 100:
            tempo_spawn = 3
        if tempo == 300:
            tempo_spawn = 2



        

        if clk_spawn_pu== 35:
            clk_spawn_pu = 0
            n_M += 1
            spr_powerup = pygame.sprite.Sprite(all_powerup)

        #palla_di_neve = pygame.image.load("PalladiNeve.png")
        #drone = pygame.image.load("Drone.png")
        #scudo = pygame.image.load("Scudo.png")
            u = int(random.randrange(1,3))
            if u == 1:
                spr_powerup.image = pygame.image.load("Scudo.png")
            elif u == 2:
                spr_powerup.image = pygame.image.load("Drone.png")
            else:
                spr_powerup.image = pygame.image.load("PalladiNeve.png")
            spr_powerup.rect = spr_powerup.image.get_rect()
            spr_powerup.rect.topright= (SCHERMO.get_width()-10, random.randrange(10, 320))
        

            powerup_dict.update({n_M: spr_powerup})

    

        if clock_nemici == tempo_spawn:
            clock_nemici= 0
            n_N += 1
            hp = 4
            spr_ghost = pygame.sprite.Sprite(all_enemies)
            spr_ghost.image = pygame.image.load("uccello.png")
            spr_ghost.rect = spr_ghost.image.get_rect()
            spr_ghost.rect.topright= (SCHERMO.get_width()-30, random.randrange(240, 340))

            nemici_dict.update({n_N: spr_ghost})
            nemici_life.update({n_N: hp})
        
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
        else:
            pass



        for event in pygame.event.get():

        
       
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
                    tupla = [traiettoria , uccelloy]
                    punti_dict.update({n_list: tupla})

            #print(punti_dict)
                traiettoria = uccellox
                punti_dict.clear()
                n_list = 0

                spr_proiettile.rect.topright = (uccellox, uccelloy)
                proiettili_dict.update({n_P: spr_proiettile})


            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    inizializza()
        
            if event.type == pygame.QUIT:
                    pygame.quit()

            if event.type == pygame.USEREVENT: 
                clk_spawn_pu+=1
                tempo+=1
                clock_nemici += 1
                nemici_firerate += 1
                if orologio_j == True:
                    clock_jetpack += 1
                    if clock_jetpack == 10:
                        clock_jetpack = 0
                        orologio_j = False
            

                else:
                    nemici_allsprites = "vuoto"
            
                if pygame.sprite.spritecollide(uccello, proiettili_all_enemies, True):
                
                    hai_perso()
                
                else:
                    pass      
    
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
                
                
                else:
                    pass

            if proiettile_attivo.rect.x < SCHERMO.get_width()-10:
                allsprites = "pieno"
                proiettile_attivo.rect.x += 30
                    
            else:
                allsprites = "vuoto"

        for e in powerup_dict:
            powerup_attivo = powerup_dict[e]
    
            if powerup_attivo.rect.x > 0:
                allpowerup = "pieno"
                powerup_attivo.rect.x -= 5                
            else:
                allpowerup = "vuoto"
                powerup_attivo.kill()
           
   
        for n in nemici_proiettili_dict:
            nemici_proiettile_attivo = nemici_proiettili_dict.get(n)
            if not nemici_proiettile_attivo == None:
            


                if nemici_proiettile_attivo.rect.x > 0:
                    nemici_allsprites = "pieno"
                    nemici_proiettile_attivo.rect.x -= 15
            
                        
                else:
                    nemici_allsprites = "vuoto"
                
                if pygame.sprite.spritecollide(uccello, proiettili_all_enemies, True):
                        nemici_proiettile_attivo.rect.x = 0
                        hai_perso()
                    
                else:
                    pass

        
    
    


    
        disegna_oggetti()
        aggiorna()