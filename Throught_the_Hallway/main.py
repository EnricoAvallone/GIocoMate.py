#importo le librerie
from typing import Counter
import pygame
from pygame.locals import *
import os
from pygame.time import Clock
from genericpath import exists
import redis
import time
import random

class Retta:
    def __init__(self, tipo="PARAMETRI", *args):
        """
        Il tipo è PARAMETRI per a, b, c; COEFFICIENTE per m e un punto; PUNTI per due punti
        """
        if tipo == "PARAMETRI":
            self.__a = args[0]
            self.__b = args[1]
            self.__c = args[2]
        elif tipo == "COEFFICIENTE":
            self.__m = args[0]
            self.__punto = args[1]

            self.__a = -self.__m
            self.__b = 1
            self.__c = self.__m * self.__punto[0] - self.__punto[1]
        elif tipo == "PUNTI":
            self.__punto1 = args[0]
            self.__punto2 = args[1]
            self.__m = (self.__punto2[1] - self.__punto1[1]) / (self.__punto2[0] - self.__punto1[0])
            self.__a = -self.__m
            self.__b = 1
            self.__c = -self.__punto1[0] + self.__punto1[1]
        else:
            raise Exception("Il tipo specificato non è un'opzione")

    # PROPRIETA' DELLA RETTA
    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @property
    def m(self):
        """
        :returns: il coefficiente angolare
        """
        try:
            return self.__m
        except AttributeError:
            if self.__b != 0:
                return -self.__a / self.__b
            else:  # Se b = 0, dai un errore
                raise ZeroDivisionError

    @property
    def q(self):
        """
        :returns: l'intercetta
        """
        if self.__b != 0:
            return -self.__c / self.__b
        else:  # Se b = 0, dai un errore
            raise ZeroDivisionError

    def eqImplicita(self):
        """
        :returns: la stringa dell'equazione implicita
        """
        # PRIMO TERMINE
        incognita_1 = f"{self.__a}x" if self.__a != 0 else ""
        incognita_1 = f"x" if self.__a == 1 else incognita_1
        incognita_1 = f"-x" if self.__a == -1 else incognita_1
        incognita_1 = incognita_1 if self.__a <= 0 else f"+{incognita_1}"

        # SECONDO TERMINE
        incognita_2 = f"{self.__b}y" if self.__b != 0 else ""
        incognita_2 = f"y" if self.__b == 1 else incognita_2
        incognita_2 = f"-y" if self.__b == -1 else incognita_2
        incognita_2 = incognita_2 if self.__b <= 0 else f"+{incognita_2}"

        # TERMINE NOTO
        noto = f"{self.__c}" if self.__c != 0 else ""
        noto = noto if self.__c <= 0 else f"+{noto}"

        return f"{incognita_1}{incognita_2}{noto}=0"

    # FUNZIONI DELLA RETTA
    def eqEsplicita(self):
        """
        :returns: la stringa dell'equazione esplicita
        """
        if self.__b == 0:
            raise ZeroDivisionError

        b = self.__b if self.__b >= 0 else -self.__b

        # VARIABILE INDIPENDENTE
        a = self.__a if self.__b >= 0 else -self.__a

        ind = f"{a}/{b}x" if abs(self.__b) != 1 else f"{a}x"
        ind = ind if abs(a/b) != 1 else f"x"
        ind = ind if a <= 0 else f"+{ind}"
        ind = ind if a != 0 else ""

        # TERMINE NOTO
        c = self.__c if self.__b >= 0 else -self.__c

        noto = f"{c}/{b}" if abs(self.__b) != 1 else f"{c}"
        noto = noto if c <= 0 else f"+{noto}"
        noto = noto if c != 0 else ""

        return f"y={ind}{noto}"

    def trovaY(self, x):
        """
        :returns: la stringa dell'equazione esplicita
        """
        return round(self.__a / self.__b * x + self.__c / self.__b, 2)

    def punti(self, n, m):
        """
        :returns: la stringa dell'equazione esplicita
        """
        return [(i, self.trovaY(i)) for i in range(min(n, m), max(n, m) + 1, 30)]

    def intersezione(self, retta1):
        if type(retta1) != Retta:
            raise Exception("Per calcolare l'intersezione serve un altra retta")

        if retta1.b == 0:
            raise ZeroDivisionError

        if -self.__a / self.__b == -retta1.a / retta1.b and -self.__c / self.__b != -retta1.c / retta1.b:
            return None

        if -self.__a / self.__b == -retta1.a / retta1.b and -self.__c / self.__b == -retta1.c / retta1.b:
            return self

        x = ((self.__c / self.__b) - (retta1.c / retta1.b)) / ((-self.__a / self.__b) + (retta1.a / retta1.b))
        y = (-self.__a / self.__b) * x + (-self.__c / self.__b)
        return round(x, 2), round(y, 2)


#si crea la classe button per i bottoni utilizzati nel menu di gioco 
class Button():
    #, text_input, font, base_color, hovering_color
    def __init__(self, immagine, pos):
        self.immagine = immagine
        self.__x_pos = pos[0]
        self.__y_pos = pos[1]
        #self.font = font
        #self.base_color, self.hovering_color = base_color, hovering_color
        #self.text_input = text_input
        #self.text = self.font.render(self.text_input, True, self.base_color)
        #if self.immagine == None:
        #    self.immagine = self.text
        self.rect = self.immagine.get_rect(center= (self.__x_pos, self.__y_pos))
        #self.text_rect = self.text.get_rect(center= (self.__x_pos, self.__y_pos))

    def update(self):
        SCHERMO.blit(self.immagine, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False




#chiedere gruppo di italiano

#indirizzo il percorso alla cartella dove sono presenti le immagini
os.chdir(os.getcwd()+"/Throught_the_Hallway/images")

#avvio le librerie
pygame.init()
random.seed()
#93.145.175.242-63213
#10.255.237.221-6379
r = redis.StrictRedis(host="93.145.175.242", port=63213,password='1357642rVi0', db=0)
#r.delete()
##definisco i gruppi di sprites##
all_powerup = pygame.sprite.Group()#gli sprite dei powerups
all_help_scudo = pygame.sprite.Group()
all_help_drone = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()#gli sprite dei proiettili amici
all_sprites2 = pygame.sprite.Group()#gli sprite dei proiettili del drone
all_enemies1 = pygame.sprite.Group()#gli sprite dei nemici
all_enemies2 = pygame.sprite.Group()#gli sprite dei nemici 2
proiettili_all_enemies = pygame.sprite.Group()#gli sprite dei proiettili nemici
personaggio = pygame.sprite.Group()#lo sprite del personaggio
uccello = pygame.sprite.Sprite(personaggio)#assegno lo sprite al gruppo
all_spada = pygame.sprite.Group()


##ricavo le immagini necessarie##

def image_load():
    global sfondo_iniziale1, play_notpressed, play_pressed, sfondo, base, game_over 
    global vita50, vita100, vita75, vita25, palla_di_neve, drone, scudo, play_button
    global spr_drone, spr_scudo, options_notpressed, options_pressed, sfondo_prova

    sfondo_iniziale1 = pygame.image.load("Sfondo_iniziale.png")
    play_notpressed = pygame.image.load("Tasto_Play_1.png")
    play_pressed = pygame.image.load("Tasto_Play_2.png")
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
    play_button = pygame.image.load("play_button.png")
    options_notpressed = pygame.image.load("Tasto_Menu_1.png")
    options_pressed = pygame.image.load("Tasto_Menu_2.png")
    sfondo_prova = pygame.image.load("sfondo_luna.png")

    uccello.image = pygame.image.load("Protagonista con Jetpack.png") #assegno l'immagine in questo modo poichè il personaggio è sottoforma di sprite
    uccello.rect = uccello.image.get_rect()
    uccello.rect.update(50,0,50,187)

    spr_scudo = pygame.sprite.Sprite(all_help_scudo)
    spr_scudo.image = pygame.image.load("scudoamico.png")
    spr_scudo.rect = spr_scudo.image.get_rect()
    spr_scudo.rect.update(0,0,300,300)


    spr_drone = pygame.sprite.Sprite(all_help_drone)
    spr_drone.image = pygame.image.load("DroneAmico.png")
    spr_drone.rect = spr_drone.image.get_rect()
    spr_drone.rect.center = (100, 300)


image_load()





#Costanti globali
SCHERMO = pygame.display.set_mode((1400,800))
FPS = 180
VEL_AVANZ = 12




def inizializza():
    ##creo/inizializzo quasi tutte le variabili che andrò ad usare nel codice 
    ## questa funzione serve anche a resettare tutte le variabili una volta restartato il gioco

    ##le rendo sempre accessibili##
    # - global power-up
    global power_up, shuffle_pu, powerup_dict, n_M, all_powerup, allpowerup, spawn, type_powerup, timerdrone, timerpalladineve, timerscudo, timerdrone_, timerpalladineve_, timerscudo_, droppalladineve, dropdrone, dropscudo, scudo, n_P_drone, proiettili_dict_drone,l
    # - global uccello
    global uccellox, spiay, proiettili_dict, salto, gravity, n_salti, counter_salti, dimensioni
    # - global sfondo
    global basex, sfondox
    # - global nemici 
    global  nemico, allenemies2, nemici_dict, n_N, all_enemies1, nemici_life, n_K, all_enemies2, nemici2_dict, nemici2_life
    # - global orologi
    global clock_nemici1, clock_jetpack, orologio_j,tempo, tempo_spawn1, clk_spawn_pu, tempo_spawn2, clock_nemici2, clock_spada, orologio_s
    # - global proiettili nemici
    global nemici_proiettili_dict, nemici_allsprites, nemici_firerate, sparo_nemici, proiettili_all_enemies, nemici_n_proiettile
    # - global proiettili amici
    global n_P, all_sprites, all_sprites2, allsprites, allsprites2

    global surf_text, fnt, past

    global spada_dict, allspada, n_S

    l=0
    spiay = 500 #posizione personaggio ad inizio gioco
    basex = 0
    sfondox = 0
    proiettili_dict = {}
    proiettili_dict_drone = {}
    nemici_proiettili_dict = {}
    nemici_dict = {}
    nemici_life = {}
    nemici2_dict = {}
    nemici2_life = {}
    nemico = False
    salto = False
    allsprites= "vuoto"
    allsprites2= "vuoto"
    nemici_allsprites = "vuoto"
    allenemies2= "vuoto"
    all_sprites.empty()
    all_sprites2.empty()
    all_enemies1.empty()
    all_enemies2.empty()
    proiettili_all_enemies.empty()
    nemici_proiettili_dict.clear()
    nemici_dict.clear()
    nemici_life.clear()
    proiettili_dict.clear()
    nemici2_life.clear()
    spada_dict = {}
    allspada = "vuoto"
    all_spada.empty()
    
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
    clock_spada = 0
    orologio_s = False
    
    ##NOMI DICT##
    ##utilizzo delle variabili per dare un nome agli elementi da inserire nei dizionari
    n_P= 0 #nome proiettile
    n_P_drone = 0 #nome proiettile drone
    n_N= 0 #nome nemico 
    n_M = 0 #nome power-up
    n_K = 0 #nome nemici 2
    n_S = 0

    gravity=0 #la velocità con cui il personaggio cade inizialmente
    sparo_nemici = False #quando diventa True (tramite "nemici_firerate") i nemici sparano
    nemici_n_proiettile= 0
    n_list = 0
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
    


play_button = Button(immagine=play_notpressed, pos=(700, 343)) 

options_button = Button(immagine=options_notpressed, pos=(700, 243))

 
    
    

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
#200
#9000
def disegna_oggetti():
    SCHERMO.blit(sfondo, (sfondox,-80))
    SCHERMO.blit(base, (basex,200))
    
    uccello.rect.topright = ( 200 , spiay)
    personaggio.draw(SCHERMO)

    surf_text = fnt.render(str(tempo), True, (255, 255, 0), None)
    SCHERMO.blit(surf_text, (1310, 10))

    #powerups
    if dropdrone == True:
        all_help_drone.draw(SCHERMO)
    else:
        pass

    if dropscudo == True:
        all_help_scudo.draw(SCHERMO)
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
        spr_scudo.rect.topright = (300, spiay-100)
    elif scudo == False:
        spr_scudo.remove


    if allsprites == "vuoto":
        all_sprites.empty()
        pass
    else:
        all_sprites.draw(SCHERMO)

    if allsprites2== "vuoto":
        all_sprites2.empty()
        pass
    else:
        all_sprites2.draw(SCHERMO)

    #icone powerups
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

    if allspada == "vuoto":
        all_spada.empty()
        pass
    else:
        all_spada.draw(SCHERMO)

    
    all_enemies1.draw(SCHERMO)
    all_enemies2.draw(SCHERMO)


def sconfitta():
    pygame.mixer.music.load("sus.mp3")
    pygame.mixer.music.play(1, 0)
    
    SCHERMO.blit(sfondo_iniziale1, (0,0))
    n_partita = time.asctime( time.localtime(time.time()) )
    fnt_classifica = pygame.font.SysFont("Times New Roman", 20)
    r.zadd(players, {(str(n_partita)): tempo})
    scritta_punteggio = "total score: "+str(tempo)
    
    print("\ntutte le partite:")
    partita = r.zrange(players, 0, -1, withscores=True)
    print(partita)

    punteggio_migliore=partita[len(partita)-1][1]
    scritta_punteggio_migliore = "punteggio migliore personale:"+str(punteggio_migliore)
    
    globale = "Classifica Globale"
 
    r.zadd(globale, {(str(players)): punteggio_migliore})

    classifica_globale = r.zrange(globale, 0, -1, desc=True, withscores=True)
    u = 0
    surf_text_globale_title = fnt_classifica.render("classifica globale:", True, (0, 0, 0), (121, 85, 62))
    SCHERMO.blit(surf_text_globale_title, (620, 510))

    if len(classifica_globale) <= 10:
        for i in range(0,len(classifica_globale)):
            scritta_classifica = str(i+1)+"° "+ str(classifica_globale[i])
            surf_text_globale = fnt_classifica.render(scritta_classifica, True, (0, 0, 0), (121, 85, 62))
            u += 20
            SCHERMO.blit(surf_text_globale, (600, (520+u)))
    else:
        for i in range(0,10):
            scritta_classifica = str(i+1)+"° "+ str(classifica_globale[i])
            surf_text_globale = fnt_classifica.render(scritta_classifica, True, (0, 0, 0), (255, 111, 67))
            u += 20
            SCHERMO.blit(surf_text_globale, (600, (520+u)))
    




    surf_text = fnt.render(scritta_punteggio, True, (0, 0, 0), (189, 189, 189))
    surf_text_migliore = fnt.render(scritta_punteggio_migliore, True, (0, 0, 0), (128, 222, 234))
    surf_text_title = fnt.render("Through The Hallway", True, (0, 0, 0), (128, 222, 234))
    surf_text_perso = fnt.render("HAI PERSO", True, (0, 0, 0))
    print("\n\n\n",r.keys())
    SCHERMO.blit(surf_text, (580, 270))
    SCHERMO.blit(surf_text_migliore, (430, 370))
    SCHERMO.blit(surf_text_title, (0,0))
    SCHERMO.blit(surf_text_perso, (600, 100))





    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                inizializza()
                ricominciamo = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                start()
                inizializza()
                ricominciamo = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()



    

    
#inizializzo Variabili
### Ciclo Principale ###
def start():
    global ricominciamo, fnt, players

    
    font = pygame.font.Font(None, 32)
    smaller_font = pygame.font.Font(None, 20)
    input_box = pygame.Rect(100, 200, 140, 32)
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = " "
    inserisci_username_title = font.render("inserisci username:", True, pygame.Color('gray27'))
    inserisci_username_subtitle = smaller_font.render("", True, pygame.Color('gray27'))
    error_username_subtitle = smaller_font.render("", True, pygame.Color('gray27'))


    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if play_button.checkForInput(event.pos):
                    if text == " ":
                        error_username_subtitle = smaller_font.render("inserisci prima l'username", True, pygame.Color('gray27'))
                        
                    else:
                        SCHERMO.blit(play_pressed, (613, 293))
                        username=("TTH_"+text)
                        players = username
                        inizializza()
                        aggiorna()
                        disegna_oggetti()
                        ricominciamo = True
                
                        
                    

                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    text = ""
                    active = not active
                else:
                    username=("TTH_"+text)
                    if r.exists(username) == 1:
                        inserisci_username_subtitle = smaller_font.render("utente già registrato", True, pygame.Color('gray50'))
                    else:
                        inserisci_username_subtitle = smaller_font.render("nuovo utente", True, pygame.Color('gray50'))
                    
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive

                if options_button.checkForInput(event.pos):
                    SCHERMO.blit(options_pressed, (612, 207))
                    aggiorna()
                    SCHERMO.fill((30, 30, 30))
                    torna_menu_title = font.render('premi "m" per tornare al menù', True, pygame.Color('gray50'))
                    SCHERMO.blit(torna_menu_title, (540, 500))
                    aggiorna()
                    ricominciamo1 = False 
                    while not ricominciamo1:    
  
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                pygame.quit()
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                                ricominciamo1 = True
            
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        username=("TTH_"+text)
                        if r.exists(username) == 1:
                            inserisci_username_subtitle = smaller_font.render("utente già registrato", True, pygame.Color('gray50'))
                            color = pygame.Color("yellow")
                        else:
                            inserisci_username_subtitle = smaller_font.render("nuovo utente", True, pygame.Color('gray50'))
                            color = pygame.Color("green")

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    else:
                        text += event.unicode


            if event.type == pygame.QUIT:
                pygame.quit()
        
        

        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        #text.
        SCHERMO.blit(sfondo_iniziale1, (0, 0))
        play_button.update()
        options_button.update()
        SCHERMO.blit(txt_surface, (input_box.x+5, input_box.y+5))
        SCHERMO.blit(inserisci_username_title, (input_box.x, input_box.y-25))
        SCHERMO.blit(inserisci_username_subtitle, (input_box.x, input_box.y+40))
        SCHERMO.blit(error_username_subtitle, (617, 400))

        #input_box
        pygame.draw.rect(SCHERMO, color, input_box, 2)

        pygame.display.flip()
        

            


start()


if ricominciamo == True:
    while True:
        basex -= VEL_AVANZ
        sfondox -= VEL_AVANZ
        if sfondox < -11200: sfondox = 0
        if basex < -2100: basex = 0



        keys=pygame.key.get_pressed()


        if spiay == 530:
            spiay = 530
        elif spiay < 530: 
            spiay += gravity
            gravity = 14


        if spiay > 528:
            n_salti = 0




        if keys[K_ESCAPE]:
            pygame.quit()


        if keys[K_j]:
    
            if clock_jetpack < 3:
                orologio_j = True
                if spiay == 0:
                    spiay = 0
                if spiay > 0:
                    gravity =-5
                    spiay += gravity




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
            spr_enemies.rect.topright= (SCHERMO.get_width()-30, random.randrange(340, 620))

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
                    spr_proiettile.rect.topright = (nemici_dict[b].rect.x, nemici_dict[b].rect.y + 37)

                    nemici_proiettili_dict.update({nemici_n_proiettile: spr_proiettile})
                    nemici_firerate = 0
                    sparo_nemici = False

        if counter_salti == True:
            if n_salti == 0:          
                dimensioni = spiay-190
            if n_salti == 1:          
                dimensioni = spiay-120
            n_salti +=1
            salto = True

            counter_salti = False

        if salto == True:
            if spiay > dimensioni:
                gravity = -15
                spiay += gravity
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
                spr_proiettile.rect.topright = (250, spiay+65)
                proiettili_dict.update({n_P: spr_proiettile})

            if dropdrone == True:
                if event.type == pygame.USEREVENT:
                    pygame.mixer.music.load("sparo.mp3")
                    pygame.mixer.music.play(1, 0)
                    n_P_drone += 1
                    spr_proiettile_drone = pygame.sprite.Sprite(all_sprites2)
                    spr_proiettile_drone.image = pygame.image.load("proiettile.png")
                    spr_proiettile_drone.rect = spr_proiettile_drone.image.get_rect()

                    spr_proiettile_drone.rect.topright = (spr_drone.rect.x, spr_drone.rect.y)
                    proiettili_dict_drone.update({n_P_drone: spr_proiettile_drone})



            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    inizializza()
        
            if event.type == pygame.QUIT:
                    pygame.quit()

            if event.type == pygame.USEREVENT:
                x1, y1 = float(spr_drone.rect.centerx), float(spr_drone.rect.centery)
                x2, y2 = (1300), (random.randrange(0, 160))
                retta = Retta("PUNTI", (x1, y1), (x2, y2))
                linea = retta.punti(100,2000) 
                clk_spawn_pu += 1
                tempo += 1
                clock_nemici1 += 1
                nemici_firerate += 1
                clock_nemici2 += 1
                if orologio_s == True:
                    clock_spada += 1
                    if clock_spada == 10:
                        clock_spada = 0
                        orologio_s = False
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

            #if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                
                #orologio_s = True

            #    n_S += 1
             #   spr_spada = pygame.sprite.Sprite(all_spada)
              #  spr_spada.image = pygame.image.load("spada_prova.png")
               # spr_spada.rect = spr_spada.image.get_rect()

                #spr_spada.rect.topright = (450, spiay-100)
                #spada_dict.update({n_S : spr_spada})

        
    
        for i in proiettili_dict:
 
            proiettile_attivo = proiettili_dict[i]                    

            if proiettile_attivo.rect.x < SCHERMO.get_width()-10:
                allsprites = "pieno"
                proiettile_attivo.rect.x += 30
                    
            else:
                allsprites = "vuoto"
        
        if dropdrone == True:

            for d in proiettili_dict_drone:
        
                proiettile_attivo_drone = proiettili_dict_drone[d]
                if proiettile_attivo_drone.rect.x < SCHERMO.get_width()-10:
                    allsprites2 = "pieno"
                    lineax = linea[0][0]
                    lineay= linea[0][1]
                    proiettile_attivo_drone.rect.centerx = lineax
                    proiettile_attivo_drone.rect.centery = lineay
                    linea.remove(linea[0])
                    
                    
                else:
                    l = 0
                    allsprites2 = "vuoto"


        


        for a in nemici_dict:

            nemico_attivo = nemici_dict[a]
       
            if nemico_attivo.alive()== True:
                nemico_attivo = nemici_dict[a]
                #x2, y2 = float(nemico_attivo.rect.centerx), float(nemico_attivo.rect.centery)
                if pygame.sprite.spritecollide(nemico_attivo, all_sprites, True):
                    if nemici_life:
                        nemici_life[a] -= 2
                        if nemici_life[a] == 0:
                            nemico_attivo.kill()
                            nemici_life.pop(a)

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
            




        #for c in spada_dict:
         #   spada_attivo = spada_dict[c]
            
            
          #  if pygame.sprite.spritecollide(nemico2_attivo, all_spada, True):
           #     nemico2_attivo.kill()

            #else:
             #   pass

            #if spada_attivo.rect.y < SCHERMO():
             #   allspada = "pieno"
              #  spada_attivo.rect.y += 10
            #else:
             #   allspada = "vuoto"
              #  spada_attivo.kill()

        if timerdrone_ == 1:
            dropdrone = True

        if timerdrone_ == 10:
            dropdrone = False
            timerdrone = False
            timerdrone_ = 0

       
        
        if timerscudo == 1:
            dropscudo = True
            scudo = True
        if timerscudo_ == 10:
            scudo = False
            dropscudo = False 
            timerscudo = False
            timerscudo_ = 0

        if clk_spawn_pu== 30:
            clk_spawn_pu = 0
            n_M += 1
            spr_powerup = pygame.sprite.Sprite(all_powerup)

            
            u = int(random.randrange(1,3))
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
                powerup_attivo.rect.x -= 10                
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

                
                #if scudo == True and pygame.sprite.spritecollide(spr_scudo, all_enemies2, True):
                #    pass

                if pygame.sprite.spritecollide(uccello, proiettili_all_enemies, True) or pygame.sprite.spritecollide(uccello, all_enemies2, True):
                    nemici_proiettile_attivo.rect.x = 0
                    sconfitta()
                

                else:
                    pass

        
                    
    


        aggiorna()
        disegna_oggetti()
        