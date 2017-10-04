import arcade

LANE_SIZE = 100

class Gun(arcade.Sprite):
    def setup(self, player, world, lane):
        self.player = player
        self.world = world
        self.gun_left = arcade.load_texture('./image/revolver_left.png')
        self.gun_right = arcade.load_texture('./image/revolver_right.png')
        self.texture = self.gun_left
        self.center_x = player.center_x - 30
        self.center_y = player.center_y

    def moveUp(self):
        self.center_y += LANE_SIZE 
    def moveDown(self):
        self.center_y -= LANE_SIZE
    def swapLeft(self):
        self.center_x -= 110
        self.texture = self.gun_left
    def swapRight(self):
        self.center_x += 110
        self.texture = self.gun_right

        
        
        
