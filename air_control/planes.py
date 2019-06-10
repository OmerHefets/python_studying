import random
from . import constants as cst


class Plane:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_position(self):
        return self.__x, self.__y

    def set_position(self, rand, bounds, x, y):
        """
        Set a starting position for a plane.
        0 < X < IMG_PER_LINE - 1
        0 < Y < IMG_PER_LINE - 1
        :param rand: return random position
        :param bounds: set the range of the random init
        :param x: X set if not random
        :param y: Y set if not random
        :return: set position
        """
        if not rand:
            self.__x = x
            self.__y = y
            return self.__x, self.__y
        else:
            self.__x = random.randint(0, cst.NUM_OF_IMAGES_PER_LINE)
            ###


def main():
    pass


if __name__ == "__main__":
    main()
