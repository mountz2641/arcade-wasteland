import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
LANE_SIZE = 100

class Wall(arcade.Sprite):
    def setup(self, world, lane):
        self.health = 10
        self.world = world
        self.lane = lane
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
        print('wall %d get damage %d remain %d' %(self.lane, damage, self.health))
