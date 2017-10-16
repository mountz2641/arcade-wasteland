import arcade

LANE_SIZE = 100
RELOAD_TIME = 0.75

class Gun(arcade.Sprite):
    def setup(self, player, world, lane):
        self.player = player
        self.world = world
        self.gun_left = arcade.load_texture('./image/revolver_left.png',scale = 0.7)
        self.gun_right = arcade.load_texture('./image/revolver_right.png',scale = 0.7)
        self.texture = self.gun_left
        self.center_x = player.center_x - 30
        self.center_y = player.center_y
        self.ammo = 6
        self.max_ammo = 6
        self.isReload = False
        self.wait = 0

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

    def update(self,delta):
        if(self.isReload):
            self.wait += delta
            if(self.wait > RELOAD_TIME):
                self.ammo = 6
                self.isReload = False
                self.wait = 0
        self.ammo_text = arcade.create_text("Ammo: " + str(self.ammo) + " / " + str(self.max_ammo), arcade.color.WHITE, 25, 
                                            align="center", anchor_x="center", anchor_y="center")

    def reload_gun(self):
        self.isReload = True

    def shoot(self):
        if(self.isReload):
            return False
        else:
            self.ammo -= 1
            if(self.ammo <= 0):
                self.reload_gun()
        return True    


        
        
        
