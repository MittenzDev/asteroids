import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # create player instance here
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        updatable.update(dt)
        screen.fill((0, 0, 0)) # fill screen with black
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip() # refresh the screen
        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()
