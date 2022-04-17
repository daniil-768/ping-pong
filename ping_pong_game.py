from typing import KeysView
from pygame import *

w = 1600
h = 900

img_back = "back.jpg"
img_player = 'player.png'
img_ball = 'ball.png'

life_1 = 3
life_2 = 3
tik_took_1 = 0
tik_took_2 = 0
speed_x = 10
speed_y = 10
speed = 5

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

class Player2(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 0: 
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 660: 
            self.rect.y += self.speed



player2 = Player(img_player, 100, 335, 70, 360, 10)
player1 = Player2(img_player, 1500, 335, 70, 360, 10)
ball = GameSprite(img_ball, 810, 540, 70, 50, speed)



finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if sprite.collide_rect(player1, ball):
        speed_x *= -1
        tik_took_1 += 1

    if sprite.collide_rect(player2, ball):
        speed_x *= -1
        tik_took_2 += 1

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y == 800:
        speed_y *= -1

    if ball.rect.y == 100:
        speed_y *= -1

    if not finish:
        window.blit(background,(0,0))
        
        player2.update()
        player1.update()
        ball.update()

        player2.reset()
        player1.reset()
        ball.reset()

        display.update()
time.delay(50)