import pygame as pg
from settings import *
from tilemap import collide_hit_rect
vec = pg.math.Vector2

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y
            
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walk_count = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        
    
    # LOADING IMAGES...
    def load_images(self):
        # PLAYER running frames
        PLAYER_RUN_1 = pg.image.load(PLAYER_RUN_1_PATH).convert_alpha()
        PLAYER_RUN_2 = pg.image.load(PLAYER_RUN_2_PATH).convert_alpha()
        PLAYER_RUN_3 = pg.image.load(PLAYER_RUN_3_PATH).convert_alpha()
        PLAYER_RUN_4 = pg.image.load(PLAYER_RUN_4_PATH).convert_alpha()
        # PLAYER idle frames
        PLAYER_IDLE_1 = pg.image.load(PLAYER_IDLE_1_PATH).convert_alpha()
        PLAYER_IDLE_2 = pg.image.load(PLAYER_IDLE_2_PATH).convert_alpha()
        PLAYER_IDLE_3 = pg.image.load(PLAYER_IDLE_3_PATH).convert_alpha()
        PLAYER_IDLE_4 = pg.image.load(PLAYER_IDLE_4_PATH).convert_alpha()

        # ANIMATION frames
        self.idle_frames = [PLAYER_IDLE_1, PLAYER_IDLE_2, PLAYER_IDLE_3, PLAYER_IDLE_4]
        self.walk_frames_r = [PLAYER_RUN_1, PLAYER_RUN_2, PLAYER_RUN_3, PLAYER_RUN_4]
        self.walk_frames_l = []
        for i in self.walk_frames_r:
            self.walk_frames_l.append(pg.transform.flip(i, True, False))

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        # diagonal movement pythagoras suttin
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def update(self):
        self.animate()
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.rect.y = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
        # show walk animation
        if self.walking:
            if now - self.last_update > 75:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]      
        # show idle animation
        if not self.walk_count:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                self.image = self.idle_frames[self.current_frame]

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # set up for animation
        self.walk_count = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0
        self.health = 100
    
    def update(self):
        self.animate()
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(MOB_SPEED, 0).rotate(-self.rot)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        #if self.health <= 0:
        #    self.kill()
        #self.rect.center = self.pos.x
        #collide_with_walls(self, self.game.walls, 'x')
        #self.hit_rect.centery = self.pos.y
        #collide_with_walls(self, self.game.walls, 'y')
        #self.rect.center = self.hit_rect.center
        # LOADING IMAGES...

    def load_images(self):
        # MOB running frames
        MOB_RUN_1 = pg.image.load(MOB_RUN_1_PATH).convert_alpha()
        MOB_RUN_2 = pg.image.load(MOB_RUN_2_PATH).convert_alpha()
        MOB_RUN_3 = pg.image.load(MOB_RUN_3_PATH).convert_alpha()
        MOB_RUN_4 = pg.image.load(MOB_RUN_4_PATH).convert_alpha()
        # MOB idle frames
        MOB_IDLE_1 = pg.image.load(MOB_IDLE_1_PATH).convert_alpha()
        MOB_IDLE_2 = pg.image.load(MOB_IDLE_2_PATH).convert_alpha()
        MOB_IDLE_3 = pg.image.load(MOB_IDLE_3_PATH).convert_alpha()
        MOB_IDLE_4 = pg.image.load(MOB_IDLE_4_PATH).convert_alpha()

        # ANIMATION frames
        self.idle_frames = [MOB_IDLE_1, MOB_IDLE_2, MOB_IDLE_3, MOB_IDLE_4]
        self.walk_frames_r = [MOB_RUN_1, MOB_RUN_2, MOB_RUN_3, MOB_RUN_4]
        self.walk_frames_l = []
        for i in self.walk_frames_r:
            self.walk_frames_l.append(pg.transform.flip(i, True, False))
  
    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
        # show walk animation
        if self.walking:
            if now - self.last_update > 75:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]      
        # show idle animation
        if not self.walk_count:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                self.image = self.idle_frames[self.current_frame]

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
