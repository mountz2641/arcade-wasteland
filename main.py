import arcade
from player import Player

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.sprite_list = []
        arcade.set_background_color(arcade.color.BLACK)

        #set player up
        self.player = Player('./image/cowboy.png', 0.1)
        self.player.setup(self, width // 2 - 25, height // 2 + 50)
        self.sprite_list.append(self.player)

    def on_key_press(self, key, key_modifiers):
        if(key == arcade.key.UP):
            if(self.player.location != 2 and self.player.location != 5):
                self.player.walk('up')
        elif(key == arcade.key.DOWN):
            if(self.player.location != 0 and self.player.location != 3):
                self.player.walk('down')
        elif(key == arcade.key.LEFT):
            if(self.player.location > 2):
                self.player.walk('left')
        elif(key == arcade.key.RIGHT):
            if(self.player.location <= 2):
                self.player.walk('right')

    def update(self, delta):
        pass

    def on_draw(self):
        arcade.start_render()
        for sprite in self.sprite_list:
            sprite.draw()


def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
    main()