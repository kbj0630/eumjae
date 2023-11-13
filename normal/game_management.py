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
crash_color = (68, 114, 196)
goal_color = (255, 255, 0)
end_goal_color = (255, 0, 0)

#퀴즈 관련 변수
quiz_answer = {"images/normal_quiz1.jpg" : blue, "images/normal_quiz2.jpg" : yellow, "images/normal_quiz3.jpg" : blue, "images/normal_quiz4.jpg" : blue, "images/normal_quiz5.jpg" : red}
quiz_order = random.sample(list(quiz_answer.keys()), 3)
quiz_next = 0


#스테이지 관련 변수
stagelist = ["images/normal_stage1.jpg","images/normal_stage2.jpg", "images/normal_stage3.jpg"]
stage_next = 0
clear_rate = 0

def cursor_set():
    cursor_x = 400
    cursor_y = 210
    pag.moveTo(cursor_x, cursor_y)