import pygame
import sys
pygame.init()


WIDTH, HEIGHT = 500, 500


class Wall:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))

    def draw(self):
        screen.blit(self.img, self.rect)


class Enemy:
    def __init__(self, x, y, w, h, img, speed, p1, p2, orient):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.speed = speed
        self.orient = orient
        self.p1 = p1
        self.p2 = p2


    def move(self):
        if self.orient == 'h':
            self.rect.x += self.speed
            if self.rect.x >= self.p2 or self.rect.x <= self.p1:
                self.speed *= -1

        else:
            self.rect.y += self.speed
            if self.rect.y >= self.p2 or self.rect.y <= self.p1:
                self.speed *= -1

    def draw(self):
        screen.blit(self.img, self.rect)


class Player:
    def __init__(self, x, y, w, h, img_path, walls):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w , h))
        self.x_speed = 0
        self.y_speed = 0
        self.walls = walls



    def collide(self, obj):
        return self.rect.colliderect(obj.rect)



    def move(self):
        self.rect.x += self.x_speed
        for wall in self.walls:
            if self.collide(wall):
                self.rect.x -= self.x_speed


        self.rect.y += self.y_speed
        for wall in self.walls:
            if self.collide(wall):
                self.rect.y -= self.y_speed




    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))



walls = []
with open('map.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                walls.append(Wall(col * 25, row * 25, 25, 25, "camen.png"))
                print(row, col)
            col += 1
        row += 1

walls2 = []
with open('map2.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                walls2.append(Wall(col * 25, row * 25, 25, 25, "nezer.png"))
                print(row, col)
            col += 1
        row += 1


walls3 = []
with open('map3.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                walls3.append(Wall(col * 25, row * 25, 25, 25, "cirpich.png"))
                print(row, col)
            col += 1
        row += 1


walls4 = []
with open('map4.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                walls4.append(Wall(col * 25, row * 25, 25, 25, "endstone.png"))
                print(row, col)
            col += 1
        row += 1

        
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player(30, 30 , 25, 25, "steve.png" , walls)

#0-й уровень
player90 = Player(114, 60 , 272, 44, "logo.png", walls)

player00 = Player(75, 359 , 66, 66, "steve.png", walls)
player01 = Player(146, 359 , 66, 66, "alex.jpg", walls)
player02 = Player(217, 359 , 66, 66, "villager.png", walls)
player03 = Player(288, 359 , 66, 66, "cow.jpg", walls)
player004 = Player(359, 359 , 66, 66, "pig.png", walls)

fon0 = Player(0,0 , 500 , 500, "house.jpg", walls)

#1-й уровень

fon1 = Player(0,0 , 500 , 500, "cave.jpg", walls)

enemy = Enemy(200, 100, 25, 25, 'zomby.png', 4, 30, 200, 'v')
enemy2 = Enemy(100, 350, 25, 25, 'zomby.png', 3, 350, 450, 'v')
enemy3 = Enemy(375, 300, 25, 25, 'zomby.png', 2, 375, 450, 'h')#горизонталь
enemy4 = Enemy(25, 250, 25, 25, 'zomby.png', 5, 25, 300, 'h')#горизонталь
player11 = Player(428, 403 , 50 , 70, "ad.webp", walls)

#2-й уровень

fon2 = Player(-1150,-290 , 1920 , 1080, "nezer.webp", walls)

enemy21 =  Enemy(100, 50, 25, 25, 'blaze.jpg', 3, 100, 200, 'h')
enemy22 =  Enemy(250, 75, 25, 25, 'blaze.jpg', 2, 250, 300, 'h')
enemy23 =  Enemy(250, 200, 25, 25, 'blaze.jpg', 2, 250, 300, 'h')
enemy24 =  Enemy(350, 125, 25, 25, 'blaze.jpg', 3, 350, 450, 'h')
enemy25 =  Enemy(350, 275, 25, 25, 'blaze.jpg', 3, 350, 450, 'h')
enemy26 =  Enemy(350, 375, 25, 25, 'blaze.jpg', 3, 350, 450, 'h')
enemy27 =  Enemy(75, 300, 25, 25, 'blaze.jpg', 3, 75, 200, 'h')
enemy28 =  Enemy(50, 220, 25, 25, 'blaze.jpg', 1, 100, 225, 'v')
enemy29 =  Enemy(25, 100, 25, 25, 'blaze.jpg', 1, 100, 225, 'v')
enemy210 = Enemy(175, 75, 25, 25, 'blaze.jpg', 1, 75, 225, 'v')
enemy211 = Enemy(200, 200, 25, 25, 'blaze.jpg', 1, 75, 225, 'v')
player2 = Player(390, 25 , 50 , 70, "ad.webp", walls)

#3-й уровень

fon3 = Player(0,0 , 500 , 500, "crep.jpg", walls)

enemy31 =  Enemy(100, 25, 25, 25, 'skelet.png', 2, 25, 100, 'v')
enemy32 =  Enemy(300, 25, 25, 25, 'skelet.png', 2, 25, 100, 'v')
enemy33 =  Enemy(325, 125, 25, 25, 'skelet.png', 3, 325, 420, 'h')#горизонталь
enemy34 =  Enemy(176, 100, 25, 25, 'skelet.png', 2, 175, 325, 'h')
enemy35 =  Enemy(25, 125, 25, 25, 'skelet.png', 3, 25, 140, 'h')
enemy36 =  Enemy(75, 175, 25, 25, 'skelet.png', 3, 75, 400, 'h')
enemy37 =  Enemy(450, 449, 25, 25, 'skelet.png', 2, 275, 450, 'v')
enemy38 =  Enemy(400, 275, 25, 25, 'skelet.png', 2, 275, 450, 'v')
enemy39 =  Enemy(200, 400, 25, 25, 'skelet.png', 2, 200, 250, 'h')
enemy310 = Enemy(200, 300, 25, 25, 'skelet.png', 3, 300, 425, 'v')
enemy311 = Enemy(50, 250, 25, 25, 'skelet.png', 1, 250, 375, 'v')
player4 = Player( 39, 415 , 50 , 50, "end.png", walls)

#4-й уровень

fon4 = Player(0,0 , 500 , 500, "TheEnd.webp", walls)

enemy41 =  Enemy(50, 225, 25, 25, 'enderman.jpg', 2, 225, 325, 'v')
enemy42 =  Enemy(100, 300, 25, 25, 'enderman.jpg', 1, 75, 175, 'h')
enemy43 =  Enemy(25, 425, 25, 25, 'enderman.jpg', 1, 25, 75, 'h')#горизонталь
enemy44 =  Enemy(125, 75, 25, 25, 'enderman.jpg', 1, 125, 175, 'h')
enemy45 =  Enemy(127, 125, 25, 25, 'enderman.jpg', 1,125, 175, 'h')
enemy46 =  Enemy(25, 75, 25, 25, 'enderman.jpg', 1, 25, 75, 'h')
enemy47 =  Enemy(30, 125, 25, 25, 'enderman.jpg', 1, 25, 75, 'h')
enemy48 =  Enemy(300, 175, 25, 25, 'enderman.jpg', 1, 300, 450, 'h')
enemy49 =  Enemy(449, 100, 25, 25, 'enderman.jpg', 1, 300, 450, 'h')
enemy410 = Enemy(300, 50, 25, 25, 'enderman.jpg', 1, 300, 400, 'h')
enemy411 = Enemy(399, 25, 25, 25, 'enderman.jpg', 1, 300, 400, 'h')
enemy412 =  Enemy(300, 300, 25, 25, 'enderman.jpg', 2, 300, 450, 'v')
enemy413 = Enemy(375, 350, 25, 25, 'enderman.jpg', 2, 375, 450, 'h')
enemy414 = Enemy(453, 400, 25, 25, 'enderman.jpg', 2, 375, 450, 'h')

cristal1 = Enemy(155, 420, 40, 40, 'cristal.png', 0, 155, 155, 'h')
cristal2 = Enemy(55, 155, 40, 40, 'cristal.png', 0, 55, 55, 'h')
cristal3 = Enemy(430, 30, 40, 40, 'cristal.png', 0, 430, 430, 'h')
cristal4 = Enemy(430, 305, 40, 40, 'cristal.png', 0, 305, 405, 'h')

player04 = Player(-225, -225 , 50 , 50, "endport.webp", walls)

#5-й уровень

player5 = Player(-198, 0 , 896 , 504, "titr.jpg", walls)


boss = 0



gamestate = 0

while True:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                player.x_speed = -5
            elif e.key == pygame.K_RIGHT:
                player.x_speed = 5
            elif e.key == pygame.K_UP:
                player.y_speed = -5
            elif e.key == pygame.K_DOWN:
                player.y_speed = 5
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                player.x_speed = 0
            elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                player.y_speed = 0
    
    if gamestate == 0:          #Типо выбор персонажа
        fon0.draw()
        player90.draw()
        player00.draw()
        player01.draw()
        player02.draw()
        player03.draw()
        player004.draw()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if player00.rect.x < x < player00.rect.right and player00.rect.y < y < player00.rect.bottom:
                    player = Player(30, 30 , 25, 25, "steve.png", walls)                        
                    gamestate = 1
                if player01.rect.x < x < player01.rect.right and player01.rect.y < y < player01.rect.bottom:
                    player = Player(30, 30 , 25, 25, "alex.jpg", walls)
                    gamestate = 1
                if player02.rect.x < x < player02.rect.right and player02.rect.y < y < player02.rect.bottom:
                    player = Player(30, 30 , 25, 25, "villager.png", walls)                
                    gamestate = 1
                if player03.rect.x < x < player03.rect.right and player03.rect.y < y < player03.rect.bottom:
                    player = Player(30, 30 , 25, 25, "cow.jpg", walls)
                    gamestate = 1
                if player004.rect.x < x < player004.rect.right and player04.rect.y < y < player004.rect.bottom:
                    player = Player(30, 30 , 25, 25, "pig.png", walls)
                    gamestate = 1


    if gamestate == 1:         #Типо пещера 
        fon1.draw()        
        player.move()
        enemy.move()
        enemy2.move()
        enemy3.move()
        enemy4.move()

        player.draw()
        enemy.draw()
        enemy2.draw()
        enemy3.draw()
        enemy4.draw()
        player11.draw()

        player.walls = walls
        for wall in walls:
            wall.draw()
        if player.collide(enemy) or player.collide(enemy2) or player.collide(enemy3) or player.collide(enemy4):
            player.rect.x  = 30
            player.rect.y  = 30
            




        if player.collide(player11):
            player.rect.x = 50
            player.rect.y = 30
            gamestate = 2

    if gamestate == 2:        #Типо ад
        fon2.draw()
        player.move()
        enemy21.move()
        enemy22.move()
        enemy23.move()
        enemy24.move()
        enemy25.move()
        enemy26.move()
        enemy27.move()
        enemy28.move()
        enemy29.move()
        enemy210.move()
        enemy211.move()


        player.draw()
        enemy21.draw()
        enemy22.draw()
        enemy23.draw()
        enemy24.draw()
        enemy25.draw()
        enemy26.draw()
        enemy27.draw()
        enemy28.draw()
        enemy29.draw()
        enemy210.draw()
        enemy211.draw()

        player2.draw()   
        player.walls = walls2
        for wall in walls2:
            wall.draw()
        if player.collide(enemy21) or player.collide(enemy22) or player.collide(enemy23) or player.collide(enemy24) or player.collide(enemy25) or player.collide(enemy26) or player.collide(enemy27) or player.collide(enemy28) or player.collide(enemy29) or player.collide(enemy210) or player.collide(enemy211):
            player.rect.x  = 30
            player.rect.y  = 30




        player.walls = walls2
        for wall in walls2:
            wall.draw()
        if player.collide(player2):
            player.rect.x = 50
            player.rect.y = 30

            gamestate = 3


    if gamestate == 3:      #Типо портал в энд
        fon3.draw()
        player.move()
        enemy31.move()
        enemy32.move()
        enemy33.move()
        enemy34.move()
        enemy35.move()
        enemy36.move()
        enemy37.move()
        enemy38.move()
        enemy39.move()
        enemy310.move()
        enemy311.move()


        player.draw()
        enemy31.draw()
        enemy32.draw()
        enemy33.draw()
        enemy34.draw()
        enemy35.draw()
        enemy36.draw()
        enemy37.draw()
        enemy38.draw()
        enemy39.draw()
        enemy310.draw()
        enemy311.draw()
        player.draw()
        player4.draw()        
        player.walls = walls3
        for wall in walls3:
            wall.draw()

        if player.collide(enemy31) or player.collide(enemy32) or player.collide(enemy33) or player.collide(enemy34) or player.collide(enemy35) or player.collide(enemy36) or player.collide(enemy37) or player.collide(enemy38) or player.collide(enemy39) or player.collide(enemy310) or player.collide(enemy311):
            player.rect.x  = 30
            player.rect.y  = 30

        if player.collide(player4):
            gamestate = 4
            player.rect.x = 225
            player.rect.y = 225

    if gamestate == 4:      #Типо битва с боссом
        boss = 0
        fon4.draw()
        player.move()
        enemy41.move()
        enemy42.move()
        enemy43.move()
        enemy44.move()
        enemy45.move()
        enemy46.move()
        enemy47.move()
        enemy48.move()
        enemy49.move()
        enemy410.move()
        enemy411.move()
        enemy412.move()
        enemy413.move()
        enemy414.move()

        player04.draw()
        cristal1.draw()
        cristal2.draw()
        cristal3.draw()
        cristal4.draw()        
        player.draw()
        enemy41.draw()
        enemy42.draw()
        enemy43.draw()
        enemy44.draw()
        enemy45.draw()
        enemy46.draw()
        enemy47.draw()
        enemy48.draw()
        enemy49.draw()
        enemy410.draw()
        enemy411.draw()
        enemy412.draw()
        enemy413.draw()
        enemy414.draw()
        player.draw()

        player.walls = walls4
        for wall in walls4:
            wall.draw()

        if player.collide(enemy41) or player.collide(enemy42) or player.collide(enemy43) or player.collide(enemy44) or player.collide(enemy45) or player.collide(enemy46) or player.collide(enemy47) or player.collide(enemy48) or player.collide(enemy49) or player.collide(enemy410) or player.collide(enemy411) or player.collide(enemy412) or player.collide(enemy413) or player.collide(enemy414):
            player.rect.x = 225
            player.rect.y = 225
            boss = 0
            cristal1.rect.x = 155
            cristal1.rect.y = 420
            cristal2.rect.x = 55
            cristal2.rect.y = 155
            cristal3.rect.x = 430
            cristal3.rect.y = 30
            cristal4.rect.x = 430
            cristal4.rect.y = 305
            player04.rect.x = -225
            player04.rect.y = -225



        if player.collide(cristal1):
            cristal1.rect.x = 600
            cristal1.rect.y = 600
            boss +=1
        if player.collide(cristal2):
            cristal2.rect.x = 600
            cristal2.rect.y = 600
            boss +=1        
        if player.collide(cristal3):
            cristal3.rect.x = 600
            cristal3.rect.y = 600
            boss +=1
        if player.collide(cristal4):
            cristal4.rect.x = 600
            cristal4.rect.y = 600
            boss +=1
        if boss == 4:
            player04.rect.x = 225
            player04.rect.y = 225
        if player.collide(player04):
            gamestate = 5

        
    if gamestate == 5:    #Типо титры пойдут
        player5.draw()



    pygame.display.update()
    clock.tick(60)