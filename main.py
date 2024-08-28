import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from score_display import *

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load('background.jpg')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale if needed
    rocket_image = pygame.image.load("rocket.png").convert_alpha()
    rocket_image = pygame.transform.scale(rocket_image, (26,60))

    clock = pygame.time.Clock() 
    dt = 0
    score = 0
    

    #Setup Font
    font_size = 36
    font = pygame.font.Font(None, font_size)  # Use default font
    text_color = (255, 255, 255)  # White color
    

    #Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Add Object-Types to Groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    #Initialization
    player1 = Player(rocket_image, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    the_asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        #Player-asteroid collision check
        for asteroid in asteroids:
            if asteroid.collision(player1):
                print("Game over!")
                sys.exit()

            #Shots-asteroid collision check
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
                    score +=1
                    break

        score_text = f"Score: {score}"

        #Black out screen
        screen.blit(background_image, (0,0))
        
        #Draws all asteroids, shots, and rocket
        for obj in drawable:
            obj.draw(screen)

        # Render the score text
        score_text = f"Score: {score}"
        text_surface = font.render(score_text, True, text_color)
        score_text_rect = text_surface.get_rect(topleft=(10, 10))

        #Draws score text
        screen.blit(text_surface, score_text_rect)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
