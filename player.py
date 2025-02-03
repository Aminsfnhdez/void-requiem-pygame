import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Carga la imagen original
        original_image = pygame.image.load("assets/player.png").convert_alpha()
        # Redimensiona la imagen a un tamaño más apropiado (por ejemplo, 50x50 píxeles)
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect(center=(400, 500))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
