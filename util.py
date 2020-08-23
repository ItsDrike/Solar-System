import random
import typing as t
from math import sqrt, sin, cos


def number_remap(
    value: float,
    old_min: float,
    old_max: float,
    new_min: float,
    new_max: float
) -> float:
    return ((value - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min


def euclidean_distance(
    point1_x: float,
    point1_y: float,
    point2_x: float,
    point2_y: float
) -> float:
    x_dist = abs(point1_x - point2_x)
    y_dist = abs(point1_y - point2_y)
    return sqrt(x_dist ** 2 + y_dist ** 2)


def rotate(
    point_x: float,
    point_y: float,
    center_x: float,
    center_y: float,
    angle: float
) -> t.Tuple[float, float]:
    rotated_x = cos(angle) * (point_x - center_x) - sin(angle) * (point_y - center_y) + center_x
    rotated_y = sin(angle) * (point_x - center_x) + cos(angle) * (point_y - center_y) + center_y

    return rotated_x, rotated_y


class Colors:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREY = 125, 125, 125
    RED = 240, 20, 30
    GREEN = 30, 255, 20
    BLUE = 100, 0, 255
    YELLOW = 255, 255, 0

    ColorType = t.Tuple[int, int, int]

    @staticmethod
    def RANDOM() -> ColorType:
        return (random.randint(100, 255), 0, random.randint(100, 255))
