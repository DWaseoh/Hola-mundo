class Mago:
    def __init__(self, v, a, d):
        self.Vida = v
        self.Ataque = a
        self.Defensa = d
        self.VidaMaxima = 1000

    def recibirdano(self, ArmaAtaque):
        self.Vida = self.Vida - ArmaAtaque / self.Defensa
        return ArmaAtaque / self.Defensa

    def pocion(self, Consumible):
        if self.Vida + Consumible >= self.VidaMaxima:
            self.Vida = self.VidaMaxima
        else:
            self.Vida = self.Vida + Consumible


class Consumible:

    def __init__(self, dv,rv, cs):
        self.DarVida = dv
        self.ReducirVida = rv
        self.CutreSecreto = cs

class Arma:

    def __init__(self, a):
        self.Ataque = a

Gandalf = Mago(1000, 900, 700)
Espada = Arma(100000)
Pocion = Consumible (50, 0, 0)


while True:
    i = input("¿Qué quieres hacerle a Gandalf? (Atacar|Dar pocion|Dar pocion equivocada)")
    if i.title() == "Atacar":
        print ("Gandalf ha recibido "+str(int(Gandalf.recibirdano(Espada.Ataque))))
        print ("Gandalf ahora tiene "+str(int(Gandalf.Vida)))
    elif i.title() == "Dar Pocion":
        Gandalf.pocion(Pocion.DarVida)
        print ("Gandalf ha recuperado "+ str(int(Pocion.DarVida)))
        print ("Gandalf ahora tiene "+str(int(Gandalf.Vida)))
    elif i.title() == "Dar Pocion Equivocada":
        print ("Gandalf ha cambiado de sexo 0.o")
        print ("Estaras contento, acabas de morir, te ha matado por lo que hiciste")
        break

    if Gandalf.Vida < 0:
        print ("Vaya, lo has matado, bueno, no te preocupes, resucita en la segunda.")
        break