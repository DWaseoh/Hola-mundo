import pygame
import random
pygame.init()

win = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("First Game")

#Vida
xvida = random.randrange(10, 995)
yvida = random.randrange(10, 995)

#Enemigo
xmalo = random.randrange(10, 995)
ymalo = random.randrange(10, 995)

#Vida1
xvida1 = random.randrange(10, 995)
yvida1 = random.randrange(10, 995)

#Enemigo1
xmalo1 = random.randrange(10, 995)
ymalo1 = random.randrange(10, 995)

#Vida2
xvida2 = random.randrange(10, 995)
yvida2 = random.randrange(10, 995)

#Enemigo2
xmalo2 = random.randrange(10, 995)
ymalo2 = random.randrange(10, 995)

#Jugador
x = 50
y = 50
radio = 10
vel = 5
score = 0

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#Para el movimiento por la ventana
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    elif keys[pygame.K_LEFT] and x == vel:
        x = 1000
    if keys[pygame.K_RIGHT] and x < 1000 - vel:
        x += vel
    elif keys[pygame.K_RIGHT] and x == 1000 - vel:
        x = 0
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    elif keys[pygame.K_UP] and y == vel:
        y = 1000
    if keys[pygame.K_DOWN] and y < 1000 - vel:
        y += vel
    elif keys[pygame.K_DOWN] and y == 1000 - vel:
        y = 0

    #vida y malo 0
    if (xvida > x + radio/-1.5 and xvida < x + radio/1.5) and (yvida > y + radio/-1.5 and yvida < y + radio/1.5):
        radio += 5
        score = score + 5
        xmalo = random.randrange(10, 995)
        ymalo = random.randrange(10, 995)
        xvida = random.randrange(10, 995)
        yvida = random.randrange(10, 995)
    if xvida > 1000-vel:
        xvida = 10
    elif xvida < vel:
        xvida = 995
    if yvida > 1000-vel:
        yvida = 10
    elif yvida < vel:
        yvida = 995

    if (xmalo > x + radio/-2 and xmalo < x + radio/2) and (ymalo > y + radio/-2 and ymalo < y + radio/2):
        radio -= 5
        score = score - 1
        xmalo = random.randrange(10, 995)
        ymalo = random.randrange(10, 995)
        xvida = random.randrange(10, 995)
        yvida = random.randrange(10, 995)
    if xmalo > 1000-vel:
        xmalo = 10
    elif xmalo < vel:
        xmalo = 995
    if ymalo > 1000-vel:
        ymalo = 10
    elif ymalo < vel:
        ymalo = 995
#vida y malo 1
    if (xvida1 > x + radio/-1.5 and xvida1 < x + radio/1.5) and (yvida1 > y + radio/-1.5 and yvida1 < y + radio/1.5):
        radio += 5
        score = score + 5
        xmalo1 = random.randrange(10, 995)
        ymalo1 = random.randrange(10, 995)
        xvida1 = random.randrange(10, 995)
        yvida1 = random.randrange(10, 995)
    if xvida1 > 1000-vel:
        xvida1 = 10
    elif xvida1 < vel:
        xvida1 = 995
    if yvida1 > 1000-vel:
        yvida1 = 10
    elif yvida1 < vel:
        yvida1 = 995

    if (xmalo1 > x + radio/-2 and xmalo1 < x + radio/2) and (ymalo1 > y + radio/-2 and ymalo1 < y + radio/2):
        radio -= 5
        score = score - 1
        xmalo1 = random.randrange(10, 995)
        ymalo1 = random.randrange(10, 995)
        xvida1 = random.randrange(10, 995)
        yvida1 = random.randrange(10, 995)
    if xmalo1 > 1000-vel:
        xmalo1 = 10
    elif xmalo1 < vel:
        xmalo1 = 995
    if ymalo1 > 1000-vel:
        ymalo1 = 10
    elif ymalo1 < vel:
        ymalo1 = 995
#vida y malo 2
    if (xvida2 > x + radio/-1.5 and xvida2 < x + radio/1.5) and (yvida2 > y + radio/-1.5 and yvida2 < y + radio/1.5):
        radio += 10
        score = score + 10
        xmalo2 = random.randrange(10, 995)
        ymalo2 = random.randrange(10, 995)
        xvida2 = random.randrange(10, 995)
        yvida2 = random.randrange(10, 995)
    if xvida2 > 1000-vel:
        xvida2 = 10
    elif xvida2 < vel:
        xvida2 = 995
    if yvida2 > 1000-vel:
        yvida2 = 10
    elif yvida2 < vel:
        yvida2 = 995

    if (xmalo2 > x + radio/-2 and xmalo2 < x + radio/2) and (ymalo2 > y + radio/-2 and ymalo2 < y + radio/2):
        radio -= 20
        score = score - 5
        xmalo2 = random.randrange(10, 995)
        ymalo2 = random.randrange(10, 995)
        xvida2 = random.randrange(10, 995)
        yvida2 = random.randrange(10, 995)
    if xmalo2 > 1000-vel:
        xmalo2 = 10
    elif xmalo2 < vel:
        xmalo2 = 995
    if ymalo2 > 1000-vel:
        ymalo2 = 10
    elif ymalo2 < vel:
        ymalo2 = 995




    #pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    win.fill((0,0,0))
    pygame.draw.circle(win, (255, 255, 255), (x, y), radio)
    pygame.draw.circle(win, (255, 0, 0), (xmalo, ymalo), 5)
    pygame.draw.circle(win, (0, 255, 0), (xvida, yvida), 5)
    pygame.draw.circle(win, (255, 0, 0), (xmalo1, ymalo1), 5)
    pygame.draw.circle(win, (0, 255, 0), (xvida1, yvida1), 5)
    pygame.draw.circle(win, (0, 0, 26), (xmalo2, ymalo2), 5)
    pygame.draw.circle(win, (255, 255, 0), (xvida2, yvida2), 5)
    pygame.display.update()

    if radio >= 800:
        print ("YOU WIN")
        print ("FINAL SCORE: " + str(score))
        run = False
    elif radio <= 0:
        print ("YOU LOSE")
        run = False

pygame.quit()