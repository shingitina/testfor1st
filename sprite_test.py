import pygame, math
from pygame.locals import *
import random, sys, os, re
from PIL import Image

SCR_RECT = Rect(0, 0, 128, 128) # screen size by px
#コメント(utf-8)

#IMG_FILE = "enterprize.jpg"
#IMG_FILE = "20101201_il01_035.jpg"
#IMG_FILE = "aurora001.jpg"
#IMG_FILE = "mig2.jpg"
#IMG_FILE = "73475789.png"
#IMG_FILE = "star1.png"
#IMG_FILE = "moment_in_space_by_adriencgd.png"
#IMG_FILE = ""
IMG_FILE = "p11176.png"

class TestSprite:
    def __init__(self):
        os.putenv('SDL_FBDEV', '/dev/fb1')
        pygame.init()
        pygame.mouse.set_visible(False)
        screen = pygame.display.set_mode(SCR_RECT.size)
        pygame.display.set_caption('test')
        width, height = self.load_images()
        self.init_game(width, height)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()

    def init_game(self, width, height):
        self.all_sprite = pygame.sprite.RenderUpdates()
        self.pc = pygame.sprite.Group()
        Player.containers = self.all_sprite, self.pc
        self.player = Player(width, height)

    def update(self):
        self.all_sprite.update()

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.all_sprite.draw(screen)

    def load_images(self):
        Player.image, width, height  = self.load_image(IMG_FILE)
        return width, height

    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def load_image(self, filename, colorkey=None):
        """
        #load image

        @param filename filename includes directory
        @param colorkey background color (default None)
        @return pygame.surface.Surface
        """
        #check if image file is png or gif
        filecase = re.compile(r'[a-zA-Z0-9_/]+\.png|[a-zA-Z0-9_/]+\.gif')

        img = Image.open(filename)
        print("Image size(Width, Height) = (%d, %d)" % img.size)
        width  = img.size[0]
        height = img.size[1]

        try:
            image = pygame.image.load(filename)
        except pygame.error as message:
            print("Cannot load image: " + filename)
            raise SystemExit(message)

        # process by extention
        is_match = filecase.match(filename)
        if is_match:
            image = image.convert_alpha()
        else:
            image = image.convert()

        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image, width, height

class Player(pygame.sprite.Sprite):
#    speed = 3 # moving speed
    speed = 1 # moving speed
#    BEGIN_LEFT=-303
#    POS_BEGIN_LEFT=-303
#    POS_END_LIMIT=-303
#    IMG_WIDTH = 303
#    limit = IMG_WIDTH + 128

    def __init__(self, width, height):
        self.width  = width
        self.height = height
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.bottom = SCR_RECT.bottom
#        self.rect.left = 400
#        self.rect.left = -128
#        self.rect.left = -self.IMG_WIDTH
        self.rect.left = -self.width
        self.limit = self.width + 128

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.limit == 0:
#            self.rect = self.rect.clamp(SCR_RECT)
#            self.rect.left = -128
            self.rect.left = -self.width
            self.limit = self.width  + 128
        else:
            self.limit -= 1

if __name__ == '__main__':
    TestSprite()
