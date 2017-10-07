import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

class Bullet(arcade.Sprite):
    def setup(self, player, lane, world, enemy_list):
        self.player = player
        self.lane = lane
        self.world = world
        self.speed = 6
        self.center_x = player.center_x                
        self.center_y = player.center_y
        self.hitted_enemy = None
        self.enemy_list = enemy_list
        if(lane > 2):
            self.direction = 1
            self.center_x = player.center_x + 40 
        else:
            self.direction = -1
            self.angle = 180
            self.center_x = player.center_x - 40
            
    def check_enemy(self):
        for enemy in self.enemy_list:
            if(arcade.geometry.check_for_collision(self, enemy)):
                return enemy
        return None

    def update(self):
        self.center_x += self.speed * self.direction
        self.hitted_enemy = self.check_enemy()
        if(self.center_x > SCREEN_WIDTH + 60 or self.center_x < -60):
            self.world.bullet_list.remove(self)
        elif(self.hitted_enemy != None):
            self.world.enemy_dead(self.hitted_enemy)
            self.collision_list = []
            self.world.bullet_list.remove(self)

