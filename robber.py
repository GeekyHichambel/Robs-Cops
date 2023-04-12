import pygame as pg
import config as cfg
import images as ig
import csv

class roby():

	def __init__(self,x,y):
		self.vel = 3
		self.image = ig.mr_rob_front
		self.x , self.y = x,y
		self.mask = pg.mask.from_surface(self.image)

	def moving(self):
		if cfg.movement:
			#up
			if cfg.direc == 1 and cfg.moving_up == True:
				self.image = ig.mr_rob_back
				self.mask = pg.mask.from_surface(self.image)
				if (self.y - self.vel) >= 0:
					self.y = (self.y-self.vel) 
			#down
			elif cfg.direc == 2 and cfg.moving_down == True:
				self.image = ig.mr_rob_front
				self.mask = pg.mask.from_surface(self.image)
				if ((self.y+50) + self.vel) <= cfg.screen_height:
					self.y = (self.y+self.vel)
			#left
			elif cfg.direc == 3 and cfg.moving_left == True:
				self.image = ig.mr_rob_left
				self.mask = pg.mask.from_surface(self.image)
				if (self.x - self.vel) > 0:
					self.x = (self.x-self.vel)
				elif (self.x - self.vel) <= 0:
					self.x = cfg.screen_width + 10
			#right
			elif cfg.direc == 4 and cfg.moving_right == True:
				self.image = ig.mr_rob_right
				self.mask = pg.mask.from_surface(self.image)
				if (self.x + self.vel) < cfg.screen_width:
					self.x = (self.x+self.vel)
				elif (self.x + self.vel) >= cfg.screen_width: 
					self.x = -10

	def notmoving(self):
		cfg.moving_up = False
		cfg.moving_right = False
		cfg.moving_left = False
		cfg.moving_down = False

	def move_func(self,direc):
		cfg.direc = direc
		if direc == 1:
			cfg.moving_up = True
			cfg.moving_down = False
			cfg.moving_left = False
			cfg.moving_right = False
		elif direc == 2:
			cfg.moving_up = False
			cfg.moving_down = True
			cfg.moving_left = False
			cfg.moving_right = False
		elif direc == 3:
			cfg.moving_up = False
			cfg.moving_down = False
			cfg.moving_left = True
			cfg.moving_right = False
		elif direc == 4:
			cfg.moving_up = False
			cfg.moving_down = False
			cfg.moving_left = False
			cfg.moving_right = True		


	def draw(self,screen):
		screen.blit(self.image,(self.x,self.y))
					
robman = roby(372,802)