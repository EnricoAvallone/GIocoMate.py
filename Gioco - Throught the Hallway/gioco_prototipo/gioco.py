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

sfondo = pygame.image.load("base.png")
uccello = pygame.image.load("uccello.png")
base = pygame.image.load("sfondo_luna.png")
game_over = pygame.image.load("uccello.png")




clk = pygame.time.Clock()



#Costanti globali
SCHERMO = pygame.display.set_mode((512,288))
FPS = 50
VEL_AVANZ = 3



def inizializza():
    
    global all_sprites, all_enemies, set_timer, clock, firerate, proiettili_dict, n, salto, gravity, yinizio
    global uccellox, uccelloy, uccello_vely, uccello_volo
    global basex, sfondox
    global pro_x, pro_y, lancio, nemico, rimuovi, allsprites, allenemies
    uccellox, uccelloy = 60,150
    uccello_vely = 0
    uccello_volo = 2
    basex = 0
    sfondox = 0
    pro_x=500
    proiettili_dict = {}
    nemico = False
    rimuovi = False
    salto = False
    allsprites= "vuoto"
    allenemies = "vuoto"
    all_sprites.empty()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clock = 0
    firerate = 0
    n= 0
    gravity=7
    yinizio=[]

    
    


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def disegna_oggetti():
    SCHERMO.blit(base, (basex,-1550))
    SCHERMO.blit(sfondo, (sfondox,260))
    SCHERMO.blit(uccello, (60,uccelloy))
    if allsprites == "vuoto":
        all_sprites.empty()
        pass
    else:
        all_sprites.draw(SCHERMO)

    if nemico == False:
        all_enemies.empty()
        pass
    else:
        all_enemies.draw(SCHERMO)

                    
    
    


def hai_perso():
    SCHERMO.blit(game_over, (50,180))
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
    if sfondox < -2048: sfondox = 0
    if basex < -3328: basex = 0
    keys=pygame.key.get_pressed()

    

    if uccelloy == 250:
        gravity = 250
        uccelloy = gravity
    elif uccelloy < 250: 
        uccelloy += gravity
        gravity = 6
    
    


    if keys[K_SPACE] and uccelloy > 249:
        salto =True
        
        
    
        
    if salto == True:

        if uccelloy > 170:
            gravity = -6
            uccelloy += gravity
        else:
            gravity = 7
            salto = False
        yinizio.clear()

    
    

    for event in pygame.event.get():

        
       
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:

            n += 1
            n_proiettile= (n)
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
                clock= 0
                nemico = True
                spr_ghost = pygame.sprite.Sprite(all_enemies)
                spr_ghost.image = pygame.image.load("uccello.png")
                spr_ghost.rect = spr_ghost.image.get_rect()
                
                spr_ghost.rect.topright= (SCHERMO.get_width()-30, random.randrange(0, 288))
                
    
    
    
    for i in proiettili_dict:
        proiettile_attivo = proiettili_dict[i]
        if proiettile_attivo.rect.x < SCHERMO.get_width()-10:
            allsprites = "pieno"
            proiettile_attivo.rect.x += 30
            
        else:
            allsprites = "vuoto"


        


        
        
    


    
    disegna_oggetti()
    aggiorna()