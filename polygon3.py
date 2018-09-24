import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((128, 128))
myclock = pygame.time.Clock()
screen.fill(BLACK)

#colors = (RED, GREEN, BLUE)
colors = (
    (255,   0,   0)
  , (127, 255, 127)
  , (255, 255,   0)
  , (  0, 255,   0)
  , (  0, 255, 255)
  , ( 64,  64, 255)
  , (255,   0, 255)
    )

flag=0
while flag==0:
    screen.fill(BLACK)
    triangle = [(20, 60), (30, 40), (40, 60)]
    for idx in range(len(colors)):
        pygame.draw.polygon(screen, colors[idx], triangle)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT: flag=1
        myclock.tick(2)

pygame.quit()
