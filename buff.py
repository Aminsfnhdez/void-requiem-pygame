import pygame
import random
from config import WIDTH, HEIGHT

class Buff(pygame.sprite.Sprite):
    """
    Clase que representa un buff en el juego. Hereda de pygame.sprite.Sprite.
    """
    def __init__(self):
        """
        Inicializa el buff con una imagen, posición y velocidad.
        """
        super().__init__()
        # Cargar y escalar la imagen del buff
        self.image = pygame.image.load("assets/buff.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Ajusta el tamaño 
        self.rect = self.image.get_rect()
        
        # Posición aleatoria en la pantalla
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(50, HEIGHT//2)  # Aparece en la mitad superior
        
        # Velocidad de movimiento
        self.speedy = 2
        
    def update(self):
        """
        Actualiza la posición del buff en el eje y y lo elimina si sale de la pantalla.
        """
        # Movimiento simple hacia abajo
        self.rect.y += self.speedy
        
        # Si sale de la pantalla, eliminar el sprite
        if self.rect.top > HEIGHT:
            self.kill() 