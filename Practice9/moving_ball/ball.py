import pygame


class Ball:
    """A ball that moves in fixed steps and stays inside the screen."""

    def __init__(self, x: int, y: int, radius: int = 25, color=(255, 0, 0), step: int = 20):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.step = step

    def move(self, dx: int, dy: int, screen_width: int, screen_height: int) -> None:
        """Move the ball only if the new position stays inside the screen."""
        new_x = self.x + dx
        new_y = self.y + dy

        if self.radius <= new_x <= screen_width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= screen_height - self.radius:
            self.y = new_y

    def handle_key(self, key: int, screen_width: int, screen_height: int) -> None:
        """Move the ball 20 pixels for each arrow key press."""
        if key == pygame.K_a:
            self.move(-self.step, 0, screen_width, screen_height)
        elif key == pygame.K_d:
            self.move(self.step, 0, screen_width, screen_height)
        elif key == pygame.K_w:
            self.move(0, -self.step, screen_width, screen_height)
        elif key == pygame.K_s:
            self.move(0, self.step, screen_width, screen_height)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
