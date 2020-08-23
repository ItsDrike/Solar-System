import typing as t
import random
from util import euclidean_distance, rotate

VECTOR = t.Tuple[float, float]


class Planet:
    def __init__(self, position: VECTOR, radius: float, center: VECTOR, orbit_angle: float):
        self.position = position
        self.radius = radius
        self.center = center
        self.orbit_angle = orbit_angle

        self.orbit_radius = euclidean_distance(*position, *center)
        self.rotation_angle = (365 / self.radius) / self.orbit_radius
        self.rotation_angle /= 10

    def rotate(self) -> None:
        self.position = rotate(*self.position, *self.center, self.rotation_angle)

    @property
    def shape(self) -> t.Tuple[t.Tuple[int, int], int]:
        return (round(self.position[0]), round(self.position[1])), round(self.radius)

    @property
    def orbit_shape(self) -> t.Tuple[t.Tuple[int, int], int]:
        return (round(self.center[0]), round(self.center[1])), round(self.orbit_radius)

    @classmethod
    def random_planet(
        cls,
        center: VECTOR,
        max_orbit_radius: float,
        min_orbit_radius: float = 20,
        max_radius: float = 15,
        min_radius: float = 5,
        orbit_angle: float = 0.0
    ):
        random_x = center[0] + random.uniform(min_orbit_radius, max_orbit_radius)
        random_pos = (random_x, center[1])
        radius = random.uniform(min_radius, max_radius)

        return cls(random_pos, radius, center, orbit_angle)
