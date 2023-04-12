import pygame as pg
import config as cfg
import images as ig
from gamefunctions import func

pg.init()
cfg.initialize()

screen = pg.display.set_mode((cfg.screen_width,cfg.screen_height))
pg.display.set_caption('Rob and Cops')
ig.perf()

while cfg.game_on:

	if cfg.switch == 1:
		func.main_menu(screen)

	if cfg.switch == 2:
		func.main_game(screen)
		
	if cfg.switch == 3:
		func.controls(screen)

	if cfg.switch == 4:
		func.game_over(screen)