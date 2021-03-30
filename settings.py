import pygame as pg
import sys
import os
from os import path

# COLOUR LIBRARY
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 255, 0)
YELLOW = (255, 255, 0)

# GAME SETTINGS
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = 'Dungeon Game'
ICON = pg.image.load('icon.png')
BGCOLOR = DARKGREY

TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# PLAYER SETTINGS
PLAYER_SPEED = 300
PLAYER_ATTACK_DMG = 15
PLAYER_HEALTH = 100
PLAYER_HIT_RECT = pg.Rect(0, 0, 0, 0)

# LOADING - PATH for player running frames
PLAYER_RUN_1_PATH = os.path.join('assets', 'knight_f_run_anim_f0.png')
PLAYER_RUN_2_PATH = os.path.join('assets', 'knight_f_run_anim_f1.png')
PLAYER_RUN_3_PATH = os.path.join('assets', 'knight_f_run_anim_f2.png')
PLAYER_RUN_4_PATH = os.path.join('assets', 'knight_f_run_anim_f3.png') 

# LOADING - PATH for player idle frames
PLAYER_IDLE_1_PATH = os.path.join('assets', 'knight_f_idle_anim_f0.png')
PLAYER_IDLE_2_PATH = os.path.join('assets', 'knight_f_idle_anim_f1.png')
PLAYER_IDLE_3_PATH = os.path.join('assets', 'knight_f_idle_anim_f2.png')
PLAYER_IDLE_4_PATH = os.path.join('assets', 'knight_f_idle_anim_f3.png') 

# PLAYER Damage frames. if player is damaged player this animation.
PLAYER_HIT_1_PATH = os.path.join('assets', 'knight_f_hit_anim_f0.png')

# MOB SETTINGS
MOB_SPEED = 100
MOB_ATTACK_DMG = 10
MOB_HEALTH = 100
MOB_HIT_RECT = pg.Rect(0, 0, 0, 0)

# LOADING - PATH for mob running frames
MOB_RUN_1_PATH = os.path.join('assets', 'goblin_run_anim_f0.png')
MOB_RUN_2_PATH = os.path.join('assets', 'goblin_run_anim_f1.png')
MOB_RUN_3_PATH = os.path.join('assets', 'goblin_run_anim_f2.png')
MOB_RUN_4_PATH = os.path.join('assets', 'goblin_run_anim_f3.png') 

# LOADING - PATH for mob idle frames
MOB_IDLE_1_PATH = os.path.join('assets', 'goblin_idle_anim_f0.png')
MOB_IDLE_2_PATH = os.path.join('assets', 'goblin_idle_anim_f1.png')
MOB_IDLE_3_PATH = os.path.join('assets', 'goblin_idle_anim_f2.png')
MOB_IDLE_4_PATH = os.path.join('assets', 'goblin_idle_anim_f3.png') 
