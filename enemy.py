import arcade
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
LANE_SIZE = 100

class Enemy (arcade.Sprite):
    def setup(self, world, lane):
        self.health = 1
        self.direction = 1
        self.world = world
        self.speed = 150
        self.lane = lane
        self.damage = 1
        self.bounty = 10
        if(lane == 0):
            self.center_x = -80
            self.center_y = SCREEN_HEIGHT // 2 + (50 - LANE_SIZE)
            self.direction = 1
        elif(lane == 1):
            self.center_x = -80
            self.center_y = SCREEN_HEIGHT // 2 + 50
            self.direction = 1
        elif(lane == 2):
            self.center_x = -80
            self.center_y = SCREEN_HEIGHT // 2 + (50 + LANE_SIZE)
            self.direction = -1
        elif(lane == 3):
            self.center_x = SCREEN_WIDTH + 80
            self.center_y = SCREEN_HEIGHT // 2 + (50 - LANE_SIZE)
            self.direction = -1
        elif(lane == 4):
            self.center_x = SCREEN_WIDTH + 80
            self.center_y = SCREEN_HEIGHT // 2 + 50
            self.direction = -1
        elif(lane == 5):
            self.center_x = SCREEN_WIDTH + 80
            self.center_y = SCREEN_HEIGHT // 2 + (50 + LANE_SIZE)
            self.direction = -1        
    
    def update(self, delta):
        self.center_x += (int(self.speed * delta) * self.direction)

