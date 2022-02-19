from pygame import*
from random import randint

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

img_back = 'galaxy.jpg'
img_hero = 'rocker.png'



win_width = 700
win_height = 500
display.set_caption('Shooter')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
    
lost = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost

        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed

        if self.rect.y < 0:
            self.kill()



font.init()
font2 = font.SysFont('Arial', 36)

rocket = Player('rocket.png', 310, 350, 80, 110, 10)
ship = Enemy('ufo.png', randint(5, 500), 5, 70, 50, 4)


monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1,5))
    monsters.add(monster)

bullets = sprite.Group()

finish = False
clock = time.Clock()
run = True
FPS = 60

score = 0

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                rocket.fire()

    if not finish:
        window.blit(background,(0,0))
        text = font2.render('Cчёт:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render('Пропущенно:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        rocket.update()
        rocket.reset()
        bullets.update()
        bullets.draw(window)
        ship.update()
        ship.reset()
        monsters.update()
        monsters.draw(window)
        display.update()

    time.delay(50)
    clock.tick(FPS)
