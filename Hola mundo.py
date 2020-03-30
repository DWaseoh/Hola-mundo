n=input("¿Cómo se llama tu personaje?")

'''aqui invoco la variable c2'''
c2=input("Qué clase tiene "+n+"? Guerrero, mago o pícaro")

if c2 == "sacerdote":
    print("Bendigame por favor")
elif c2 == "picaro":
    print("Te gusta robar eh?")
elif c2 == "guerrero" or  n == "dani":
        print("Te gusta ir al gym, verdad?")
        print("MENTIROSO")
else:
    print("No te he dicho eso")

a=input("Qué armas maneja "+n+"?")

l=input("Dónde nació "+n+"?")

print("Nuestro "+c2+" "+n+" nació en "+l+" y desde pequeño se adiestro con "+a)

print("Entonces "+n+" murió estrepitosamente")