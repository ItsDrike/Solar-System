from contextlib import suppress

import pygame

from util import Colors
from planet import Planet

PLANETS = 5
WIDTH, HEIGHT = 1200, 900
TICK_RATE = 100


class Game:
    def __init__(self, width: int, height: int, fps: int) -> None:
        self.size = self.width, self.height = width, height

        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.fps_clock = pygame.time.Clock()
        self.tick_rate = fps

        self.running = True

    def handle_user_event(self) -> None:
        """Handle pygame events (f.e.: quit, click)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False

    def redraw_screen(self) -> None:
        """
        Redraw all cells on the screen.

        This does not update the screen, it only redraws it.
        """
        self.screen.fill(Colors.BLACK)

        # Draw the sun
        pygame.draw.circle(
            self.screen,
            Colors.YELLOW,
            (round(self.width / 2), round(self.height / 2)),
            20
        )

        # Draw other planets
        for planet in self.planets:
            pygame.draw.circle(self.screen, Colors.GREEN, *planet.orbit_shape, 1)
            pygame.draw.circle(self.screen, Colors.WHITE, *planet.shape)

    def update_screen(self, tick: bool = True) -> None:
        """
        Update the screen accordingly to `redraw_screen`
        also check for user event and tick (if not specified otherwise)
        """

        self.handle_user_event()

        if not self.running:
            return

        self.redraw_screen()
        pygame.display.update()
        if tick:
            self.fps_clock.tick(self.tick_rate)

    def main(self, planets: int) -> None:
        # Planet creation
        self.planets = []
        center = (self.width / 2, self.height / 2)
        max_orbit_radius = min(self.width / 2, self.height / 2) - 15

        for _ in range(planets):
            self.planets.append(Planet.random_planet(center, max_orbit_radius))

        # Main game loop
        while self.running:
            for planet in self.planets:
                planet.rotate()

            self.update_screen()


game = Game(WIDTH, HEIGHT, TICK_RATE)

with suppress(KeyboardInterrupt):
    game.main(PLANETS)

print("\nStopped")
pygame.quit()
