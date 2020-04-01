class Personaje():

    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        #super(Personaje, self).__init__()

    def getVida(self):
        return self.vida

    def hechizo(self):
        self.vida = self.vida / 2
        self.potencia = self.potencia / 3
        self.magia = self.magia * 2

    def info(self):
        print(self.nombre)

def combatir (ataque, defensa):
    vida = dani.vida
    zombie =1000000
    while vida > 0 or zombie > 0:
        el = input("Elige atacar o defender (a/d)>")
        if el == "a":
            print("Le quitas 20 al zombie")
            vida = dani.vida - 50
            print("El zombie te ha quitado 50, te quedan " + str(vida))
        elif el == "d":
            print("Te has defendido, te queda " +  str(vida))
        else:
            break


dani = Personaje
dani.nombre = input("Dime tu nombre: ")
dani.vida = 100

while True:
    i=input(dani.nombre + ">")
    if i == "avanza":
        print("Tu personaje avanza")
    elif i == "izquierda":
        print("Tu personaje se mueve a la izquierda")
    elif i == "salir":
        break
    elif i == "vida":
        v = dani.getVida(dani)
        print(str(v))
    elif i == "combatir":
        combatir(100, 20)