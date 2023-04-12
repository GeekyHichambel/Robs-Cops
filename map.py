import pygame as pg
import os
import sys
import csv
import images as ig
import config as cfg

#1 - pillar_up
#2 - pillar_across
#3 - pillar_corner
#8 - pillar_corner2
#9 - pillar_corner4
#10 - pillar_corner3
#13 - barrier_across
#14 - safe
#16 - money1
#17 - money2
#18 - money3
#19 - money4
class Tile(pg.sprite.Sprite):

	def __init__(self,image, x, y):
		super(Tile, self).__init__()
		self.image = image
		self.x = x
		self.y = y
		self.mask = pg.mask.from_surface(self.image)

	def draw(self, screen):
		screen.blit(self.image,(self.x,self.y))

class TileMap():
	def __init__(self, filename):
		self.x_index = 0
		self.y_index = 0
		self.tile_size_1 = 16
		self.tile_size_2 = 32
		self.start_x = 0
		self.start_y = 0
		self.tiles = self.tile_load(filename)
		self.map_surface = pg.Surface((self.map_w, self.map_h))
		self.map_surface.set_colorkey((0,0,0))

	def draw_map(self, surface):
		surface.blit(self.map_surface,(0,0)) 

	def load_map(self):
		for tile in self.tiles:
			tile.draw(self.map_surface)

	def csv_load(self, filename):
		map = []
		with open(os.path.join(filename)) as data:
			data = csv.reader(data, delimiter = ',')

			for row in data:
				map.append(list(row))

		return map

	def tile_load(self, filename):
		tiles = pg.sprite.Group()
		map = self.csv_load(filename)
		x,y = 0,10
		for self.y_index, row in enumerate(map):
			x = 0 
			for self.x_index, tile in enumerate(row):
				if tile == '1': #pillar_up
					tiles.add(Tile(ig.pillar_up, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '2': #pillar_across
					tiles.add(Tile(ig.pillar_across, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '3': #pillar_corner
					tiles.add(Tile(ig.pillar_corner, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '8': #pillar_corner2
					tiles.add(Tile(ig.pillar_corner2, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '9': #pillar_corner4
					tiles.add(Tile(ig.pillar_corner4, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '10': #pillar_corner3
					tiles.add(Tile(ig.pillar_corner3, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '13': #barrier_across
					tiles.add(Tile(ig.barrier_across, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '14': #safe
					tiles.add(Tile(ig.safe, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '16': #money1
					tiles.add(Tile(ig.money1, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '17': #money2
					tiles.add(Tile(ig.money2, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '18': #money3
					tiles.add(Tile(ig.money3, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '19': #money4
					tiles.add(Tile(ig.money4, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '24': #pistol1
					tiles.add(Tile(ig.pistol1, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '25': #pistol2
					tiles.add(Tile(ig.pistol2, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '26': #pistol3
					tiles.add(Tile(ig.pistol3, x*self.tile_size_1, y*self.tile_size_1))

				elif tile == '27': #pistol4
					tiles.add(Tile(ig.pistol4, x*self.tile_size_1, y*self.tile_size_1))

				x += 1
			y += 1

		self.map_w, self.map_h = x*self.tile_size_1, y*self.tile_size_1
		return tiles

	def get_collisions(self,tiles,obj):
		i = 0
		collisions = []
		for tile in (tiles):
			collide_mask = tile.mask.overlap_mask(obj.mask, (obj.x - tile.x, obj.y - tile.y))
			if collide_mask.count() > 0:
				collisions.append(tile) 
				i+=1

		return i,collisions

	def checkcollision(self,tiles,obj):
		i,collisions = tiles.get_collisions(tiles.tiles,obj)
		money = []
		for tile in collisions:
			if tile.image == ig.money1 or tile.image == ig.money2 or tile.image == ig.money3 or tile.image == ig.money4:
				money.append(tile)
				if len(money) == 4:
					for tile in money:
						tile.image = ig.none
				
					cfg.score += 1

			elif tile.image == ig.pistol1 or tile.image == ig.pistol2 or tile.image == ig.pistol3 or tile.image == ig.pistol4:
					pass

			elif tile.image == ig.none:
				pass

			else:
				obj.notmoving()
				if cfg.direc == 1:
					obj.y += 3

				elif cfg.direc == 2:
					obj.y -= 3

				elif cfg.direc == 3:
					obj.x += 3

				elif cfg.direc == 4:
					obj.x -= 3
