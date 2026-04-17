import pygame
from ball import Ball
def main():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Moving Ball")

    clock = pygame.time.Clock()

    ball = Ball(400, 300)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 👇 управление на удержание
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            ball.move(-ball.step, 0, screen_width, screen_height)
        if keys[pygame.K_d]:
            ball.move(ball.step, 0, screen_width, screen_height)
        if keys[pygame.K_w]:
            ball.move(0, -ball.step, screen_width, screen_height)
        if keys[pygame.K_s]:
            ball.move(0, ball.step, screen_width, screen_height)

        screen.fill((0, 0, 0))
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # 60 FPS (чтобы движение было плавное)

    pygame.quit()


if __name__ == "__main__":
    main()