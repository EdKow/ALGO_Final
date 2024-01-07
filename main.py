import pygame
from ball import Ball
from paddle import Paddle
import GameFunction as GF


# Initialise game
pygame.init()

# Adjust width and height
width, height = 700, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# FPS
frame_per_second = 60

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# paddle dimension
paddle_width, paddle_height = 20, 100

# Size of the ball
ball_radius = 10

# Font
font_score = pygame.font.SysFont("comicsans", 50)

# winning requirement
winning_score = 10


def main():
    run = True
    clock = pygame.time.Clock()

    # Adjusts the left paddle size/position
    left_paddle = Paddle(10, height // 2 - paddle_height //
                         2, paddle_width, paddle_height)
    # Adjust the right paddle size/position
    right_paddle = Paddle(width - 10 - paddle_width, height //
                          2 - paddle_height // 2, paddle_width, paddle_height)
    # Adjusts ball size/position
    ball = Ball(width // 2, height // 2, ball_radius)

    # Sets initial score for both paddles
    left_score = 0
    right_score = 0

    while run:
        clock.tick(frame_per_second)

        # Draws elements to the screen
        GF.draw(window, [left_paddle, right_paddle], ball, left_score, right_score)

        # Safe exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Adds keyboard event
        keys = pygame.key.get_pressed()
        GF.paddle_movement(keys, left_paddle, right_paddle)

        # Ball movement
        ball.move()
        GF.collision(ball, left_paddle, right_paddle)

        # scoring on the opponents side
        if ball.x < 0:
            right_score += 1
            pygame.time.delay(1500)
            ball.reset()
        elif ball.x > width:
            left_score += 1
            pygame.time.delay(1500)
            ball.reset()

        # So that there is an end to the game
        won = False
        if left_score >= winning_score:
            won = True
            win_text = "Left Player Won!"
        elif right_score >= winning_score:
            won = True
            win_text = "Right Player Won!"

        if won:
            text = font_score.render(win_text, 1, white)
            window.blit(text, (width // 2 - text.get_width() //
                               2, height // 2 - text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

if __name__ == '__main__':
    main()