import pygame



# Draws screen and adds elements to it
def draw(window, paddles, ball, left_score, right_score):
    
    font_score = pygame.font.SysFont("comicsans", 50)
    width, height = 700, 500
    white = (255,255,255)
    black = (0,0,0)
    
    # Fills window with black colour
    window.fill(black)
    
    # Adds text/labels to window
    left_score_text = font_score.render(f"{left_score}", 1, white)
    right_score_text = font_score.render(f"{right_score}", 1, white)
    window.blit(left_score_text, (width // 4 - left_score_text.get_width() // 2, 20))
    window.blit(right_score_text, (width * (3 / 4) - right_score_text.get_width() // 2, 20))

    # Draws paddle on screen
    for paddle in paddles:
        paddle.draw(window)

    # Draws the dotted line in the centre
    for i in range(10, height, height // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(window, white, (width // 2 - 5, i, 10, height // 20))

    # Draws ball on screen
    ball.draw(window)
    pygame.display.update()


def collision(ball, left_paddle, right_paddle):
    width, height = 700, 500
    # Checks if the ball hits the ceiling of the screen
    if ball.y + ball.radius >= height:
        ball.y_vel *= -1
    # Checks if the ball hits the floor of the screen
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    # Checks if the ball is colliding with the left paddle
    if ball.x_vel < 0:
        if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.max_velocity
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    # Checks if the ball is colliding with the right paddle
    else:
        if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.max_velocity
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


# Handles the movement of both paddles
def paddle_movement(keys, left_paddle, right_paddle):
    width, height = 700, 500

    # if key W is pressed: move left paddle up
    # Ensure that the paddle doesn't go off screen
    if keys[pygame.K_w] and left_paddle.y - left_paddle.velocity >= 0:
        left_paddle.move(up=True)

    # if key S is pressed: move left paddle down
    # Ensure that the paddle doesn't go off screen
    if keys[pygame.K_s] and left_paddle.y + left_paddle.velocity + left_paddle.height <= height:
        left_paddle.move(up=False)

    # if key UP is pressed: move right paddle up
    # Ensure that the paddle doesn't go off screen
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.velocity >= 0:
        right_paddle.move(up=True)

    # if key DOWN is pressed: move right paddle down
    # Ensure that the paddle doesn't go off screen
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.velocity + right_paddle.height <= height:
        right_paddle.move(up=False)