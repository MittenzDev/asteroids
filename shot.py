import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.rect = pygame.Rect(
            x - SHOT_RADIUS, y - SHOT_RADIUS, SHOT_RADIUS * 2, SHOT_RADIUS * 2
        )
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width = 2)
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position