import pygame

class Paddle:
    white = (255,255,255)
    colour = white
    velocity = 4

    # Initialize paddle
    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    # Draw paddle as a rect
    def draw(self, window):
        pygame.draw.rect(
            window, self.colour, (self.x, self.y, self.width, self.height))

    # Move paddle by changing the velocity
    # If up = True : move upwards
    # Else : move downwards
    def move(self, up=True):
        if up:
            self.y -= self.velocity
        else:
            self.y += self.velocity

    # Resets
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y