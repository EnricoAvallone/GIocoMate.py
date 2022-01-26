class parabola:
    
    def __init__(self, p1 = None, p2 = None, p3 = None):
        
        self.__a = float(p1)
        self.__b = float(p2)
        self.__c = float(p3)
    
    def esplicita(self):
        if self.__b == 0:
            return f"\nl'equazione in forma esplicita è:\n y = {self.__a}x^2 + {self.__c}"
        elif self.__c == 0:
            return f"\nl'equazione in forma esplicita è:\n y = {self.__a}x^2 + {self.__b}x "
        else:
            return f"\nl'equazione in forma esplicita è:\n y = {self.__a}x^2 + {self.__b}x + {self.__c}"

    def cordinateV(self):
        Xv = 0
        Yv = 0
        if self.__b == 0:
            Xv = 0
        else:
            Xv = - (self.__b / (self.__a*2))
        delta = (self.__b * self.__b) - (4 * self.__c * self.__a)
        cord_V = (Xv, Yv)
        print("\nl'output di questa funzione è una tupla contenente le cordinate del vertice")
        return cord_V

    def cordinateF(self):
        Xf = 0
        Yf = 0
        if self.__b == 0:
            Xf = 0
        else:
            Xf = - (self.__b / (self.__a*2))
        delta = (self.__b * self.__b) - (4 * self.__c * self.__a)
        Yf = (1 - delta) / (4 * self.__a)
        cord_F = (Xf, Yf)
        print("\nl'output di questa funzione è una tupla contenente le cordinate del fuoco")
        return cord_F

    def eqdirettrice(self):
        diret = - (1 + (self.__b * self.__b + (- 4) * self.__c * self.__a)) / (4 * self.__a)
        print("\nl'output di questa funzione è una variabile contenente il termine noto della direttrice")
        return diret

valori_a_b_c = parabola(input("\ninresisci il valore di a: "), input("inresisci il valore di b: "), input("inresisci il valore di c: "))

print(valori_a_b_c.esplicita())
print(valori_a_b_c.cordinateV())
print(valori_a_b_c.cordinateF())
print(valori_a_b_c.eqdirettrice())

print("Hello World")