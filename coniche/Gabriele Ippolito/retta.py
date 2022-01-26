class retta:
    def __init__(self, tipo = None, p1 = None, p2 = None, p3 = None, p4 = None):
        #capisco che dati mi sono stati forniti li converto in float e ricavo a, b, c ed m

        if(tipo == "input_abc"):
            #p1=a p2=b p3=c
            self.__a = float(p1)
            self.__b = float(p2)
            self.__c = float(p3)
            self.__punti = []
            self.__m = -float(p1) / float(p2)

        elif(tipo == "input_2punti"):
            #p1=x1 p2=y1 p3=x2 p4=y2
            self.__a = float(p4) - float(p2)
            self.__b = - (float(p3) - float(p1))
            self.__c = - float(p1) * (float(p4)-float(2)) + float(p2) * (float(p3) - float(p1))
            self.__punti = []
            self.__m = (float(p4) - float(p2))/(float(p3)-float(p1))
               
        elif(tipo == "input_coefficiente"):
            #p1=coefficiente p2=x p3=y
            self.__a = -float(p1)
            self.__b = 1
            self.__c = float(p1) * float(p2) - float(p3)
            self.__punti = []
            self.__m = float(p1)
 
    def getA(self):
        #restituisce il valore di a (float) calcolato in precedenza
        return self.__a

    def getB(self):
        #restituisce il valore di b (float) calcolato in precedenza
        return self.__b
    
    def getC(self):
        #restituisce il valore di c (float) calcolato in precedenza
        return self.__c

    def eqEsplicita(self):
        #restituisce sotto forma di stringa l'equazione in forma esplicita
        if self.__b == 0:
            return f"\n\n equazione forma esplicita: \n x = {- self.__c/ self.__a} \n (y= 0) \n\n ---------------------------"
        elif self.__a == 0:
            return f"\n\n equazione forma esplicita: \n y = {- self.__c/ self.__b} \n (x= 0) \n\n ---------------------------"
        else:
            #risolvo con un if il problema del segno
            if - self.__c/ self.__b < 0:
                return f"\n\n equazione forma esplicita: \n y = {- self.__a / self.__b}x {- self.__c/ self.__b} \n\n ---------------------------"
            else:
                return f"\n\n equazione forma esplicita: \n y = {- self.__a / self.__b}x + {- self.__c/ self.__b} \n\n ---------------------------"

    def eqImplicita(self):
        if self.__b == 0:
            if self.__c < 0:    #risolvo con un if il problema del segno
                return f"---------------------------\n\n equazione forma implicita: \n {self.__a}x {self.__c} = 0 \n (y= 0) "
            else:
                return f"---------------------------\n\n equazione forma implicita: \n {self.__a}x + {self.__c} = 0 \n (y= 0) "

        elif self.__a == 0:
            if self.__c < 0:    #risolvo con un if il problema del segno
                return f"---------------------------\n\n equazione forma implicita: \n {self.__b}y {self.__c} = 0 \n (x= 0) "
            else:
                return f"---------------------------\n\n equazione forma implicita: \n {self.__b}y + {self.__c} = 0 \n (x= 0) "
        else:
            if self.__c < 0 and self.__b < 0:   #risolvo con un if il problema del segno
                return f"---------------------------\n\n equazione forma implicita: \n {self.__a}x {self.__b}y {self.__c} = 0 "
            elif self.__c <0:
                return f"---------------------------\n\n equazione forma implicita: \n {self.__a}x + {self.__b}y {self.__c} = 0 "
            elif self.__b <0:
                return f"---------------------------\n\n equazione forma implicita: \n {self.__a}x {self.__b}y + {self.__c} = 0 "
            else:
                return f"---------------------------\n\n equazione forma implicita: \n {self.__a}x + {self.__b}y + {self.__c} = 0 "

    def getY(self, x):
        #restituisce esclusivamente il valore di y (float) dove possibile
        if self.__b == 0:
            x = - self.__c/ self.__a
            y = 0
            return y
        elif self.__a == 0:
            y = - self.__c/ self.__b
            x= 0
            return y
        else:
            pass #y = (- self.__a / self.__b)x + (- self.__c/ self.__b) -- serve la x
             
    #ricavo e restituisco la lista dei punti in base a quanti ne sono stati richiesti
    def punti(self):
        #scelgo un range che prenda sia numeri negativi che positivi (50%/50%)
        inizio = - (1/2) * int(n)
        fine = (1/2) * int(n)

        if self.__a == 0:
            for i in range(int(inizio), int(fine)):
                x = i
            self.__punti.append((x, - self.__c/ self.__b))
        
        elif self.__b == 0:
            for i in range(int(inizio), int(fine)):
                y = i
            self.__punti.append((- self.__c/ self.__a, y))

        else:    
            for i in range(int(inizio), int(fine)):
                x = i
                self.__punti.append ((x, (- self.__a * x - self.__c) / self.__b))
        
        return self.__punti

    def getM(self):
        #restituisce il valore del coefficiente angolare (float)
        if self.__b == 0:
            return False #la retta è parallela all'asse delle y, il coefficiente angolare non è definito in alcun modo
        else:
            return self.__m

    
    def intersezione(self, s):#prendo le due rette

        #trovo l'intersezione tra le due liste di punti
        a = s.punti()
        b = self.punti()
        c = list(set(a).intersection(b))
        return c




#creo un dizionario dove saranno inserite tutte le rette create in modo tale da poterle usare in più momenti
rette_dict = {}

while True:
    #punto di inizio e di ritorno: si può decidere se creare una nuova retta, se analizzare una retta creata o se trovare l'intersezione tra due rette create
    menù = int(input("\n\n\n-Premi 1 per creare una nuova retta\n-Premi 2 per utilizzare una retta già esistente\n-Premi 3 per trovare l'intersezioni tra due rette\n\n-->"))

    while True:

        if menù == 1: #è stato scelto di creare una nuova retta

            tipo_valori = int(input("\n\nche tipi di valore stai dando? \n\n1) a, b, c\n2) due punti appartenenti alla retta\n3) coefficiente angolare ed un punto appartenente alla retta \n\ndigitare 1, 2 o 3 a seconda della risposta..."))
            #chiedo che tipi di valore si danno per dire poi al codice che tipo di calcoli deve fare 

            if tipo_valori == 1: #i valori che si danno sono a, b e c

                tipo_retta = "input_abc"

                nome_retta = (input("\n\ncome vuoi chiamare la tua nuova retta\n -->"))
                nome_retta0 = (nome_retta, "0")
                nome_retta1 = (nome_retta, "1")
                nome_retta2 = (nome_retta, "2")

                valore_retta = float(input("\n\ninserire valore a..."))
                valore_retta1 = float(input("\ninserire valore b..."))
                valore_retta2 = float(input("\ninserire valore c..."))
                
                #inserisco i dati nel dizionario identificandoli con il nome dato alla retta
                rette_dict.update({nome_retta0: tipo_retta})
                rette_dict.update({nome_retta: valore_retta})
                rette_dict.update({nome_retta1: valore_retta1})
                rette_dict.update({nome_retta2: valore_retta2})

                
            elif tipo_valori == 2: #i valori che si danno sono le coordinate di due punti
                tipo_retta = "input_2punti"

                nome_retta = (input("\n\ncome vuoi chiamare la tua nuova retta\n -->"))
                nome_retta0 = (nome_retta, "0")
                nome_retta1 = (nome_retta, "1")
                nome_retta2 = (nome_retta, "2")
                nome_retta3= (nome_retta, "3")

                valore_retta = float(input("\n\ninserie x del primo punto..."))
                valore_retta1 = float(input("\ninserie y del primo punto..."))
                valore_retta2 = float(input("\ninserie x del secondo punto..."))
                valore_retta3 = float(input("\ninserire y del secondo punto..."))

                #inserisco i dati nel dizionario identificandoli con il nome dato alla retta
                rette_dict.update({nome_retta0: tipo_retta})
                rette_dict.update({nome_retta: valore_retta})
                rette_dict.update({nome_retta1: valore_retta1})
                rette_dict.update({nome_retta2: valore_retta2})
                rette_dict.update({nome_retta3: valore_retta3})

            

            elif tipo_valori == 3:
                tipo_retta = "input_coefficiente" # i valori che si danno sono le coordinatedi un punto ed il coefficiente angolare

                nome_retta = (input("\n\ncome vuoi chiamare la tua nuova retta\n -->"))
                nome_retta0 = (nome_retta, "0")
                nome_retta1 = (nome_retta, "1")
                nome_retta2 = (nome_retta, "2")

                valore_retta = float(input("\n\ninserie il valore del coefficiente angolare..."))
                valore_retta1 = float(input("\ninserie x del un punto..."))
                valore_retta2 = float(input("\ninserie y del un punto..."))

                #inserisco i dati nel dizionario identificandoli con il nome dato alla retta
                rette_dict.update({nome_retta0: tipo_retta})
                rette_dict.update({nome_retta: valore_retta})
                rette_dict.update({nome_retta1: valore_retta1})
                rette_dict.update({nome_retta2: valore_retta2})

           #dopo aver ricevuto i dati torno al punto di inizio 
            while True:
                scelta =input("\n\nla tua retta è stata creata correttamente \n digita 'm' per tornare al menù principale\n-->")
                if scelta == "m":
                    scelta = ""
                    break
                else: 
                    print("Errore")
            break
    
        elif menù == 2:#è stato scelto di ricavare le informazioni da una retta creata in precedenza
            
            #chiedo il nome della retta per richiamarla dal dizionario 
            nome_retta_attiva= str(input("\n\ndi quale retta vuoi ricavare le informazioni? \n inserisci il nome-->"))
            nome_retta_attiva1 = (nome_retta_attiva, "1")
            nome_retta_attiva2 = (nome_retta_attiva, "2")
            tipo_retta_attiva = (nome_retta_attiva, "0")

            n = (input("quante coppie di ordinate vuoi ricavare?..."))#chiedo quante coppie di coordinate si vogliono ricevere

            if rette_dict[tipo_retta_attiva] == "input_coefficiente":
                #se la tipologia di dati forniti per quanto riguarda la retta scelta sono le coordinate del coefficiente
                retta_attiva = retta(rette_dict[tipo_retta_attiva], rette_dict[nome_retta_attiva], rette_dict[nome_retta_attiva1], rette_dict[nome_retta_attiva2])
            
            if rette_dict[tipo_retta_attiva] == "input_2punti":
                #se la tipologia di dati forniti per quanto riguarda la retta scelta sono le coordinate di due punti
                nome_retta_attiva3 = (nome_retta_attiva, "3")#richiamo anche il 4 valore che nelle altre tipologie non è presente
                retta_attiva = retta(rette_dict[tipo_retta_attiva], rette_dict[nome_retta_attiva], rette_dict[nome_retta_attiva1], rette_dict[nome_retta_attiva2], rette_dict[nome_retta_attiva3])
            
            if rette_dict[tipo_retta_attiva] == "input_abc":
                #se la tipologia di dati forniti per quanto riguarda la retta scelta sono a, b e c
                retta_attiva = retta(rette_dict[tipo_retta_attiva], rette_dict[nome_retta_attiva], rette_dict[nome_retta_attiva1], rette_dict[nome_retta_attiva2])
            
            #restituisco tutte le informazioni ricavate attraverso il codice sulla retta scelta
            print(retta.eqImplicita(retta_attiva))

            print(retta.eqEsplicita(retta_attiva))

            print(" coefficiente angolare:\n\n m=",retta.getM(retta_attiva),"\n\n ---------------------------\n\n\n", sep="")

            print("lista punti:\n",retta.punti(retta_attiva), sep="")

            #dopo aver mostrato le info chiedo se si vuole tornare al menù principale dove si possono analizzare altre rette o crearne di nuove
            while True:
                scelta=input("\n\ndigita 'm' per tornare al menù principale\n-->")
                if scelta == "m":
                    scelta = ""
                    break
                else: 
                    print("Errore")
            break
        
        elif menù == 3:# è stato scelto di trovare l'intersezione tra due rette

            nome_retta_attiva = input("inserire il nome della prima retta\n-->")#chiedo qual'è la prima retta di cui si vuole ricavare l'intersezione
            nome_retta_attiva1 = (nome_retta_attiva, "1")
            nome_retta_attiva2 = (nome_retta_attiva, "2")
            tipo_retta_attiva = (nome_retta_attiva, "0")

            nome_intersezione = input("\ninserire il nome della seconda retta\n-->")#chiedo qual'è la seconda retta di cui si vuole ricavare l'intersezione
            nome_intersezione1 = (nome_intersezione, "1")
            nome_intersezione2 = (nome_intersezione, "2")
            tipo_intersezione = (nome_intersezione, "0")

            if rette_dict[tipo_retta_attiva] == "input_coefficiente":
                #se la tipologia di dati forniti per quanto riguarda la retta scelta sono le coordinate del coefficiente
                retta_attiva = retta(rette_dict[tipo_retta_attiva], rette_dict[nome_retta_attiva], rette_dict[nome_retta_attiva1], rette_dict[nome_retta_attiva2])
            
            if rette_dict[tipo_retta_attiva] == "input_2punti":
                #se la tipologia di dati forniti per quanto riguarda la retta scelta sono le coordinate di due punti
                nome_retta_attiva3 = (nome_retta_attiva, "3")#richiamo anche il 4 valore che nelle altre tipologie non è presente
                retta_attiva = retta(rette_dict[tipo_retta_attiva], rette_dict[nome_retta_attiva], rette_dict[nome_retta_attiva1], rette_dict[nome_retta_attiva2], rette_dict[nome_retta_attiva3])
            
            if rette_dict[tipo_retta_attiva] == "input_abc":
                #se la tipologia di dati forniti per quanto riguarda la retta scelta sono a, b e c
                retta_attiva = retta(rette_dict[tipo_retta_attiva], rette_dict[nome_retta_attiva], rette_dict[nome_retta_attiva1], rette_dict[nome_retta_attiva2])



            if rette_dict[tipo_intersezione] == "input_coefficiente":
                #se la tipologia di dati forniti per quanto riguarda la retta scelta sono le coordinate del coefficiente
                intersezione_attiva = retta(rette_dict[tipo_intersezione], rette_dict[nome_intersezione], rette_dict[nome_intersezione1], rette_dict[nome_intersezione2])
            
            if rette_dict[tipo_intersezione] == "input_2punti":
                #se la tipologia di dati forniti per quanto riguarda la retta scelta sono le coordinate di due punti
                nome_intersezione3 = (nome_intersezione, "3")#richiamo anche il 4 valore che nelle altre tipologie non è presente
                intersezione_attiva = retta(rette_dict[tipo_intersezione], rette_dict[nome_intersezione], rette_dict[nome_retta_attiva1], rette_dict[nome_intersezione2], rette_dict[nome_intersezione3])
            
            if rette_dict[tipo_intersezione] == "input_abc":
                #se la tipologia di dati forniti per quanto riguarda la retta scelta sono a, b e c
                intersezione_attiva = retta(rette_dict[tipo_intersezione], rette_dict[nome_intersezione], rette_dict[nome_intersezione1], rette_dict[nome_intersezione2])
            
            n = 20 #definisco la quantità di coppie di coordinate da mostrare nel caso le due rette fossero parallele
            
            print("\n\npunto di intersezione:  ",retta_attiva.intersezione(intersezione_attiva),"\n\n")

            #dopo aver mostrato le info chiedo se si vuole tornare al menù principale dove si possono analizzare altre rette o crearne di nuove
            while True:
                scelta=input("\n\ndigita 'm' per tornare al menù principale\n-->")
                if scelta == "m":
                    scelta = ""
                    break
                else: 
                    print("Errore")
            break

        else:
            print("Errore")
            break
        




            
