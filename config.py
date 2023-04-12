import pygame as pg

def initialize():
	global game_on
	global switch
	global frames
	global screen_width
	global screen_height
	global moving_up
	global moving_down
	global moving_left
	global moving_right
	global direc
	global score
	global game_won
	global movement

	direc = None
	game_on = True
	switch = 2
	frames = 60
	screen_width = 800
	screen_height = 960 
	moving_up = False
	moving_down = False
	moving_left = False
	moving_right = False
	score = 0
	game_won = False
	movement = True