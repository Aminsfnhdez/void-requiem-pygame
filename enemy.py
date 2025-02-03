import random
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("assets/enemy.png").convert_alpha()
        # Redimensiona el enemigo a 40x40 píxeles
        self.image = pygame.transform.scale(original_image, (40, 40))
        self.rect = self.image.get_rect(center=(random.randint(50, 750), -50))
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.kill()
