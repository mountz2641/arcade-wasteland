import arcade
import arcade.key

LANE_SIZE = 100

class Player(arcade.Sprite):
    def setup(self, world, x, y):
        self.world = world
        self.center_x = x
        self.center_y = y
        self.location = 1
        """ 2
            1
            0
        """
    def walk(self, direction):
        if(direction == 'up'):
            self.location += 1
            self.center_y += LANE_SIZE
        elif(direction == 'down'):
            self.location -= 1
            self.center_y -= LANE_SIZE