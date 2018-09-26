import pygame, os

def hsv2rgb(hue, s, v):
#hue: Hue
#s: Saturation, Chroma
#v: Value, Lightness, Brightness
    reg_num = hue // 60
    idx_reg = hue % 60
    if reg_num == 0:
        r = 255
        g = int(round(idx_reg / 59 * 255))
        b = 0
    elif reg_num == 1:
        r = 255 - int(round(idx_reg / 59 * 255))
        g = 255
        b = 0
    elif reg_num == 2:
        r = 0
        g = 255
        b = int(round(idx_reg / 59 * 255))
    elif reg_num == 3:
        r = 0
        g = 255 - int(round(idx_reg / 59 * 255))
        b = 255
    elif reg_num == 4:
        r = int(round(idx_reg / 59 * 255))
        g = 0
        b = 255
    elif reg_num == 5:
        r = 255
        g = 0
        b = 255 - int(round(idx_reg / 59 * 255))
    return r, g, b

def pygame_setup():
    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()
    pygame.mouse.set_visible(False)

def pygame_main():
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((128, 128))
    screen.fill(BLACK)
    myclock = pygame.time.Clock()
    s, v = 0, 0
    while True:
        screen.fill(BLACK)
#        triangle = [(20, 110), (63, 40), (106, 110)]
        triangle = [(20, 70), (40, 40), (60, 70)]
        for hue in range(360):
#        for idx in range(len(colors)):
            color_rgb = hsv2rgb(hue, s, v)
            pygame.draw.polygon(screen, color_rgb, triangle)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.QUIT: break
            myclock.tick(60)
    pygame.quit()


def main():
    pygame_setup()
    pygame_main()
    exit()

    s, v = 0, 0
    for hue in range(360):
        r, g, b = hsv2rgb(hue, s, v)
        print(r, g, b)

if __name__ == "__main__":
    main()
