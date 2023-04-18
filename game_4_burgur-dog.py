import pygame,random
 

#initialize pygame
pygame.init()

#create a display surface and set its caption
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Burger Dog")


# define a clock to slow down the while loop and make sure it runs at the same speed on every single computer (FPS = frame per second)
FPS  = 60
clock = pygame.time.Clock()
#VELOCITY = 10 it runs 10 times a second


#set game values
PLAYER_STARTING_LIVES = 4
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTER_BURGER_VELOCITY = 3
BURGER_ACCELERATION = .25
BUFFER_DISTANCE = 100

score = 0
burger_points = 0
burger_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY

boost_level = STARTING_BOOST_LEVEL

burger_velocity = STARTER_BURGER_VELOCITY


#colors
ORANGE = (246,175,54)
WHITE = (255,255,255)
BLACK = (0,0,0)

#set fonts
font = pygame.font.Font("WashYourHand.ttf", 32)

#set text 
title_text = font.render("Burger Dog", True, ORANGE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.centery = 10

score_text = font.render("Score: "+ str(score), True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

points_text = font.render("Points: "+str(burger_points), True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft= (10, 10)

eaten_text = font.render("Burgers eaten: : "+str(burger_eaten), True, ORANGE)
eaten_rect = eaten_text.get_rect()
eaten_rect.centerx = WINDOW_WIDTH//2
eaten_rect.y = 50

lives_text = font.render("Lives: "+str(player_lives), True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10 , 10)

boost_text = font.render("Boost: "+str(boost_level), True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 10 , 50)

game_over_text = font.render("Game Over!", True, ORANGE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2 , WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to continue!", True, ORANGE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2 , WINDOW_HEIGHT//2+ 60)

#set music
bark_sound = pygame.mixer.Sound("bark_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.music.load("bd_background_music.wav")

#set images
player_image_right = pygame.image.load("dog_right.png")
player_image_left = pygame.image.load("dog_left.png")
player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.center =(WINDOW_WIDTH//2 , WINDOW_HEIGHT//2)

burger_image = pygame.image.load("burger.png")
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH-32), -100)


#the main game loop
pygame.mixer.music.play()
running = True
while running:
    #lopp through a list of ecents 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False 
           
           
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = player_image_left
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_velocity
        player_image = player_image_right
    if keys[pygame.K_UP] and player_rect.top > 100:
        player_rect.y -= player_velocity
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity
        
    #engage boost
    if keys[pygame.K_SPACE] and boost_level >0:
        player_velocity = PLAYER_BOOST_VELOCITY
        boost_level -= 1
    else:
        boost_level = PLAYER_NORMAL_VELOCITY

    #move the burger and update the burger points
    burger_rect.y += burger_velocity
    
    #the faster the burger moves the more points it  worths
    burger_points = int(burger_velocity * (WINDOW_HEIGHT - burger_rect.y + 100))
    
    # player missed the burger
    if burger_rect.y > WINDOW_HEIGHT:
        player_lives -= 1
        miss_sound.play()
        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH-32), -BUFFER_DISTANCE)
        burger_velocity = STARTER_BURGER_VELOCITY
        
        player_rect.centerx = WINDOW_WIDTH//2
        player_rect.bottom =WINDOW_HEIGHT
        boost_level = STARTING_BOOST_LEVEL
        
    if player_rect.colliderect(burger_rect):
        score += burger_points
        burger_eaten += 1
        bark_sound.play()
        
        #relocate the player
        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH-32), -BUFFER_DISTANCE)
        burger_velocity += BURGER_ACCELERATION
        
        boost_level += 25
        if boost_level >STARTING_BOOST_LEVEL:
            boost_level = STARTING_BOOST_LEVEL
            
        
        
    # fill the surface
    display_surface.fill(BLACK)
    
    #update HUD
    score_text = font.render("Score: "+ str(score), True, ORANGE)
    points_text = font.render("Points: "+str(burger_points), True, ORANGE)
    eaten_text = font.render("Burgers eaten: : "+str(burger_eaten), True, ORANGE)
    boost_text = font.render("Boost: "+str(boost_level), True, ORANGE)
    lives_text = font.render("Lives: "+str(player_lives), True, ORANGE)
    
    if player_lives == 0:
            score_text = font.render("Score: "+ str(score), True, ORANGE)
            display_surface.blit(game_over_text, game_over_rect)
            display_surface.blit(continue_text, continue_rect)
            pygame.display.update()
            
            #pause the game until player presses a key and reset the game
            pygame.mixer.music.stop()
            is_paused = True
            while is_paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        score = 0
                        player_lives = PLAYER_STARTING_LIVES
                        burger_eaten = 0
                        boost_level = STARTING_BOOST_LEVEL
                        burger_velocity = STARTER_BURGER_VELOCITY
                        pygame.mixer.music.play(-1, 0.0)
                        is_paused = False
                    #the player wants to quit
                    if event.type == pygame.QUIT:
                        is_paused = False
                        running = False 
    
    #blit HUD
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)
    display_surface.blit(eaten_text, eaten_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(points_text, points_rect)
    pygame.draw.line(display_surface, WHITE, (0,100), (WINDOW_WIDTH,100), 3)
    
    #blit assets
    display_surface.blit(player_image, player_rect)
    display_surface.blit(burger_image, burger_rect)
        
    #update the display
    pygame.display.update()
    
    #tick the clock
    clock.tick(FPS)

           
# end the  game
pygame.quit()
