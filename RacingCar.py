import random
import math
import pygame, sys
import time

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((798, 600))
pygame.display.set_caption('Car Racing Game')
icon = pygame.image.load('images/logo.jpeg')
pygame.display.set_icon(icon)


def countdown():
    font2 = pygame.font.Font('freesansbold.ttf', 85)
    countdownBackground = pygame.image.load('images/bg.png')
    three = font2.render('3', True, (187, 30, 16))
    two = font2.render('2', True, (255, 255, 0))
    one = font2.render('1', True, (51, 165, 50))
    go = font2.render('GO!!!', True, (0, 255, 0))

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()

    screen.blit(three, (350, 250))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    screen.blit(two, (350, 250))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    screen.blit(one, (350, 250))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    screen.blit(go, (350, 250))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdownBackground, (0, 0))
    pygame.display.update()
    time.sleep(1)
    gameloop()
    pygame.display.update()


def gameloop():
    #####MUSIC#####
    pygame.mixer.music.load('images/BackgroundMusic.mp3')
    pygame.mixer.music.play()
    #####COLLISION SOUND####
    crash_sound = pygame.mixer.Sound('images/car_crash.wav')

    #####SCORING PART####
    score_value = 0
    font1 = pygame.font.Font("freesansbold.ttf", 25)

    def show_score(x, y):
        score = font1.render("SCORE: " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

    ###HIGH SCORE PART###
    with open('images/highscore.txt', 'r') as f:
        highscore = f.read()

    def show_highscore(x, y):
        Highscore_txt = font1.render('High Score:' + str(highscore), True, (255, 0, 0))
        screen.blit(Highscore_txt, (x, y))
        pygame.display.update()

    ###GAME OVER FUNCTION###
    def gameover(x, y):
        gameover_img = pygame.image.load('images/gameover.png')
        run = True
        while run:
            screen.blit(gameover_img, (x, y))
            time.sleep(0.5)
            show_score(330, 400)
            time.sleep(0.5)
            show_highscore(330, 450)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        countdown()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    ###Background Image###
    background = pygame.image.load('images/bg.png')

    main_car = pygame.image.load('images/car.png')
    main_carX = 350
    main_carY = 495
    main_carX_change = 0
    main_carY_change = 0

    car1 = pygame.image.load('images/car1.jpeg')
    car1X = random.randint(178, 490)
    car1Y = 100
    car1Ychange = 3

    car2 = pygame.image.load('images/car2.png')
    car2X = random.randint(178, 490)
    car2Y = 100
    car2Ycahnge = 3

    car3 = pygame.image.load('images/car3.png')
    car3X = random.randint(178, 490)
    car3Y = 100
    car3Ychange = 3

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    main_carX_change += 5
                if event.key == pygame.K_LEFT:
                    main_carX_change -= 5
                if event.key == pygame.K_UP:
                    main_carY_change -= 5
                if event.key == pygame.K_DOWN:
                    main_carY_change += 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    main_carX_change = 0
                if event.key == pygame.K_LEFT:
                    main_carX_change = 0
                if event.key == pygame.K_UP:
                    main_carY_change = 0
                if event.key == pygame.K_DOWN:
                    main_carY_change = 0

        if main_carX < 178:
            main_carX = 178
        if main_carX > 490:
            main_carX = 490
        if main_carY < 0:
            main_carY = 0
        if main_carY > 495:
            main_carY = 495

        # RGB
        screen.fill((0, 0, 0))

        ##BACKGROUND IMAGE##
        screen.blit(background, (0, 0))

        ###MAIN CAR DISPLAYING##
        screen.blit(main_car, (main_carX, main_carY))

        ##OTHER CARS DISPLAYING##
        screen.blit(car1, (car1X, car1Y))
        screen.blit(car2, (car2X, car2Y))
        screen.blit(car3, (car3X, car3Y))

        ##SHOW SCORE FUNTION
        show_score(570, 280)

        # HIGH SCORE FUNTION
        show_highscore(0, 0)

        # MAIN CAR UPDATING VALUES
        main_carX += main_carX_change
        main_carY += main_carY_change

        # OTHER CARS MOVEMENTS
        car1Y += car1Ychange
        car2Y += car2Ycahnge
        car3Y += car3Ychange

        # car1Y += 2
        # car2Y += 2
        # car3Y += 2

        # OTHER CARS INFINITELY MOVEMENTS
        if car1Y > 670:
            car1Y = -100
            car1X = random.randint(178, 490)
            score_value += 5
        if car2Y > 670:
            car2Y = -150
            car2X = random.randint(178, 490)
            score_value += 5
        if car3Y > 670:
            car3Y = -200
            car3X = random.randint(178, 490)
            score_value += 5

        # CHECKING IF HIGH SCORE HAS BEEN CREATED
        if score_value > int(highscore):
            highscore = score_value

            ###DETECTING COLLISIONS BETWEEN THE CARS

        # DISTANCE BETWEEN CAR1 and MAINCAR
        def iscollision1(car1X, car1Y, main_carX, main_carY):
            distance = math.sqrt(math.pow(car1X - main_carX, 2) + math.pow(car1Y - main_carY, 2))
            # If DISTANCE is SMALLER THAN 50 affter then Collision will Occur
            if distance < 50:
                return True
            else:
                return False

        # DISTANCE BETWEEN CAR2 and MAINCAR
        def iscollision2(car2X, car2Y, main_carX, main_carY):
            distance = math.sqrt(math.pow(car2X - main_carX, 2) + math.pow(car2Y - main_carY, 2))
            # If DISTANCE is SMALLER THAN 50 affter then Collision will Occur
            if distance < 50:
                return True
            else:
                return False

        # DISTANCE BETWEEN CAR3 and MAINCAR
        def iscollision3(car3X, car3Y, main_carX, main_carY):
            distance = math.sqrt(math.pow(car3X - main_carX, 2) + math.pow(car3Y - main_carY, 2))
            # If DISTANCE is SMALLER THAN 50 affter then Collision will Occur
            if distance < 50:
                return True
            else:
                return False

            # Giving COLLISION VARIABLE#

        # COLLISIN BETWEEN MAINCAR and Other CARS
        coll1 = iscollision1(car1X, car1Y, main_carX, main_carY)
        coll2 = iscollision2(car2X, car2Y, main_carX, main_carY)
        coll3 = iscollision3(car3X, car3Y, main_carX, main_carY)

        # IF COLLISION Occur
        if coll1:
            screen.fill((255, 0, 0))
            car1Ychange = 0
            car2Ycahnge = 0
            car3Ychange = 0
            main_carX_change = 0
            main_carY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
            time.sleep(1)
            gameover(0, 0)

        if coll2:
            screen.fill((255, 0, 0))
            car1Ychange = 0
            car2Ycahnge = 0
            car3Ychange = 0
            main_carX_change = 0
            main_carY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
            time.sleep(1)
            gameover(0, 0)

        if coll3:
            screen.fill((255, 0, 0))
            car1Ychange = 0
            car2Ycahnge = 0
            car3Ychange = 0
            main_carX_change = 0
            main_carY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
            time.sleep(1)
            gameover(0, 0)

        if car1Ychange == 0 and car2Ycahnge == 0 and car3Ychange == 0:
            pass

        # show_score(570, 280)
        # show_highscore(0, 0)
        ##WRITING HIGH SCORE TEXT FILE
        with open('images/highscore.txt', 'w') as f:
            f.write(str(highscore))

        pygame.display.update()


countdown()
