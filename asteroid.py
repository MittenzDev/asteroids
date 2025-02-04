import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rect = pygame.Rect(
            x - self.radius, y - self.radius, self.radius * 2, self.radius * 2
        )
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width = 2)
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position