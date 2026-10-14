from random import uniform

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_direction = uniform(20, 50)
            velocity1 = self.velocity.rotate(new_direction)
            velocity2 = self.velocity.rotate(-new_direction)

            old_radius = self.radius

            asteroid1 = Asteroid(
                self.position.x, self.position.y, old_radius - ASTEROID_MIN_RADIUS
            )
            asteroid2 = Asteroid(
                self.position.x, self.position.y, old_radius - ASTEROID_MIN_RADIUS
            )
            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2
