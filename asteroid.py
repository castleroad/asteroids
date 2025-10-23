from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        radius = ASTEROID_MIN_RADIUS
        
        self.kill()

        if (self.radius == radius):
            return

        angle = random.uniform(20, 50)
        speed_multiplier = 1.2

        if (self.radius < ASTEROID_MAX_RADIUS):
            astr = Asteroid(self.position.x, self.position.y, radius)
            astr.velocity = self.velocity.rotate(angle) * speed_multiplier
            astr = Asteroid(self.position.x, self.position.y, radius)
            astr.velocity = self.velocity.rotate(-angle) * speed_multiplier
            return
            
        radius += ASTEROID_MIN_RADIUS
        astr = Asteroid(self.position.x, self.position.y, radius)
        astr.velocity = self.velocity.rotate(angle) * speed_multiplier
        astr = Asteroid(self.position.x, self.position.y, radius)
        astr.velocity = self.velocity.rotate(-angle) * speed_multiplier
