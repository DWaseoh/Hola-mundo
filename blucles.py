'''el comando int es para que solo pueda recibir una variable numero entero'''
#n=int(input("Dame un numero, capullo:"))
n=100
'''el comando str sirve para que lea la variable como un numero'''
print(str(n) + " por " + "100 es igual a "+str(n*100))
'''para i en el rango (n) genera un bucle. i es 0 y suma 1 hasta terminar el rango'''
for i in range(n):
    print("-->" + str(i))
'''lo mismo pero en una lista'''
'''i es rojo, cuando termina vuelve y es verde'''

lis2t=["rojo","verde","amarillo"]

for i in lis2t:
#variable, i siempre es rojo
    i = "rojo"

    if i == "rojo":
        #print("comunista")
        break
    else:
        print(i)

#bucle, i es 0 y suma 1 hasta llegar a 99
for i in range(100):
    #si el resto de i/2 es 0 entonces es par
    if i%2 == 0:
        print(str(i)+" es par")
    #si no, es impar
    else:
        print(str(i)+"es impar")

d = 0
while d <= 100:
    print(str(d) + " es menor que 100")
    d = d+2

boo=True
while boo:
    c = input("Dime un número par")
    if (int(c)%2 != 0):
        boo = False

while True:
    print("Hola")
    break
