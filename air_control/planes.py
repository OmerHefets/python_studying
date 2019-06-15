import random
# from . import constants as cst

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


class Plane:

    def __init__(self, x, y, rand):
        self.__x = -1
        self.__y = -1
        self.set_position(x=x, y=y, rand=rand, bounds=NUM_OF_IMAGES_PER_LINE)

    def get_position(self):
        return self.__x, self.__y

    def set_position(self, x, y, rand, bounds=NUM_OF_IMAGES_PER_LINE):
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
            self.__x = random.randint(0, bounds)

    @staticmethod
    def check_for_collisions(list_of_planes, x_coor, y_coor):
        x_coordinates_list = []
        y_coordinates_list = []
        if len(list_of_planes) == 0:
            return False
        for plane in list_of_planes:
            temp_x, temp_y = plane.get_position()
            x_coordinates_list.append(temp_x)
            y_coordinates_list.append(temp_y)
        if x_coor in x_coordinates_list:
            return True
        elif y_coor in y_coordinates_list:
            return True
        else:
            return False


"""
# check collisions in X
for i in range(len(x_coordinates_list)):
    for j in range(len(x_coordinates_list)):
        if i != j and x_coordinates_list[i] == x_coordinates_list[j]:
            return True
# check collisions in Y
for i in range(len(y_coordinates_list)):
    for j in range(len(y_coordinates_list)):
        if i != j and y_coordinates_list[i] == y_coordinates_list[j]:
            return True
return False
"""


def main():
    pass


if __name__ == "__main__":
    main()
