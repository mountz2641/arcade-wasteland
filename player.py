import arcade
import arcade.key
from bullet import Bullet

LANE_SIZE = 100

class Player(arcade.Sprite):
    def setup(self, world, x, y, enemy_list):
        self.world = world
        self.center_x = x
        self.center_y = y
        self.lane = 1
        self.enemy_list = enemy_list
        self.item = 'gun'
        """ 2   5
            1   4
            0   3
        """
    def walk(self, direction):
        if(direction == 'up'):
            self.lane += 1
            self.center_y += LANE_SIZE
        elif(direction == 'down'):
            self.lane -= 1
            self.center_y -= LANE_SIZE
        elif(direction == 'left'):
            self.lane -= 3
            self.center_x -= 50
        elif(direction == 'right'):
            self.lane += 3
            self.center_x += 50

    def action(self):
        if(self.item == 'gun'):
            self.shoot()
    def shoot(self):
        self.bullet = Bullet('./image/bullet.png',1)
        self.bullet.setup(self, self.lane, self.world, self.enemy_list)
        self.world.bullet_list.append(self.bullet)
