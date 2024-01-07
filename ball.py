import pygame

class Ball:
    max_velocity = 5
    white = (255,255,255)
    colour = white

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.max_velocity
        self.y_vel = 0

    def draw(self, window):
        pygame.draw.circle(window, self.colour, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1