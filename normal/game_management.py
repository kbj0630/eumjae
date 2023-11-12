import pygame as pg
import pyautogui as pag
import sys
import random

screen_size = (1170, 700)

#색깔
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (21, 32, 243)
yellow = (255, 255, 0)
crash_color = (68, 115, 197)
goal_color = (254, 0, 0)

#퀴즈 관련 변수
quiz_answer = {"images/quiz1.jpg" : blue, "images/quiz2.jpg" : blue, "images/quiz3.jpg" : red, "images/quiz4.jpg" : blue, "images/quiz5.jpg" : red}
quiz_order = list(quiz_answer.keys())
random.shuffle(quiz_order)
quiz_next = 0

#스테이지 관련 변수
stage = ["images/normal_stage1.jpg","images/normal_stage2.jpg", "images/normal_stage3.jpg"]
stage_next = 0
life = 3


def stage_n():
    global stage_next
    global stage

    screen = pg.display.set_mode(screen_size)
    clock = pg.time.Clock()
    font = pg.font.Font(None, 40)
    tmr = 0

    print(stage_next)
    img_bg = pg.image.load(stage[stage_next])
    img_bg = pg.transform.scale(img_bg, screen_size)
    cursor_set()

    while True:
        tmr += 1
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            crash_wall(img_bg, crash_color, mouse_x, mouse_y)
            goal(img_bg, goal_color, mouse_x, mouse_y)

            if event.type == pg.QUIT:
                stage_next = 0
                quiz_next = 0
                pg.quit()
                sys.exit()

        txt = font.render(str(round((tmr/60), 2)), True, black)
        screen.blit(img_bg, [0, 0])
        screen.blit(txt, (10, 10))
        pg.display.update()
        clock.tick(60)

def quiz():
    global quiz_next
    screen = pg.display.set_mode(screen_size)
    img_bg = pg.image.load(quiz_order[quiz_next])
    img_bg = pg.transform.scale(img_bg, screen_size)

    while True:
        for event in pg.event.get():  # 현재 발생한 이벤트 가져오기
            if event.type == pg.QUIT:
                stage_next = 0
                quiz_next = 0  # 게임 창을 닫는 이벤트 발생하면 게임종료
                pg.quit()
                sys.exit()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                answer = img_bg.get_at((mouse_x, mouse_y))

                for i in quiz_order:
                    if answer == quiz_answer[i]:
                        print("정답")
                        quiz_next += 1
                    else:
                        print("오답")
                        gameover()

        screen.blit(img_bg, [0, 0])
        pg.display.update()

def cursor_set():
    cursor_x = 400
    cursor_y = 200
    pag.moveTo(cursor_x, cursor_y)

def crash_wall(image, crash_color, mouse_x, mouse_y):
    global life
    key = image.get_at((mouse_x, mouse_y))
    if key == crash_color:
        if life > 0:
            life -= 1
            quiz()
        else:
            gameover()


def goal(image, goal_color, mouse_x, mouse_y):
    global stage_next
    key = image.get_at((mouse_x, mouse_y))
    if key == goal_color:
        print("통과")
        stage_next += 1
        stage_n()

def gameover():
    screen = pg.display.set_mode(screen_size)
    img_bg = pg.image.load("images/game over.jpg")
    img_bg = pg.transform.scale(img_bg, screen_size)
    while True:
        for event in pg.event.get():  # 현재 발생한 이벤트 가져오기
            if event.type == pg.QUIT:
                stage_next = 0
                quiz_next = 0  # 게임 창을 닫는 이벤트 발생하면 게임종료
                pg.quit()
                sys.exit()

        screen.blit(img_bg, [0, 0])
        pg.display.update()
