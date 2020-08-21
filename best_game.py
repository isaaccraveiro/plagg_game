import pygame
pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("my best game")

walkright = [
    pygame.image.load('plagg_walk_right1.png'),
    pygame.image.load('plagg_walk_right2.png'),
    pygame.image.load('plagg_walk_right3.png'),
    pygame.image.load('plagg_walk_right1.png'),
    pygame.image.load('plagg_walk_right2.png'),
    pygame.image.load('plagg_walk_right3.png'),
    pygame.image.load('plagg_walk_right1.png'),
    pygame.image.load('plagg_walk_right2.png'),
    pygame.image.load('plagg_walk_right3.png')
]

walkleft = [
    pygame.image.load('plagg_walk_left1.png'),
    pygame.image.load('plagg_walk_left2.png'),
    pygame.image.load('plagg_walk_left3.png'),
    pygame.image.load('plagg_walk_left1.png'),
    pygame.image.load('plagg_walk_left2.png'),
    pygame.image.load('plagg_walk_left3.png'),
    pygame.image.load('plagg_walk_left1.png'),
    pygame.image.load('plagg_walk_left2.png'),
    pygame.image.load('plagg_walk_left3.png')
]
bg = pygame.image.load('cheese.png')
char =  pygame.image.load('plagg_standing.png')
screenWidth = 500

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
      self.x = x
      self.y = y
      self.width = width
      self.height = height
      self.vel = 5
      self.isjump = False
      self.jumpcount = 10
      self.left = False
      self.right = False
      self.walkcount = 0


def redrawGameWindow ():
  win.blit(bg, (0,0))

  if plagg.walkcount + 1 >= 27:
      plagg.walkcount = 0

  if plagg.left:
      #print("walk count ", plagg.walkcount)
      #print("walk count floor div", plagg.walkcount//3)
      win.blit(walkleft[plagg.walkcount//3], (plagg.x,plagg.y))
      plagg.walkcount += 1
  elif plagg.right:
      #print("walk count ", plagg.walkcount)
      #print("walk count floor div", plagg.walkcount//3)
      win.blit(walkright[plagg.walkcount//3], (plagg.x,plagg.y))
      plagg.walkcount += 1
  else:
      win.blit(char, (plagg.x,plagg.y))
      plagg.walkcount = 0

  pygame.display.update()

run = True
plagg = player(300, 410, 64, 64)
while run == True:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and plagg.x > plagg.vel:
        plagg.x -= plagg.vel
        plagg.left = True
        plagg.right = False
    elif keys[pygame.K_RIGHT] and plagg.x < screenWidth - plagg.width - plagg.vel:
        plagg.x += plagg.vel
        plagg.right = True
        plagg.left = False
    else:
        plagg.left = False
        plagg.right = False
        plagg.walkcount = 0

    if not(plagg.isjump):
        if keys[pygame.K_SPACE]:
            plagg.isjump = True
    else:
        if plagg.jumpcount >= -10:
            neg = 1
            if plagg.jumpcount < 0:
                neg = -1
            plagg.y -= (plagg.jumpcount ** 2) * 0.5 * neg
            # y -= jumpcount + 1 * neg
            plagg.jumpcount -= 1

        else:
            plagg.isjump = False
            plagg.jumpcount = 10

    redrawGameWindow()

pygame.quit()
