import pygame
class Bullet(pygame.sprite.Sprite):
    """
    Clase que representa una bala en el juego. Hereda de pygame.sprite.Sprite.
    """
    def __init__(self, x, y):
        """
        Inicializa la bala con una imagen, posición y tamaño.
        
        :param x: La posición x de la bala.
        :param y: La posición y de la bala.
        """
        super().__init__()
        original_image = pygame.image.load("assets/bullet.png").convert_alpha()
        # Redimensiona la bala a un tamaño más pequeño, por ejemplo 10x20 píxeles
        self.image = pygame.transform.scale(original_image, (10, 20))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        """
        Actualiza la posición de la bala, moviéndola hacia arriba y eliminándola si sale de la pantalla.
        """
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()
