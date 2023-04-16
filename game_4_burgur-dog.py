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
running = True
while running:
    #lopp through a list of ecents 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False 
           

    display_surface.fill(BLACK)
    
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
