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
GAME_RUNNING = 10
GAME_OVER = 11
GAME_WIN = 12

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.time = 0
        self.spawn_rate = 45;
        
        self.sprite_list = []
        self.enemy_list = []
        self.wall_list = []
        self.bullet_list = []
        self.gun = None
        self.level = 1
        self.game_stage = GAME_RUNNING
        self.result_text = arcade.create_text("", arcade.color.WHITE, 30, 
                                            align="center", anchor_x="center", anchor_y="center")

        self.background = arcade.load_texture('./image/wasteland_background.png') 

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
        if(self.game_stage != GAME_RUNNING):
            return
        if(key == arcade.key.SPACE):
            self.player.action()
        elif(key == arcade.key.R):
            self.gun.reload_gun()

    def update(self, delta):
        if(self.game_stage != GAME_RUNNING):
            return
        print('delta time is: %f'%(delta))
        self.spawn_enemy(delta)
        self.gun.update(delta)
        for enemy in self.enemy_list:
            if(arcade.geometry.check_for_collision(enemy, self.wall_list[enemy.lane])):
                self.wall_list[enemy.lane].getDamage(enemy.damage)
                self.enemy_list.remove(enemy)
        for enemy in self.enemy_list:
            enemy.update(delta)
        for bullet in self.bullet_list:
            bullet.update(delta)
        self.score_text = arcade.create_text('Level: ' + str(self.level) + '\nScore: ' + str(self.player.score), 
                                                arcade.color.WHITE, 30, align="center", anchor_x="center", anchor_y="center")
        

    def spawn_enemy(self, delta):
        self.time += delta
        if(self.time > 0.4):
            self.time -= 0.4
            if(randint(0,100) <= self.spawn_rate):
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

    def game_win(self):
        self.game_stage = GAME_WIN
        self.result_text = arcade.create_text('YOU WIN', arcade.color.WHITE, 200, align="center", anchor_x="center", anchor_y="center")
        self.enemy_list = []

    def game_over(self):
        self.game_stage = GAME_OVER
        self.result_text = arcade.create_text('YOU DIED', arcade.color.WHITE, 190, align="center", anchor_x="center", anchor_y="center")
        self.player.dead()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
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
        arcade.render_text(self.result_text, 500, 275)

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()