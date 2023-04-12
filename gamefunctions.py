import pygame as pg
import sys
import config as cfg
import images as ig
from robber import robman
from map import *
import os

fps = pg.time.Clock()
pg.font.init()
base_font = pg.font.SysFont("felixtitling",50,bold = True)
map = TileMap(os.path.join("reso/lvls","map.csv"))

class scenes():
	def main_menu(self,screen):
		fps.tick(cfg.frames)
		screen.fill('Blue')

		#GAME EVENTS
		for event in pg.event.get():
			if event.type == pg.QUIT:
				cfg.game_on = False

			#KEYPRESSED CHECKS
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					cfg.game_on = False


		pg.display.update()

	def main_game(self,screen):
		fps.tick(cfg.frames)

		#GAME EVENTS
		for event in pg.event.get():
			if event.type == pg.QUIT:
				cfg.game_on = False

			#KEYPRESSED CHECKS
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					cfg.game_on = False

				if event.key == pg.K_w:
					robman.move_func(1)

				if event.key == pg.K_s:
					robman.move_func(2)

				if event.key == pg.K_a:
					robman.move_func(3)

				if event.key == pg.K_d:
					robman.move_func(4)

		if (cfg.moving_up) or (cfg.moving_down) or (cfg.moving_right) or (cfg.moving_left):
			robman.moving()

		screen.fill('black')
		pg.draw.rect(screen,'green',(0,0,cfg.screen_width,160),5)
		pg.draw.rect(screen,'green',(30,30,cfg.screen_width-60,100),5)
		score_text = base_font.render(f"SCORE: {cfg.score}",1,(255,255,255))
		won_text = base_font.render("HURRAY! GAME WON",1,(255,255,255))
		if cfg.score == 193:
			cfg.game_won = True
			robman.notmoving()
			cfg.movement = False
		if not cfg.game_won:
			screen.blit(score_text,(60,60))
		else:
			screen.blit(won_text,(60,60))
		map.checkcollision(map,robman)
		map.load_map()
		map.draw_map(screen)
		
		robman.draw(screen)			

		pg.display.update()

	def controls(self,screen):
		pass

	def game_over(self,screen):
		pass 

func = scenes()