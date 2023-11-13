import pygame as pg
import pyautogui as pag
import sys
from game_management import *

class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(screen_size)
        pg.display.set_caption("마우스 피하기")
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.Font(None, 40)
        self.tmr = 0
        self.life = 3

    def stage(self):
        if not hasattr(self, 'tmr_initialized'):  # tmr이 초기화되지 않았으면
            self.tmr = 0  # 타이머 초기화
            self.tmr_initialized = True
        img_bg = pg.image.load(stagelist[stage_next])
        img_bg = pg.transform.scale(img_bg, screen_size)
        clock = pg.time.Clock()
        font = pg.font.Font(None, 40)
        self.running = True

        while self.running:
            self.tmr += 1
            mouse_x, mouse_y = pg.mouse.get_pos()
            self.crash_wall(img_bg, mouse_x, mouse_y)
            self.goal(img_bg, mouse_x, mouse_y)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.txt = font.render(str(round(self.tmr/60, 2)), True, black)
            self.screen.blit(img_bg, [0, 0])
            self.screen.blit(self.txt, [10, 10])
            pg.display.update()
            clock.tick(60)

    def quiz(self):
        global quiz_next
        self.img_bg = pg.image.load(quiz_order[quiz_next])
        self.img_bg = pg.transform.scale(self.img_bg, screen_size)
        self.running = True

        while self.running:
            self.mouse_x, self.mouse_y = pg.mouse.get_pos()
            self.iscorrect = self.img_bg.get_at((self.mouse_x, self.mouse_y))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    for key in quiz_order:                            
                        if self.iscorrect == quiz_answer[key]:
                                quiz_next += 1
                                self.life -= 1
                                print("정답")
                                self.stage()
                        else:
                            print("오답")
                            self.gameover_screen()
                            self.running = False
                
            
            self.screen.blit(self.img_bg, [0,0])
            pg.display.update()

            
    def crash_wall(self, image, mouse_x, mouse_y):
        self.iscrash = image.get_at((mouse_x, mouse_y))

        if self.iscrash == crash_color:
            print(self.iscrash)
            print(self.life)
            if 0 < self.life < 4:
                print("crash")
                self.quiz()
            else:
                self.running = False
                self.gameover_screen()
            

    def goal(self, image, mouse_x, mouse_y):
        global stage_next
        global clear_rate
        self.isgoal = image.get_at((mouse_x, mouse_y))
        if self.isgoal == goal_color:
            if stage_next == 0:
                stage_next = 1
                clear_rate += 1
                self.stage()
                return
            elif stage_next == 1:
                stage_next = 2
                clear_rate += 1
                self.stage()
                return
            
        if self.isgoal == end_goal_color:
            print('goal')
            self.clear()
            return


    def start_screen(self):
        img_bg = pg.image.load("images/start.jpg")
        img_bg = pg.transform.scale(img_bg, screen_size)
        pag.moveTo(950,750)

        self.screen.blit(img_bg, [0, 0])
        pg.display.update()

        self.wait_for_start()


    def gameover_screen(self):
        img_bg = pg.image.load("images/game over.jpg")
        img_bg = pg.transform.scale(img_bg, screen_size)

        if not self.running:
            return
        self.screen.blit(img_bg, [0, 0])
        pg.display.update()

    def wait_for_start(self):
        self.waiting = True
        while self.waiting:
            mouse_x, mouse_y = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    pixel_color = self.screen.get_at((mouse_x, mouse_y))
                    if pixel_color == (14,208,60):
                        self.waiting = False
                        return
                    
    def clear(self):
        img_bg = pg.image.load("images/clear.jpg")
        img_bg = pg.transform.scale(img_bg, screen_size)

        self.screen.blit(img_bg, [0, 0])
        pg.display.update()

        self.wait_for_start()


g = Game()

g.start_screen()

cursor_set()
g.stage()
    
g.gameover_screen()