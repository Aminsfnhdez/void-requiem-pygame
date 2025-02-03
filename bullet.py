import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()
