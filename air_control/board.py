import pygame
import random
from .constants import ###
# from planes import Plane

NUM_OF_IMAGES_PER_LINE = 10
IMAGE_HEIGHT = 50  # pixels
IMAGE_WIDTH = 50  # pixels
LINE_HEIGHT_PIXEL = 2
NUM_OF_LINES = NUM_OF_IMAGES_PER_LINE + 1
NUM_OF_PLANES = 4

WINDOW_HEIGHT = (IMAGE_HEIGHT * NUM_OF_IMAGES_PER_LINE) + (LINE_HEIGHT_PIXEL * NUM_OF_LINES)
WINDOW_WIDTH = (IMAGE_WIDTH * NUM_OF_IMAGES_PER_LINE) + (LINE_HEIGHT_PIXEL * NUM_OF_LINES)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def init_screen():
    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Air Control")
    screen.fill(WHITE)
    pygame.display.flip()
    # init horizontal lines
    for i in range(NUM_OF_LINES):
        current_x_location = i * IMAGE_WIDTH + i * LINE_HEIGHT_PIXEL
        pygame.draw.line(screen, BLACK, [current_x_location, 0], [current_x_location, WINDOW_HEIGHT], LINE_HEIGHT_PIXEL)
        pygame.display.flip()
    # init vertical lines
    for i in range(NUM_OF_LINES):
        current_y_location = i * IMAGE_HEIGHT + i * LINE_HEIGHT_PIXEL
        pygame.draw.line(screen, BLACK, [0, current_y_location], [WINDOW_WIDTH, current_y_location], LINE_HEIGHT_PIXEL)
        pygame.display.flip()

    init_game(number_of_planes=NUM_OF_PLANES)
    pygame.quit()


def init_game(number_of_planes):
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        init_planes(number_of_planes=NUM_OF_PLANES)


def init_planes(number_of_planes):
    """
    Make sure that the planes do not start in the same position.
    :return:
    """
    planes_list = pygame.sprite.Group()



def movement_options():
    pass


def sum_score():
    pass


def main():
    init_screen()


if __name__ == "__main__":
    main()
