import pygame as pg
import os

main_menu = None
main_game = None
controls = None
game_over = None
#robber_images
mr_rob_front = pg.transform.scale(pg.image.load(os.path.join("reso/imgs","robber_front.png")),(48,48))
mr_rob_back = pg.transform.scale(pg.image.load(os.path.join("reso/imgs","robber_back.png")),(48,48))
mr_rob_right = pg.transform.scale(pg.image.load(os.path.join("reso/imgs","robber_right.png")),(48,48))
mr_rob_left = pg.transform.scale(pg.image.load(os.path.join("reso/imgs","robber_left.png")),(48,48))
#tiles
barrier_across = pg.image.load(os.path.join('reso/tiles','barrier_across.png'))
pillar_across = pg.image.load(os.path.join('reso/tiles','pillar_across.png'))
pillar_corner = pg.image.load(os.path.join('reso/tiles','pillar_corner.png'))
pillar_corner2 = pg.image.load(os.path.join('reso/tiles','pillar_corner2.png'))
pillar_corner3 = pg.image.load(os.path.join('reso/tiles','pillar_corner3.png'))
pillar_corner4 = pg.image.load(os.path.join('reso/tiles','pillar_corner4.png'))
pillar_up = pg.image.load(os.path.join('reso/tiles','pillar_up.png'))
safe = pg.image.load(os.path.join('reso/tiles','safe.png'))
money1 = pg.image.load(os.path.join('reso/tiles','money1.png'))
money2 = pg.image.load(os.path.join('reso/tiles','money2.png'))
money3 = pg.image.load(os.path.join('reso/tiles','money3.png'))
money4 = pg.image.load(os.path.join('reso/tiles','money4.png'))
none = pg.image.load(os.path.join('reso/tiles','black.png'))
pistol1 = pg.image.load(os.path.join('reso/tiles','pistol1.png'))
pistol2 = pg.image.load(os.path.join('reso/tiles','pistol2.png'))
pistol3 = pg.image.load(os.path.join('reso/tiles','pistol3.png'))
pistol4 = pg.image.load(os.path.join('reso/tiles','pistol4.png'))

cop1 = None
cop2 = None
cop3 = None
start_but = None
controls_but = None
mute_but = None

def perf():
	mr_rob_front.convert_alpha()
	mr_rob_back.convert_alpha()
	mr_rob_left.convert_alpha()
	mr_rob_right.convert_alpha()
	barrier_across.convert_alpha()
	pillar_across.convert_alpha()
	pillar_corner.convert_alpha()
	pillar_corner2.convert_alpha()
	pillar_corner3.convert_alpha()
	pillar_corner4.convert_alpha()
	pillar_up.convert_alpha()
	safe.convert_alpha()
	money1.convert_alpha()
	money2.convert_alpha()
	money3.convert_alpha()
	money4.convert_alpha()
	none.convert_alpha()