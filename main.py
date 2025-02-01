import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0)) # fill screen with black
        pygame.display.flip() # refresh the screen
        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()
