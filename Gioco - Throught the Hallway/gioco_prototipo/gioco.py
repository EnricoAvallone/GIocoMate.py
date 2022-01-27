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

sfondo = pygame.image.load("sfondo_luna.png")
uccello = pygame.image.load("uccello.png")
base = pygame.image.load("basecorriodio.png")
#game_over = pygame.image.load("uccello.png")



clk = pygame.time.Clock()



#Costanti globali
SCHERMO = pygame.display.set_mode((700,400))
FPS = 50
VEL_AVANZ = 5



def inizializza():
    
    global all_sprites, all_enemies, clock, proiettili_dict, nemici_dict, n_P ,n_N , salto, gravity, yinizio
    global uccellox, uccelloy
    global basex, sfondox
    global  nemico, allsprites, allenemies
    uccellox, uccelloy = 60,150
    basex = 0
    sfondox = 0
    proiettili_dict = {}
    nemici_dict = {}
    nemico = False
    salto = False
    allsprites= "vuoto"
    allenemies= ""
    all_sprites.empty()
    all_enemies.empty()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = 0
    n_P= 0
    n_N= 0
    gravity=7
    yinizio=[]

    
    


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def disegna_oggetti():
    SCHERMO.blit(sfondo, (sfondox,-1550))
    SCHERMO.blit(base, (basex,0))
    SCHERMO.blit(uccello, (60,uccelloy))
    if allsprites == "vuoto":
        all_sprites.empty()
        pass
    else:
        all_sprites.draw(SCHERMO)
    
    all_enemies.draw(SCHERMO)

    
    
    


def hai_perso():
    #SCHERMO.blit(game_over, (50,180))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()

#inizializzo Variabili
inizializza()
### Ciclo Principale ###


while True:
    basex -= VEL_AVANZ
    sfondox -= VEL_AVANZ
    if sfondox < -3328: sfondox = 0
    if basex < -0: basex = 0
    keys=pygame.key.get_pressed()

    

    if uccelloy == 320:
        gravity = 320
        uccelloy = gravity
    elif uccelloy < 320: 
        uccelloy += gravity
        gravity = 8
    
    


    if keys[K_SPACE] and uccelloy > 319:
        salto =True
        
        
    
        
    if salto == True:

        if uccelloy > 240:
            gravity = -7
            uccelloy += gravity
        else:
            gravity = 8
            salto = False
        yinizio.clear()

    
    

    for event in pygame.event.get():

        
       
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:

            n_P += 1
            n_proiettile= (n_P)
            spr_proiettile = pygame.sprite.Sprite(all_sprites)
            spr_proiettile.image = pygame.image.load("proiettile.png")
            spr_proiettile.rect = spr_proiettile.image.get_rect()
            spr_proiettile.rect.topright = (uccellox, uccelloy)

            proiettili_dict.update({n_proiettile: spr_proiettile})


        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                inizializza()
        
        if event.type == pygame.QUIT:
                pygame.quit()

        if event.type == pygame.USEREVENT: 
            clock += 1
            if clock == 5:

                n_N += 1
                n_nemico= (n_N)
                spr_ghost = pygame.sprite.Sprite(all_enemies)
                spr_ghost.image = pygame.image.load("uccello.png")
                spr_ghost.rect = spr_ghost.image.get_rect()
                spr_ghost.rect.topright= (SCHERMO.get_width()-30, random.randrange(200, 320))

                nemici_dict.update({n_nemico: spr_ghost})

                clock= 0

                
    
                
    
    for i in proiettili_dict:
 
        proiettile_attivo = proiettili_dict[i]
        for a in nemici_dict:
            nemico_attivo = nemici_dict[a]
            if nemico_attivo.alive()== True:
                nemico_attivo = nemici_dict[a]
                if pygame.sprite.spritecollide(nemico_attivo, all_sprites, True):
                    nemico_attivo.kill()
                else:
                    pass
            else:
                pass

        if proiettile_attivo.rect.x < SCHERMO.get_width()-10:
            allsprites = "pieno"
            proiettile_attivo.rect.x += 30
                    
        else:
            allsprites = "vuoto"


   


        
        
    


    
    disegna_oggetti()
    aggiorna()