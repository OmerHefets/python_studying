import pygame
import random
# from planes import Plane


NUM_OF_IMAGES_PER_LINE = 10
IMAGE_HEIGHT = 50  # pixels
IMAGE_WIDTH = 50  # pixels
LINE_HEIGHT_PIXEL = 2
NUMBER_OF_LINES = NUM_OF_IMAGES_PER_LINE + 1

WINDOW_HEIGHT = (IMAGE_HEIGHT * NUM_OF_IMAGES_PER_LINE) + (LINE_HEIGHT_PIXEL * NUMBER_OF_LINES)
WINDOW_WIDTH = (IMAGE_WIDTH * NUM_OF_IMAGES_PER_LINE) + (LINE_HEIGHT_PIXEL * NUMBER_OF_LINES)

WHITE = (255, 255, 255)


def init_screen():
    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Air Control")
    screen.fill(WHITE)
    pygame.display.flip()
    for i in range(NUM_OF_IMAGES_PER_LINE + 1):
        pass
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
    pygame.quit()


def init_game():
    pass


def init_planes():
    """
    Make sure that the planes do not start in the same position.
    :return:
    """
    pass


def movement_options():
    pass


def sum_score():
    pass


def main():
    init_screen()


if __name__ == "__main__":
    main()
