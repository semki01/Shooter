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
from pygame import*
from random import randint
from time import time as timer 



#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')

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
font2 = font.SysFont('Tahoma', 45)
win = font2.render('YOU WIN!', True, (255, 255, 255))
lose = font2.render('YOU LOSE', True, (180, 0, 0))

rocket = Player('rocket.png', 310, 350, 80, 110, 10)


monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1,5))
    monsters.add(monster)

bullets = sprite.Group()

asteroids = sprite.Group()
for i in range(1, 3):
    asteroid = Enemy('asteroid.png', randint(80, win_width - 80), -40, 80, 50, randint(1,3))
    asteroids.add(asteroid)

players = sprite.Group()
rocket = Player('rocket.png', 310, 350, 80, 110, 10)
players.add(rocket)
finish = False
clock = time.Clock()
run = True
FPS = 60

score = 0

run = True
rel_time = False

num_fire = 0

xp = 3
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        # событие нажатия на пробел - спрайт стреляет
        elif e.type == KEYDOWN:
            


            if e.key == K_SPACE:
                #fire_sound.play()
                if num_fire < 5 and rel_time == False:
                    num_fire = num_fire + 1
                    rocket.fire()

            if num_fire >= 5 and rel_time == False:

                last_time = timer()
                rel_time = True
                


    xp_text = font2.render('XP:',xp , True, (255, 0, 0))


    if num_fire >= 5 and rel_time == False:

        last_time = timer()
        rel_time = True


    if not finish:

        window.blit(background,(0,0))

        text_lose = font2.render('Пропущенно:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 60))

        window.blit(xp_text, (450, 350))

        text = font2.render('Cчёт:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1,5))
            monsters.add(monster)

        collision = sprite.groupcollide(asteroids, players, True, True)
        for c in collision:
            xp = xp - 1
            asteroid = Enemy('asteroid.png', randint(270, win_width - 80), -40, 80, 50, randint(1,3))
            asteroids.add(asteroid)

        
        if score >= 31:
            text_win = font2.render('YOU WIN!', 1, (0, 255, 0))
            window.blit(text_win, (250, 250))
            finish = True

        if lost >= 3:
            text_lost = font2.render('YOU LOSE!', 1, (255, 0, 0))
            window.blit(text_lost, (250, 250))
            finish = True

        rocket.update()
        rocket.reset()
        bullets.update()
        monsters.update()
        monsters.draw(window)
        asteroids.update()
        asteroids.draw(window)
        bullets.draw(window)

        if rel_time == True:
            now_time = timer()
        
            if now_time - last_time < 3:
                reload = font2.render('Wait, reload...', 1, (255, 0, 0))
                window.blit(reload, (260, 420))
            else:
                num_fire = 0
                rel_time = False


        display.update()

        time.delay(50)
        clock.tick(FPS)
