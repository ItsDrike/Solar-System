import typing as t
import random
from util import euclidean_distance, rotate

VECTOR = t.Tuple[float, float]


class NotEnoughSpace(Exception):
    pass


class Planet:
    def __init__(self, position: VECTOR, radius: float, center: VECTOR):
        self.position = position
        self.radius = radius
        self.center = center

        self.orbit_radius = euclidean_distance(*position, *center)
        self.rotation_angle = 365 / (self.radius * self.orbit_radius)
        self.rotation_angle /= 10  # Arbitrary constant to slow things down

    def rotate(self) -> None:
        self.position = rotate(*self.position, *self.center, self.rotation_angle)

    @property
    def shape(self) -> t.Tuple[t.Tuple[int, int], int]:
        return (round(self.position[0]), round(self.position[1])), round(self.radius)

    @property
    def orbit_shape(self) -> t.Tuple[t.Tuple[int, int], int]:
        return (round(self.center[0]), round(self.center[1])), round(self.orbit_radius)

    @property
    def borders(self) -> t.Tuple[list, list]:
        borders_x = [
            self.position[0] + self.radius,
            self.position[0] - self.radius,
        ]
        borders_y = [
            self.position[1] + self.radius,
            self.position[1] - self.radius,
        ]
        return borders_x, borders_y

    def overlaps(self, other: "Planet") -> bool:
        dist = euclidean_distance(*self.position, *other.position)
        return dist <= (self.radius + other.radius)

    @classmethod
    def random_planet_no_overlap(
        cls,
        planets: t.List["Planet"],
        max_radius: float,
        min_radius: float,
        center: VECTOR,
        max_orbit_radius: float,
        min_orbit_radius: float
    ):
        radius = random.uniform(min_radius, max_radius)
        x = center[0] + random.uniform(min_orbit_radius, max_orbit_radius)
        random_pos = (x, center[1])
        new_planet = cls(random_pos, radius, center)

        for planet in planets:
            if new_planet.overlaps(planet):
                return cls.random_planet_no_overlap(
                    planets, max_radius, min_radius, center, max_orbit_radius, min_orbit_radius
                )

        return new_planet

    @classmethod
    def generate_random_planets(
        cls,
        amount: int,
        center: VECTOR,
        max_orbit_radius: float,
        min_orbit_radius: float = 30.0,
        max_radius: float = 15.0,
        min_radius: float = 5.0,
    ) -> t.List["Planet"]:
        planets = []

        for _ in range(amount):
            try:
                planet = cls.random_planet_no_overlap(
                    planets, max_radius, min_radius, center, max_orbit_radius, min_orbit_radius
                )
            except RecursionError:
                raise NotEnoughSpace("Can't create planets without overlapping")
            planets.append(planet)

        return planets
