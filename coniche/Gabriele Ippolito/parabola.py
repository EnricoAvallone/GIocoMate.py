'''
PARABOLA
La classe parabola deve gestire un oggetto relativo alla rappresentazione e costruzione
di una parabola.
- Il costruttore dovrà tenere conto di tutte le possibilità di generazione di una parabola.
-- tramite parametri (a,b,c)
-- tramite fuoco e direttrice
-- rapporti con altri ogggetti (tangenza con rette, passaggio per punti ecc..)
'''

#devi ancora implementare l'eventualità di una parabola verticale e l'equazione a partire dal fuoco e della direttrice
from typing import Sized


while True:
    class parabola:
        def __init__(self, tipo = None, p1 = None, p2 = None, p3 = None, p4 = None):

            self.__dati = str(tipo)

            if tipo=="param":
                
                self.__a = round(float(p1), 2)
                self.__b = round(float(p2), 2)
                self.__c = round(float(p3), 2)
                self.__punti = []

                self.delta = float(self.__b * self.__b - 4 * self.__a * self.__c)

            elif tipo == "fuocoDiret":
                self.__xfuoco = round(float(p1), 2)
                self.__yfuoco = round(float(p2), 2)
                #da usare quando si implementa la parabola verticale self.__xdirettrice = p3
                self.__ydirettrice = round(float(p3), 2)
                valorea= round(float(), 2)
                valoreb= round(float(), 2)
                valorec= round(float(), 2)

                self.delta = float(valoreb * valoreb - 4 * valorea * valorec)
                pass
    


        def getA(self):
            if self.__dati=="param":
                return self.__a

            elif self.__dati=="fuocoDiret":
                self.valorea= 2 * (1 / (self.__xfuoco - self.__ydirettrice))
                return self.valorea

        def getB(self):
            if self.__dati=="param":
                return self.__b

            elif self.__dati=="fuocoDiret":
                self.valoreb = -1 * (self.__yfuoco * (2 * self.valorea))
                return self.valoreb
    
        def getC(self):
            if self.__dati=="param":
                return self.__c

            elif self.__dati=="fuocoDiret":
                self.valorec= (- 1 + self.valoreb * self.valoreb + 4 * self.__yfuoco)/4 * self.valorea
                return self.valorec



        def equazione(self):
            if tipo_valori == 1:
                if self.__a == 0:
                    pass
                
                elif self.__a > 0:
                    if self.__b < 0 and self.__c < 0:
                        return f"\nla parabola è rivolta verso l'alto \n\n equazione parabola:\n y = {self.__a}x^2 {self.__b}x {self.__c} "
                    elif self.__b < 0 and self.__c > 0:
                        return f"\nla parabola è rivolta verso l'alto \n\n equazione parabola:\n y = {self.__a}x^2 {self.__b}x + {self.__c} "
                    elif self.__c < 0 and self.__b > 0:
                        return f"\nla parabola è rivolta verso l'alto \n\n equazione parabola:\n y = {self.__a}x^2 + {self.__b}x {self.__c} "
                    else:
                        return f"\nla parabola è rivolta verso l'alto \n\n equazione parabola:\n y = {self.__a}x^2 + {self.__b}x + {self.__c} "
                
                elif self.__a < 0:
                    if self.__b < 0 and self.__c < 0:
                        return f"\nla parabola è rivolta verso il basso \n\n equazione parabola:\n y = {self.__a}x^2 {self.__b}x {self.__c} "
                    elif self.__b < 0 and self.__c > 0:
                        return f"\nla parabola è rivolta verso il basso \n\n equazione parabola:\n y = {self.__a}x^2 {self.__b}x + {self.__c} "
                    elif self.__c < 0 and self.__b > 0:
                        return f"\nla parabola è rivolta verso il basso \n\n equazione parabola:\n y = {self.__a}x^2 + {self.__b}x {self.__c} "
                    else:
                        return f"\nla parabola è rivolta verso il basso \n\n equazione parabola:\n y = {self.__a}x^2 + {self.__b}x + {self.__c} "
            
            elif tipo_valori == 2:
                if self.valorea == 0:
                    pass
                
                elif self.valorea > 0:
                    if self.valoreb < 0 and self.valorec < 0:
                        return f"\nla parabola è rivolta verso l'alto \n\n equazione parabola:\n y = {self.valorea}x^2 {self.valoreb}x {self.valorec} "
                    elif self.valoreb < 0 and self.valorec> 0:
                        return f"\nla parabola è rivolta verso l'alto \n\n equazione parabola:\n y = {self.valorea}x^2 {self.valoreb}x + {self.valorec} "
                    elif self.valorec < 0 and self.valoreb > 0:
                        return f"\nla parabola è rivolta verso l'alto \n\n equazione parabola:\n y = {self.valorea}x^2 + {self.valoreb}x {self.valorec} "
                    else:
                        return f"\nla parabola è rivolta verso l'alto \n\n equazione parabola:\n y = {self.valorea}x^2 + {self.valoreb}x + {self.valorec} "
                
                elif self.valorea < 0:
                    if self.valoreb < 0 and self.valorec < 0:
                        return f"\nla parabola è rivolta verso il basso \n\n equazione parabola:\n y = {self.valorea}x^2 {self.valoreb}x {self.valorec} "
                    elif self.valoreb < 0 and self.valorec > 0:
                        return f"\nla parabola è rivolta verso il basso \n\n equazione parabola:\n y = {self.valorea}x^2 {self.valoreb}x + {self.valorec} "
                    elif self.valorec < 0 and self.valoreb > 0:
                        return f"\nla parabola è rivolta verso il basso \n\n equazione parabola:\n y = {self.valorea}x^2 + {self.valoreb}x {self.valorec} "
                    else:
                        return f"\nla parabola è rivolta verso il basso \n\n equazione parabola:\n y = {self.valorea}x^2 + {self.valoreb}x + {self.valorec} "
                


        def fuoco(self):
            if tipo_valori == 1:
                return f" \n\n Fuoco:\n x= {- self.__b / 2 * self.__a}   y= {(1 - self.delta)/ 4 * self.__a}"
            elif tipo_valori == 2:
                return f" \n\n Fuoco:\n x= {self.__xfuoco}   y= {self.__yfuoco}"


        def direttrice(self):
            if tipo_valori == 1:
                return f"\n Direttrice: \n y= {- (1 + self.delta)/ 4 * self.__a}\n"
            elif tipo_valori == 2:
                return f"\n Direttrice: \n y= {self.__ydirettrice}\n"


        def vertice(self):
            if tipo_valori == 1:
                return f"\n Vertice: \n x = {- self.__b / 2 * self.__a}; y = {- self.delta / 4 * self.__a}\n"
            elif tipo_valori == 2:
                return f"\n Vertice: \n x = {- self.valoreb / 2 * self.valorea}; y = {- self.delta / 4 * self.valorea}\n"


        




        

    tipo_valori = int(input("\n\nche tipi di valore stai dando? \n\n1) a, b, c\n2) coordinate del fuoco e della direttrice \n\ndigitare 1 o 2 a seconda della risposta..."))

    if tipo_valori == 1:
        parabola1 = parabola("param", input("\ninserire valore a..."), input("inserire valore b..."), input("inserire valore c..."))

    elif tipo_valori == 2:
        parabola1 = parabola("fuocoDiret", input("inserie x del fuoco..."), input("inserie y del fuoco..."), input("inserie y della direttrice..."))  

    parabola.getA(parabola1)
    parabola.getB(parabola1)
    parabola.getC(parabola1)

    print(parabola.equazione(parabola1))
    print(parabola.fuoco(parabola1))
    print(parabola.direttrice(parabola1))
    print(parabola.vertice(parabola1))
    ricomincia = input("digita si se vuoi ricominciare...")

    if ricomincia == "si":
        pass
    else:
        break
