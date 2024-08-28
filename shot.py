import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self,image, rotation, x, y):
        super().__init__(x,y,SHOT_RADIUS)
        self.image = pygame.transform.scale(image, (13,30))
        self.rotation = rotation

    def draw(self, screen):
        #pygame.draw.circle(screen, "white", self.position, self.radius, 2)

        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        rotated_rect = rotated_image.get_rect(center = self.position)
        screen.blit(rotated_image, rotated_rect)

    def update(self, dt):
        self.position += self.velocity * dt