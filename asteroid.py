import pygame
import random
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
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        # get the split angle and new velocities
        split_angle = random.uniform(20, 50)
        new_velocity_one = self.velocity.rotate(split_angle)
        new_velocity_two = self.velocity.rotate(-split_angle)
        
        # create new asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_one.velocity = new_velocity_one * 1.2
        asteroid_two.velocity = new_velocity_two * 1.2
        
        for group in self.groups():
            group.add(asteroid_one)
            group.add(asteroid_two)
        self.kill()