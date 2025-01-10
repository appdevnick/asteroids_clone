import circleshape
import pygame
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
       self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            new_asteroids_angle = random.uniform(20, 50)
            new_vec_one = self.velocity.rotate(new_asteroids_angle)
            new_vec_two = self.velocity.rotate(-new_asteroids_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_roid_one = Asteroid(self.position.x, self.position.y, new_radius)
            new_roid_two = Asteroid(self.position.x, self.position.y, new_radius)
            new_roid_one.velocity = new_vec_one * 1.2
            new_roid_two.velocity = new_vec_two * 1.2