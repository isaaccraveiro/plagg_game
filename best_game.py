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
      self.standing = True

    def draw(self,win):
        if self.walkcount + 1 >= 27:
            self.walkcount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkleft[self.walkcount//3], (self.x,self.y))
                self.walkcount += 1
            elif self.right:
                win.blit(walkright[self.walkcount//3], (self.x,self.y))
                self.walkcount += 1
        else:
            if self.right:
                win.blit(walkright[0], (self.x, self.y))
            else:
                win.blit(walkleft[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.colour, (self.x,self.y), self.radius)

class enemy(object):
    walkright = [
        pygame.image.load('R1E.png'),
        pygame.image.load('R2E.png'),
        pygame.image.load('R3E.png'),
        pygame.image.load('R4E.png'),
        pygame.image.load('R5E.png'),
        pygame.image.load('R6E.png'),
        pygame.image.load('R7E.png'),
        pygame.image.load('R8E.png'),
        pygame.image.load('R9E.png'),
        pygame.image.load('R10E.png'),
        pygame.image.load('R11E.png')
    ]
    walkleft = [
        pygame.image.load('L1E.png'),
        pygame.image.load('L2E.png'),
        pygame.image.load('L3E.png'),
        pygame.image.load('L4E.png'),
        pygame.image.load('L5E.png'),
        pygame.image.load('L6E.png'),
        pygame.image.load('L7E.png'),
        pygame.image.load('L8E.png'),
        pygame.image.load('L9E.png'),
        pygame.image.load('L10E.png'),
        pygame.image.load('L11E.png'),
    ]

    def __init__(self, x, y, width, height, end):
        self. x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.y]
        self.walkcount = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walkcount + 1 >= 33:
            self.walkcount = 0

        if self.vel > 0:
            win.blit(self.walkright[self.walkcount //3], (self.x, self.y))
            self.walkcount += 1
        else:
            win.blit(self.walkleft[self.walkcount //3], (self.x, self.y))
            self.walkcount += 1

    def move(self):
      if self.vel > 0:
          if self.x + self.vel < self.path[1]:
              self.x += self.vel
          else:
              self.vel = self.vel * -1
              self.walkcount = 0
      else:
          if self.x - self.vel > self.path[0]:
              self.x += self.vel
          else:
              self.vel = self.vel * -1
              self.walkcount = 0




def redrawGameWindow ():
  win.blit(bg, (0,0))
  plagg.draw(win)
  goblin.draw(win)
  #plagg.walkcount = 0
  for bullet in bullets:
      bullet.draw(win)

  pygame.display.update()

run = True
plagg = player(300, 410, 64, 64)
goblin = enemy(200, 410, 64, 64, 500)
bullets = []
while run == True:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if plagg.left:
            facing = -1
        else:
            facing = 1

        if len (bullets) < 5:
            bullets.append(projectile(round(plagg.x + plagg.width // 2), round(plagg.y + plagg.height // 2), 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and plagg.x > plagg.vel:
        plagg.x -= plagg.vel
        plagg.left = True
        plagg.right = False
        plagg.standing = False
    elif keys[pygame.K_RIGHT] and plagg.x < screenWidth - plagg.width - plagg.vel:
        plagg.x += plagg.vel
        plagg.right = True
        plagg.left = False
        plagg.standing = False
    else:
        plagg.standing = True
        plagg.walkcount = 0

    if not(plagg.isjump):
        if keys[pygame.K_UP]:
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
