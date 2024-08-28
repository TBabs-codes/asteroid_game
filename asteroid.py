import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.asteroid_image = pygame.image.load("asteroid.png").convert_alpha()
        self.asteroid_image_scaled = pygame.transform.scale(self.asteroid_image, (radius*2.1//1,radius*2.1//1))

    def draw(self, screen):
        #pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        rect = self.asteroid_image_scaled.get_rect(center = self.position)
        screen.blit(self.asteroid_image_scaled, rect)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            a1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            a2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            a1.velocity = velocity1 * 1.2
            a2.velocity = velocity2 * 1.2
