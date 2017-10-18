import arcade
import arcade.key
from gun import Gun
from bullet import Bullet

LANE_SIZE = 100
GUN = 101
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
SCORE_UP_LEVEL = 200

class Player(arcade.Sprite):
    def setup(self, world, x, y, enemy_list):
        self.world = world
        self.center_x = x
        self.center_y = y
        self.lane = 1
        self.enemy_list = enemy_list
        self.item = GUN
        self.gun = Gun('./image/revolver_left.png', 0.5)
        self.gun.setup(self, world, self.lane)
        self.world.sprite_list.append(self.gun)
        self.world.gun = self.gun
        self.score = 0
        self.counter = 0
        self.dead_texture = arcade.load_texture('./image/dead_cowboy.png', scale = 0.1)

    def walk(self, direction):
        if direction == DIR_UP:
            self.lane += 1
            self.center_y += LANE_SIZE
            self.gun.moveUp()
        elif direction == DIR_DOWN:
            self.lane -= 1
            self.center_y -= LANE_SIZE
            self.gun.moveDown()
        elif direction == DIR_LEFT:
            self.lane -= 3
            self.center_x -= 50
            self.gun.swapLeft()
        elif direction == DIR_RIGHT:
            self.lane += 3
            self.center_x += 50
            self.gun.swapRight()

    def action(self):
        if self.item == GUN:
            if self.gun.shoot():
                self.shoot()

    def shoot(self):
        self.bullet = Bullet('./image/bullet.png',1)
        self.bullet.setup(self, self.lane, self.world, self.enemy_list)
        self.world.bullet_list.append(self.bullet)

    def dead(self):
        self.texture = self.dead_texture

    def plusScore(self, score):
        self.score += score
        self.counter += score
        if self.counter >= SCORE_UP_LEVEL:
            self.counter -= SCORE_UP_LEVEL
            self.world.increase_level()
