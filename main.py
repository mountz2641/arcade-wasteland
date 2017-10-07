import arcade
from player import Player
from enemy import Enemy
from wall import Wall
from bullet import Bullet
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.time = 0
        self.spawn_rate = 10;
        
        self.sprite_list = []
        self.enemy_list = []
        self.wall_list = []
        self.bullet_list = []
        self.gun = None
        self.level = 1

        arcade.set_background_color(arcade.color.BLACK)

        #set player up
        self.player = Player('./image/cowboy.png', 0.1)
        self.player.setup(self, width // 2 - 25, height // 2 + 50, self.enemy_list)
        self.sprite_list.append(self.player)

        #construct 6 wall
        for lane in range (0, 6):
            self.wall = Wall('./image/wall.png', 1)
            self.wall.setup(self, lane)
            self.wall_list.append(self.wall)

    def on_key_press(self, key, key_modifiers):
        #player movement
        if(key == arcade.key.UP):
            if(self.player.lane != 2 and self.player.lane != 5):
                self.player.walk(DIR_UP)
        elif(key == arcade.key.DOWN):
            if(self.player.lane != 0 and self.player.lane != 3):
                self.player.walk(DIR_DOWN)
        elif(key == arcade.key.LEFT):
            if(self.player.lane > 2):
                self.player.walk(DIR_LEFT)
        elif(key == arcade.key.RIGHT):
            if(self.player.lane <= 2):
                self.player.walk(DIR_RIGHT)
        
        #player action
        if(key == arcade.key.SPACE):
            self.player.action()
        elif(key == arcade.key.R):
                self.gun.reload_gun()

    def update(self, delta):
        print('delta time is: %f'%(delta))
        self.spawn_enemy(delta)
        self.gun.update(delta)
        for enemy in self.enemy_list:
            if(arcade.geometry.check_for_collision(enemy, self.wall_list[enemy.lane])):
                self.wall_list[enemy.lane].getDamage(enemy.damage)
                self.enemy_list.remove(enemy)
        for enemy in self.enemy_list:
            enemy.update()
        for bullet in self.bullet_list:
            bullet.update()
        self.score_text = arcade.create_text('Level: ' + str(self.level) + '\nScore: ' + str(self.player.score), 
                                                arcade.color.WHITE, 30, align="center", anchor_x="center", anchor_y="center")
        

    def spawn_enemy(self, delta):
        self.time += delta
        if(self.time > 0.4):
            self.time -= 0.4
            if(randint(0,10) <= self.spawn_rate):
                self.new_enemy = Enemy('./image/zombie.png', 0.2)
                self.new_enemy.setup(self, randint(0,5))
                self.enemy_list.append(self.new_enemy)

    def enemy_dead(self, enemy):
        self.enemy_list.remove(enemy)

    def increase_level(self):
        self.level += 1
        self.spawn_rate += 5
        if(self.level > 10):
            self.game_win()


    def on_draw(self):
        arcade.start_render()
        for enemy in self.enemy_list:
            enemy.draw()
        for wall in self.wall_list:
            wall.draw()
        for bullet in self.bullet_list:
            bullet.draw()
        for sprite in self.sprite_list:
            sprite.draw()
        arcade.render_text(self.gun.ammo_text,900,100)
        arcade.render_text(self.score_text, 500, 100)


def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()