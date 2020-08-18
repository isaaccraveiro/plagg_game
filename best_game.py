import pygame
pygame.init()

win = pygame.display.set_mode((852, 480))

pygame.display.set_caption("my best game")

walkright = [
    pygame.image.load('R1.png'),
    pygame.image.load('R2.png'),
    pygame.image.load('R3.png'),
    pygame.image.load('R4.png'),
    pygame.image.load('R5.png'),
    pygame.image.load('R6.png'),
    pygame.image.load('R7.png'),
    pygame.image.load('R8.png'),
    pygame.image.load('R9.png'),
]

walkleft = [
    pygame.image.load('L1.png'),
    pygame.image.load('L2.png'),
    pygame.image.load('L3.png'),
    pygame.image.load('L4.png'),
    pygame.image.load('L5.png'),
    pygame.image.load('L6.png'),
    pygame.image.load('L7.png'),
    pygame.image.load('L8.png'),
    pygame.image.load('L9.png'),
]
bg = pygame.image.load('bg.jpg')
char =  pygame.image.load('standing.png')

isjump = False
jumpcount = 10
screenWidth = 500
left = False
right = False
walkcount = 0

x = 50
y = 425
width = 64
height = 64
vel = 5

def redrawGameWindow ():
  global walkcount
  win.blit(bg, (0,0))

  if walkcount + 1 >= 27:
      walkcount = 0

 # if left:


  pygame.display.update()

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        right = True
        left = False
        walkcount = 0

    if not(isjump):
        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1

        else:
            isjump = False
            jumpcount = 10

    redrawGameWindow ()

(jumpcount ** 2) * 0.5 * neg
pygame.quit()
