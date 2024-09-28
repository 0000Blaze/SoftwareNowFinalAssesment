import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600S
FPS = 60

# Player class
class Player:
    def __init__(self):
        self.x = 100
        self.y = 500
        self.health = 100
        self.lives = 3
        self.speed = 5

    def move(self, dx):
        self.x += dx

    def jump(self):
        # Implement jump logic
        pass

# Projectile class
class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10

    def move(self):
        self.x += self.speed

# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player()
    projectiles = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player.speed)
        if keys[pygame.K_RIGHT]:
            player.move(player.speed)
        if keys[pygame.K_SPACE]:
            projectiles.append(Projectile(player.x, player.y))

        # Update projectile positions
        for projectile in projectiles:
            projectile.move()

        screen.fill((0, 0, 0))  # Clear screen
        pygame.display.flip()  # Update display
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
