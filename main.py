import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    #Initialization
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
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
                    break

        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)
        # player1.update(dt)
        # player1.draw(screen) #renders player on screen


        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
