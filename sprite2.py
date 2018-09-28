import pygame, math
from pygame.locals import *
import random, sys, os, re

#SCR_RECT = Rect(0, 0, 800, 600) # スクリーンサイズ(px指定)
SCR_RECT = Rect(0, 0, 128, 128) # スクリーンサイズ(px指定)

class TestSprite:
    def __init__(self):
        os.putenv('SDL_FBDEV', '/dev/fb1')
        pygame.init()
        pygame.mouse.set_visible(False)
        screen = pygame.display.set_mode(SCR_RECT.size)
        pygame.display.set_caption('test')
        self.load_images()
        self.init_game()
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()

    def init_game(self):
        self.all_sprite = pygame.sprite.RenderUpdates()
        self.pc = pygame.sprite.Group()
        Player.containers = self.all_sprite, self.pc
        self.player = Player()

    def update(self):
        self.all_sprite.update()

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.all_sprite.draw(screen)

    def load_images(self):
        Player.image = load_image("enterprize.jpg")

    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

class Player(pygame.sprite.Sprite):
#    speed = 3 # 移動速度
    speed = 1 # 移動速度
    limit = 256

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.bottom = SCR_RECT.bottom #プレイヤーは画面の一番下からスタート
#        self.rect.left = 400
        self.rect.left = -128

    def update(self):
        self.rect.move_ip(self.speed, 0)
        # 画面からはみ出さないようにする
        if self.limit == 0:
#            self.rect = self.rect.clamp(SCR_RECT)
            self.rect.left = -128
            self.limit = 256
        else:
            self.limit -= 1

def load_image(filename, colorkey=None):
    """
    画像をロードする。

    @param filename ファイル名（ディレクトリ含む）
    @param colorkey 背景色 (デフォルト値 None)
    @return pygame.surface.Surface
    """
    # 画像ファイルがpngかgifか判定するための正規表現
    filecase = re.compile(r'[a-zA-Z0-9_/]+\.png|[a-zA-Z0-9_/]+\.gif')

    try:
        image = pygame.image.load(filename)
    except pygame.error as message:
        print("Cannot load image: " + filename)
        raise SystemExit(message)

    # 画像の拡張子によって処理を振り分け
    is_match = filecase.match(filename)
    if is_match:
        image = image.convert_alpha()
    else:
        image = image.convert()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

if __name__ == '__main__':
    TestSprite()
