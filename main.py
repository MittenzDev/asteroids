import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    game_font = pygame.font.Font(None, 64)
    running = True
    asteroid_field = AsteroidField()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # create player instance here
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        updatable.update(dt)
        shot = player.update(dt)
        if shot:
            shots.add(shot)
        for asteroid in asteroids:
            if player.collision(asteroid):
                running = False # stop the main game loop
                break # exit the asteroid checking loop
            for shot in shots:
                if pygame.sprite.collide_rect(shot, asteroid):
                    shot.kill()
                    asteroid.kill()

        if running:
            screen.fill((0, 0, 0)) # fill screen with black
            for sprite in drawable:
                sprite.draw(screen)
        else:
            screen.fill((0, 0, 0)) # draw game over screen
            text_surface = game_font.render("Game Over!", True, (255, 0, 0)) # True to enable anti-aliasing of text and set color to red
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        if not running:
            pygame.time.wait(1000) # wait 1 second before closing the window
            sys.exit()

if __name__ == "__main__":
    main()
