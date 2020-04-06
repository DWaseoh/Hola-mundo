import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

class platform():
    def __init__(self,x,y,width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

#Player
x = 50
y = 50
width = 20
height = 40
vel = 5

#Platform
xp = 300
yp = 450
widthp = 60
heightp = 10

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel

    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:

            print(jumpCount)
            print(str(x))
            print(str(yp) + " " + str(widthp + yp))
            if (x > yp and x < widthp + yp):
                jumpCount = 10
                isJump = False
                print("CUMPLIDO")
            else:
                y -= (jumpCount * abs(jumpCount)) * 0.3
                jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False



    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.draw.rect(win, (255,0,0), (xp, yp, widthp, heightp))
    pygame.display.update()

pygame.quit()