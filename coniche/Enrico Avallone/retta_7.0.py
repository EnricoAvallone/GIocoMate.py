class retta:
    
    def __init__(self, p1 = None, p2 = None, p3 = None):

        self.__a = float(p1)
        self.__b = float(p2)
        self.__c = float(p3)
        self.__punti = []

    def implicita(self):
        if self.__b == 0:
            return f"\nl'equazione in forma implicita è: \n {self.__a}x + {self.__c} = 0"
        elif self.__a == 0:
            return f"\nl'equazione in forma implicita è: \n {self.__b}y + {self.__c} = 0"
        elif self.__c == 0:
            return f"\nl'equazione in forma implicita è: \n {self.__a}x + {self.__b}y = 0"
        else:
            return f"\nl'equazione in forma implicita è: \n {self.__a}x + {self.__b}y + {self.__c} = 0"

    def esplicita(self):
        if self.__b == 0:
            return f"\nl'equazione non può essere scritta in forma esplicita"
        elif self.__a == 0:
            return f"\nl'equazione in forma esplicita è: \n y = {-self.__c  / self.__b}x"
        elif self.__c == 0:
            return f"\nl'equazione in forma esplicita è: \n y = {-self.__a  / self.__b}x" 
        else:
            return f"\nl'equazione in forma esplicita è: \n y = {-self.__a  / self.__b}x + {-self.__c / self.__b}"

    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def coefficiente_angolare(self):
        if self.__b == 0:
            return f"\nla retta è parallela all'asse delle Y \nil coefficiente angolare è non definito"
        else:
            m = -self.__a / self.__b
        print("\nl'output di questa funzione è il coefficiente angolare dell'equazione") 
        return m

    def y(self, x):
        self.__x = float(x)
        if self.__b == 0:
            return f"\nla retta è parallela all'asse delle Y"
        elif self.__a == 0:
            y = -self.__c / self.__b
            cord_punti = [self.__x, y]
        elif self.__c == 0:
            y = -self.__a * self.__x / self.__b
            cord_punti = [self.__x, y]
        else:
            y = -self.__a * self.__x / self.__b + (-self.__c / self.__b)
            cord_punti = (self.__x, y)
        print("\nl'output di questa funzione è una tupla contenente le coridnate di un punto che ha per x il valore della x inserito dall'utilizzatore del codice, ed ha per y il valore della y calcolato con la x")
        return cord_punti

    def punti(self, n):
        self.__n = int(n)
        x1 = 0
        if self.__b == 0:
            return f"\nnull"
        elif self.__a == 0:
            return f"\nnull"
        else:
            for i in range (self.__n):
                tupla = (x1, (-self.__a * x1) / self.__b + (-self.__c / self.__b))
                x1 = x1 + 1
                self.__punti.append(tupla)
            print("\nl'output di questa funzione è una tupla contenente le cordinate di tutti i punti della retta data")
            return self.__punti

    def punti_intersezione(self, a2, b2, c2):
        self.__a2 = float(a2)
        self.__b2 = float(b2)
        self.__c2 = float(c2)
        if (-self.__a / self.__b) == (-self.__a2 / self.__b2):
            if self.__c == self.__c2:
                return f"\nle due rette sono coincidenti {self.__punti}"
            else:
                return f"\nle due rette sono parallele e quindi non hanno punti in comune"
        elif self.__c == self.__c2:
            print("\nl'output di questa funzione è il punto di intersezione tra le due rette")
            return 0, self.__c
        else:
            print("\nl'output di questa funzione sono le cordinate del punto in cui le due equazioni si incontrano")
            return ((-self.__c / self.__b)+(self.__c2 / self.__b2))/((-self.__b / self.__a)+(self.__b2 / self.__a2)), ((-self.__b / self.__c)+(self.__b2 / self.__c2))/((-self.__b / self.__a)+(self.__b2 / self.__a2))


valori_a_b_c = retta(input("\ninresisci il valore di a: "), input("inresisci il valore di b: "), input("inresisci il valore di c: "))

print(valori_a_b_c.implicita())
print(valori_a_b_c.esplicita())
print(valori_a_b_c.coefficiente_angolare())
print(valori_a_b_c.y(input("\ninserisci il valore della x = ")))
print(valori_a_b_c.punti(input('\nfine range = ')))
print("\n--------------------------------------------------------------\nadesso inserisci i valori dei coefficienti della seconda retta")
print(valori_a_b_c.punti_intersezione(input("\ninresisci il valore di a2: "), input("inresisci il valore di b2: "), input("inresisci il valore di c2: ")))