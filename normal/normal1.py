import pygame as pg
import pyautogui as pag
import sys

black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (1170, 700)
crash_color = (68, 115, 197)
goal_color = (254, 0, 0)

def cursor_set(cursor_x,cursor_y): #커서 초기 위치 설정 함수
    pag.moveTo(cursor_x, cursor_y)

def crash_wall(screen, crash_color, mouse_x, mouse_y): #벽 충돌 확인 함수
    pixel_color = screen.get_at((mouse_x, mouse_y))
    if pixel_color == crash_color:
        print("위치 벗어남")
        return True

def goal(screen, goal_color, mouse_x, mouse_y): #목표 도달 확인 함수
    pixel_color = screen.get_at((mouse_x, mouse_y))
    if pixel_color == goal_color:
        print("통과")
        return True

def quiz(screen,img_bg):
    running = True
    while running:
        for event in pg.event.get():  # 현재 발생한 이벤트 가져오기
            if event.type == pg.QUIT:  # 게임 창을 닫는 이벤트 발생하면 게임종료
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1:  # F1키 누르면 전체화면 모드
                    screen = pg.display.set_mode((screen_size), pg.FULLSCREEN)
                if event.key == pg.K_F2 or event.key == pg.K_ESCAPE:  # F2, ESC키 누르면 창 모드
                    screen = pg.display.set_mode((screen_size))
            if event.type == pg.MOUSEBUTTONDOWN:
                print('클릭')
                mouse_x, mouse_y = pg.mouse.get_pos()
                pixel_color = screen.get_at((mouse_x, mouse_y))
                print(pixel_color)
                '''if pixel_color == (21, 32, 243):
                    print("정답")
                    running=False
                if (pixel_color ==(255,0,0)) or (pixel_color ==(0,255,255)):
                    print("오답")
                    running = False'''
        pg.display.update()

def stage_1():
    screen = pg.display.set_mode(screen_size)
    clock = pg.time.Clock()
    font = pg.font.Font(None, 40)
    img_bg = pg.image.load("images/normal_stage1.jpg")
    img_bg = pg.transform.scale(img_bg, screen_size)
    tmr= 0

    cursor_set(400,200)

    while True: #무한 루프
        tmr += 1
        mouse_x, mouse_y = pg.mouse.get_pos() #현재 마우스 커서의 위치
        for event in pg.event.get(): #현재 발생한 이벤트 가져오기
            if crash_wall(screen, crash_color, mouse_x, mouse_y):
                quiz(screen,img_bg)
                while quiz(screen,img_bg):
                    new_img_bg = pg.image.load("quiz1.jpg")
                    img_bg = pg.transform.scale(new_img_bg, screen_size)
            if goal(screen, goal_color, mouse_x, mouse_y):
                return tmr
            if event.type == pg.QUIT: #게임 창을 닫는 이벤트 발생하면 게임종료
                    pg.quit()
                    sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1: #F1키 누르면 전체화면 모드
                    screen = pg.display.set_mode((screen_size), pg.FULLSCREEN)
                if event.key == pg.K_F2 or event.key == pg.K_ESCAPE: #F2, ESC키 누르면 창 모드
                    screen = pg.display.set_mode((screen_size))

        txt = font.render(str(round((tmr/60), 2)), True, black) #현재 시간 문자열로
        screen.blit(img_bg, [0, 0])
        screen.blit(txt, (10, 10))
        pg.display.update()
        clock.tick(60)

def stage_2(tmr_stage1):
    screen = pg.display.set_mode(screen_size)
    clock = pg.time.Clock()
    font = pg.font.Font(None, 40)
    img_bg = pg.image.load("images/normal_stage2.jpg")
    img_bg = pg.transform.scale(img_bg, screen_size)

    cursor_set(400,200)

    while True: #무한 루프
        tmr_stage1 += 1
        mouse_x, mouse_y = pg.mouse.get_pos() #현재 마우스 커서의 위치
        for event in pg.event.get(): #현재 발생한 이벤트 가져오기
            crash_wall(screen, crash_color, mouse_x, mouse_y)
            if goal(screen, goal_color, mouse_x, mouse_y):
                return tmr_stage1
            if event.type == pg.QUIT: #게임 창을 닫는 이벤트 발생하면 게임종료
                    pg.quit()
                    sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1: #F1키 누르면 전체화면 모드
                    screen = pg.display.set_mode((screen_size), pg.FULLSCREEN)
                if event.key == pg.K_F2 or event.key == pg.K_ESCAPE: #F2, ESC키 누르면 창 모드
                    screen = pg.display.set_mode((screen_size))

        txt = font.render(str(round((tmr_stage1/60), 2)), True, black) #현재 시간 문자열로
        screen.blit(img_bg, [0, 0])
        screen.blit(txt, (10, 10))
        pg.display.update()
        clock.tick(60)

def stage_3(tmr_stage2):
    screen = pg.display.set_mode(screen_size)
    clock = pg.time.Clock()
    font = pg.font.Font(None, 40)
    img_bg = pg.image.load("images/normal_stage3.jpg")
    img_bg = pg.transform.scale(img_bg, screen_size)

    cursor_set(400,200)

    while True: #무한 루프
        tmr_stage2 += 1
        mouse_x, mouse_y = pg.mouse.get_pos() #현재 마우스 커서의 위치
        for event in pg.event.get(): #현재 발생한 이벤트 가져오기
            crash_wall(screen, crash_color, mouse_x, mouse_y)
            if goal(screen, goal_color, mouse_x, mouse_y):
                return tmr_stage2
            if event.type == pg.QUIT: #게임 창을 닫는 이벤트 발생하면 게임종료
                    pg.quit()
                    sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1: #F1키 누르면 전체화면 모드
                    screen = pg.display.set_mode((screen_size), pg.FULLSCREEN)
                if event.key == pg.K_F2 or event.key == pg.K_ESCAPE: #F2, ESC키 누르면 창 모드
                    screen = pg.display.set_mode((screen_size))

        txt = font.render(str(round((tmr_stage2/60), 2)), True, black) #현재 시간 문자열로
        screen.blit(img_bg, [0, 0])
        screen.blit(txt, (10, 10))
        pg.display.update()
        clock.tick(60)


def start():
    pg.init() #파이게임 초기화
    pg.display.set_caption("마우스 피하기")
    screen = pg.display.set_mode(screen_size)
    img_bg = pg.image.load("images/start.jpg")
    img_bg = pg.transform.scale(img_bg, screen_size)

    cursor_set(950,750)

    while True: #무한 루프
        mouse_x, mouse_y = pg.mouse.get_pos() #현재 마우스 커서의 위치
        for event in pg.event.get(): #현재 발생한 이벤트 가져오기
            if event.type == pg.QUIT: #게임 창을 닫는 이벤트 발생하면 게임종료
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1: #F1키 누르면 전체화면 모드
                    screen = pg.display.set_mode((screen_size), pg.FULLSCREEN)
                if event.key == pg.K_F2 or event.key == pg.K_ESCAPE: #F2, ESC키 누르면 창 모드
                    screen = pg.display.set_mode((screen_size))
            if event.type == pg.MOUSEBUTTONDOWN:
                pixel_color = screen.get_at((mouse_x, mouse_y))
                if pixel_color == (14,208,60):
                    return

        screen.blit(img_bg, [0, 0])
        pg.display.update()

if __name__ == '__main__':
    start()
    tmr_stage1 = stage_1()
    tmr_stage2 = stage_2(tmr_stage1)
    tmr_stage3 = stage_3(tmr_stage2)
