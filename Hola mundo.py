'''Nombre del personaje'''

def comprueba(primero, segundo):
    if primero.upper() == segundo.upper():
        return True
    else:
        return False

n = input("¿Cómo se llama tu personaje?")

if comprueba("javi", n):
    n = "capullo"
    print("Ahh... con que eres un capullo.")
    c = input("¿Qué clase tienes, " + n + "? Guerrero, mago o pícaro")
else:
    print("Me gusta, ¿Es extranjero?")
    c = input("¿Qué clase tiene " + n + "? Guerrero, mago o picaro")

'''Clase del personaje y armas'''
if comprueba("MAGO", c):
    print("Eres una de esas ratas de biblioteca, ¿Verdad?")
    a = "el baculo"
    print("Si es así las armas que manejas son los baculos.")
elif c == "picaro" or c == "Picaro":
    print("Tranquilo, estaré pendiente de mi cartera a partir de ahora")
    a = "las dagas"
    print("Si es así las armas que manejas son las dagas.")
elif c == "guerrero" or c == "Guerrero":
    print("Uff, pero que musculos chaval.")
    print("Si es así puedes manejar el arma que quieras")
    a = input("¿Qué arma quieres manejar?")
else:
    print("¿Cómo que " + c + "? ¿Eso que mierda es? Eres un graciosillo por lo que veo. Pues tu clase será «retrasado»")
    c = "retrasado"
    print("Como eres un retrasado no puedes manejar ningún arma ¯\_( ㆆ u ㆆ )_/¯")
    print("Así que no puedes jugar, lo siento .|.( ㆆ u ㆆ )")

if c == "mago" or c == "Mago" or c == "picaro" or c == "Picaro" or c == "guerrero" or c == "Guerrero":
    l = input("¿Dónde naciste, " + n + "?")
    if l == "Avila" or l == "avila":
        print("Vaya mierdas estas hecho")
    elif l == "Sevilla" or l == "sevilla":
        print("Vaya puto amo")
    print ("Nuestro " + c + " " + n + " nació en " + l + " y desde pequeño se adiestro con " + a)
