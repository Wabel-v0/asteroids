import pygame
from constants import *


def main():
    print("starting asteroids")
    print(f"Screen size: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    BLACK = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        pygame.display.flip()


if __name__ == "__main__":
    main()
