import arcade
from player import Player
from enemy import Enemy
from wall import Wall
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.time = 0
        self.spawn_rate = 2;
        
        self.sprite_list = []
        self.enemy_list = []
        self.wall_list = []

        arcade.set_background_color(arcade.color.BLACK)

        #set player up
        self.player = Player('./image/cowboy.png', 0.1)
        self.player.setup(self, width // 2 - 25, height // 2 + 50)
        self.sprite_list.append(self.player)

        #construct 6 wall
        for lane in range (0, 6):
            self.wall = Wall('./image/wall.png', 1)
            self.wall.setup(self, lane)
            self.wall_list.append(self.wall)

    def on_key_press(self, key, key_modifiers):
        if(key == arcade.key.UP):
            if(self.player.lane != 2 and self.player.lane != 5):
                self.player.walk('up')
        elif(key == arcade.key.DOWN):
            if(self.player.lane != 0 and self.player.lane != 3):
                self.player.walk('down')
        elif(key == arcade.key.LEFT):
            if(self.player.lane > 2):
                self.player.walk('left')
        elif(key == arcade.key.RIGHT):
            if(self.player.lane <= 2):
                self.player.walk('right')

    def update(self, delta):
        self.spawn_monster(delta)
        for enemy in self.enemy_list:
            if(arcade.geometry.check_for_collision(enemy, self.wall_list[enemy.lane])):
                self.wall_list[enemy.lane].getDamage(enemy.damage)
                self.enemy_list.remove(enemy)
        for enemy in self.enemy_list:
            enemy.update()

    def spawn_monster(self, delta):
        self.time += delta
        if(self.time < 0.5):
            return
        self.time -= 0.5
        if(randint(0,10) <= self.spawn_rate):
            self.new_enemy = Enemy('./image/zombie.png', 0.2)
            self.new_enemy.setup(self, randint(0,5))
            self.enemy_list.append(self.new_enemy)

    def on_draw(self):
        arcade.start_render()
        for sprite in self.sprite_list:
            sprite.draw()
        for enemy in self.enemy_list:
            enemy.draw()
        for wall in self.wall_list:
            wall.draw()


def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()