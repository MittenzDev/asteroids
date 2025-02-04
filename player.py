from circleshape import CircleShape
import pygame
import constants
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.space_pressed = False
        self.shoot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width = 2)
    
    def rotate(self, dt):
        self.rotation = self.rotation + (constants.PLAYER_TURN_SPEED * dt)
        self.rotation %= 360 # constrains self.rotation to always be between 0 and 360
    
    def shoot(self):
        if self.shoot_timer > 0:
            return None
        self.shoot_timer = constants.PLAYER_SHOOT_COOLDOWN
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity *= constants.PLAYER_SHOOT_SPEED
        return Shot(self.position.x, self.position.y, velocity)


    def update(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        keys = pygame.key.get_pressed()
        shot = None

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if not self.space_pressed:
                shot = self.shoot()
                self.space_pressed = True
        else:
            self.space_pressed = False
        return shot

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
