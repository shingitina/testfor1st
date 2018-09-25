#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from __future__ import division
import random
import pygame
import os
from pygame.locals import *

FULLSCREEN = False  # True にするとフルスクリーン表示
#FPS = 60  # 秒間描画枚数
FPS = 5  # 秒間描画枚数
WIDTH, HEIGHT = 128, 128  # 表示する画面のサイズ
#LINEWIDTH = 10  # 線の太さ
LINEWIDTH = 20  # 線の太さ
#COLOR = 0, 255, 200  # 色
#BG_COLOR = 0, 0, 50  # 背景色
BG_COLOR = 0, 0, 0  # 背景色

def main():
    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT),
        (pygame.FULLSCREEN |
         pygame.HWSURFACE |
         pygame.DOUBLEBUF) if FULLSCREEN else 0)
    title_font = pygame.font.SysFont('', HEIGHT // 5)
    credit_font = pygame.font.SysFont('', HEIGHT // 10)
    timer = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    screen.fill(BG_COLOR)
    pos_prev = (
        random.randint(-WIDTH // 10 , int(WIDTH * 1.1)),
        random.randint(-HEIGHT // 10, int(HEIGHT * 1.1)))
    while True:
        timer.tick(FPS)
        if random.randint(0, 100) == 2:
            screen.fill(BG_COLOR)
        color_rand = (
            random.randint(0, 255)
          , random.randint(0, 255)
          , random.randint(0, 255))

        line_width = random.randint(1, LINEWIDTH)
        pos_new = (
            random.randint(-WIDTH // 10 , int(WIDTH * 1.1)),
            random.randint(-HEIGHT // 10, int(HEIGHT * 1.1)))
        pygame.draw.line(
#            screen, COLOR,
            screen, color_rand,
            pos_prev, pos_new,
            line_width)
        pos_prev = pos_new

#            pygame.draw.line(
#                screen, (0, 0, 0),
#                (random.randint(-WIDTH // 10 , WIDTH * 1.1),
#                 random.randint(-HEIGHT // 10, HEIGHT * 1.1)),
#                (random.randint(-WIDTH // 10 , WIDTH * 1.1),
#                 random.randint(-HEIGHT // 10, HEIGHT * 1.1)),
#                LINEWIDTH)

        pygame.display.flip()
        cap = '%5.2f fps %5.2f sec' % (
            timer.get_fps(),
            (pygame.time.get_ticks() - start_time) / 1000)
        pygame.display.set_caption(cap)
        if pygame.event.get((QUIT, KEYDOWN, MOUSEBUTTONDOWN)):
            return

if __name__=='__main__':
    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((128, 128))
    try:
        main()
    finally:
        pygame.quit()
