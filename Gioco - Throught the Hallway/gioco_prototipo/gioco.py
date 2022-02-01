from time import time
import pygame
from pygame.locals import *
import random
import os

from pygame.constants import K_0, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_UP, KEYDOWN, KEYUP, K_a, K_d, K_s, K_w
from pygame.time import Clock

os.chdir ("Gioco - Throught the Hallway/gioco_prototipo")

pygame.init()
random.seed()

all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
proiettili_all_enemies = pygame.sprite.Group()
personaggio = pygame.sprite.Group()

sfondo = pygame.image.load("sfondo_luna.png")
base = pygame.image.load("base_corridoio.png")
game_over = pygame.image.load("game_over.png")

uccello = pygame.sprite.Sprite(personaggio)
uccello.image = pygame.image.load("uccello.png")

fnt = pygame.font.SysFont("Times New Roman", 40)
fnt_life = pygame.font.SysFont("Times New Roman", 10)


palla_di_neve = pygame.image.load("PalladiNeve.png")
drone = pygame.image.load("Drone.png")
scudo = pygame.image.load("Scudo.png")





clk = pygame.time.Clock()



#Costanti globali
SCHERMO = pygame.display.set_mode((700,400))
FPS = 50
VEL_AVANZ = 9



def inizializza():
    #global power-up
    global power_up, shuffle_pu
    #global uccello
    global uccellox, uccelloy, proiettili_dict, salto, gravity
    #global sfondo
    global basex, sfondox
    #global nemici 
    global  nemico, allsprites, allenemies, nemici_dict, n_N, all_enemies, nemici_life
    #global orologi
    global clock_nemici, clock_jetpack, orologio_j,tempo, tempo_spawn
    #global proiettili nemici
    global nemici_proiettili_dict, nemici_allsprites, nemici_firerate, sparo_nemici, proiettili_all_enemies, nemici_n_proiettile
    #global proiettili amici
    global n_P, all_sprites, punti_dict, traiettoria, n_list

    tempo = 0
    uccellox, uccelloy = 60,150
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
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock_nemici = 0
    clock_jetpack = 0
    orologio_j = False
    n_P= 0
    n_N= 0
    gravity=7
    nemici_firerate = 0
    sparo_nemici = False
    nemici_n_proiettile= 0
    n_list = 0
    punti_dict = {}
    traiettoria = uccellox
    tempo_spawn = 5
    power_up = [palla_di_neve, drone, scudo]
    shuffle_pu = random.choice(power_up)
    
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
            scritta_vita = nemici_life[hp]
            vita_text = fnt_life.render(str(scritta_vita), True, (127, 255, 212))
            SCHERMO.blit(vita_text, (nemico_attivo.rect.x, nemico_attivo.rect.y-5))

    uccello.rect = uccello.image.get_rect()
    uccello.rect.topright = ( 60 , uccelloy)
    personaggio.draw(SCHERMO)


    if allsprites == "vuoto":
        all_sprites.empty()
        pass
    else:
        all_sprites.draw(SCHERMO)

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
inizializza()
### Ciclo Principale ###


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
    if tempo == 299:
        tempo_spawn = 2

    if clock_nemici == tempo_spawn:
        clock_nemici= 0
        n_N += 1
        hp = 4
        spr_ghost = pygame.sprite.Sprite(all_enemies)
        spr_ghost.image = pygame.image.load("uccello.png")
        spr_ghost.rect = spr_ghost.image.get_rect()
        spr_ghost.rect.topright= (SCHERMO.get_width()-30, random.randrange(240, 320))

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
                spr_proiettile.image = pygame.image.load("proiettile.png")
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