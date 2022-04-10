from typing import KeysView
from pygame import *

w = 1920
h = 1080

img_back = "back.jpg"
img_player = 'player.png'
img_ball = 'ball.png'

life_1 = 3
life_2 = 3
tik_took_1 = 0
tik_took_2 = 0

display.set_caption("ping pong")
window = display.set_mode((w, h))
background = transform.scale(image.load(img_back), (w, h))

class GameSprite(sprite.Sprite):  
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed): 
        
        sprite.Sprite.__init__(self) 
     
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed 
     
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
        
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_LEFT] and self.rect.y > 0: 
            self.rect.y -= self.speed 
        if keys[K_RIGHT] and self.rect.y < 660: 
            self.rect.y += self.speed 

player2 = Player(img_player, 100, 335, 70, 360, 5)

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background,(0,0))
        
        player2.update()

        player2.reset()

        display.update()
time.delay(50)