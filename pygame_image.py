import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg") #練習1
    kk_img = pg.image.load("ex01-20230613/fig/3.png")
    kk_img_1 = pg.transform.flip(kk_img, True, False)
    kk_img_2 = pg.transform.rotozoom(kk_img_1, 10, 1.0)
    kk_imgs = [kk_img_1, kk_img_2]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])

        screen.blit(kk_imgs[tmr % 2], [300, 200])

        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()