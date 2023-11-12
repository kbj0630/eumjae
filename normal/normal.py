import pygame as pg
import pyautogui as pag
import sys
import game_management as gm



def start():
    pg.init() #파이게임 초기화
    pg.display.set_caption("마우스 피하기")
    screen = pg.display.set_mode(gm.screen_size)
    img_bg = pg.image.load("images/start.jpg")
    img_bg = pg.transform.scale(img_bg, gm.screen_size)

    pag.moveTo(950,750)

    while True: #무한 루프
        mouse_x, mouse_y = pg.mouse.get_pos() #현재 마우스 커서의 위치
        for event in pg.event.get(): #현재 발생한 이벤트 가져오기
            if event.type == pg.QUIT: #게임 창을 닫는 이벤트 발생하면 게임종료
                pg.quit()
                sys.exit()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                pixel_color = screen.get_at((mouse_x, mouse_y))
                if pixel_color == (14,208,60):
                    return

        screen.blit(img_bg, [0, 0])
        pg.display.update()


if __name__ == '__main__':
    start()
    gm.stage_n()
