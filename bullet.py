import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        original_image = pygame.image.load("assets/bullet.png").convert_alpha()
        # Redimensiona la bala a un tamaño más pequeño, por ejemplo 10x20 píxeles
        self.image = pygame.transform.scale(original_image, (10, 20))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()
