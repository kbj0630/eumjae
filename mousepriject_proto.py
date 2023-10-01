import pygame as pg
import pyautogui as pag
import sys

pg.init()

screen_size = [800, 800]
screen_color = [255, 255, 255]
screen = pg.display.set_mode(screen_size)

pag.moveTo(760, 330)

specific_area = pg.Rect(100, 100, 200, 200)

while True:
    screen.fill(screen_color)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    mouse_x, mouse_y = pg.mouse.get_pos()

    screen.fill((0, 0, 0))

    pg.draw.rect(screen, (102, 255, 255), specific_area)

    if specific_area.collidepoint(mouse_x, mouse_y):
        print(f'현재 좌표(pygame): ({mouse_x}, {mouse_y}), (pyautogui): {pag.position()}')
    else:
        print(f'*벗어남* 현재 좌표(pygame): ({mouse_x}, {mouse_y}), (pyautogui): {pag.position()}')
        break

    pg.display.update()


