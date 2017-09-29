import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

    arcade.set_background_color(arcade.color.BLACK)


def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == '__main__':
    main()