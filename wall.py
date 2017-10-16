import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
LANE_SIZE = 100

class Wall(arcade.Sprite):
    def setup(self, world, lane):
        self.health = 5
        self.world = world
        self.lane = lane
        self.health_sprite = []
        self.health_sprite.append(arcade.load_texture('./image/broken_wall.png'))
        self.health_sprite.append(arcade.load_texture('./image/wall_1.png'))
        self.health_sprite.append(arcade.load_texture('./image/wall_2.png'))
        self.health_sprite.append(arcade.load_texture('./image/wall_3.png'))
        self.health_sprite.append(arcade.load_texture('./image/wall_4.png'))
        if(lane == 0):
            self.center_x = SCREEN_WIDTH // 2 - 90
            self.center_y = SCREEN_HEIGHT // 2 + (50 - LANE_SIZE)
        elif(lane == 1):
            self.center_x = SCREEN_WIDTH // 2 - 90
            self.center_y = SCREEN_HEIGHT // 2 + 50
        elif(lane == 2):
            self.center_x = SCREEN_WIDTH // 2 - 90
            self.center_y = SCREEN_HEIGHT // 2 + 50 + LANE_SIZE
        elif(lane == 3):
            self.center_x = SCREEN_WIDTH // 2 + 90
            self.center_y = SCREEN_HEIGHT // 2 + (50 - LANE_SIZE)
        elif(lane == 4):
            self.center_x = SCREEN_WIDTH // 2 + 90
            self.center_y = SCREEN_HEIGHT // 2 + 50
        elif(lane == 5):
            self.center_x = SCREEN_WIDTH // 2 + 90
            self.center_y = SCREEN_HEIGHT // 2 + (50 + LANE_SIZE)

    def getDamage(self, damage):
        self.health -= damage
        self.texture = self.health_sprite[self.health]
        print('wall %d get damage %d remain %d' %(self.lane, damage, self.health))
        if(self.health <= 0):
            self.world.game_over()