import random
import pygame

class Enemy(pygame.sprite.Sprite):
    """
    Clase que representa a los enemigos en el juego. Hereda de pygame.sprite.Sprite.
    """
    def __init__(self, wave):
        """
        Inicializa el enemigo con una imagen, posición, velocidad y salud basado en la oleada.
        
        :param wave: El número de la oleada actual.
        """
        super().__init__()
        # Determinar qué tipo de enemigo crear basado en la oleada
        if wave >= 5 and random.random() < 0.4:  # 40% de probabilidad de enemy2 después de oleada 5
            original_image = pygame.image.load("assets/enemy2.png").convert_alpha()
            self.health = 2  # Enemigos tipo 2 necesitan 2 impactos
        else:
            original_image = pygame.image.load("assets/enemy.png").convert_alpha()
            self.health = 1  # Enemigos normales necesitan 1 impacto
            
        self.image = pygame.transform.scale(original_image, (40, 40))
        self.rect = self.image.get_rect(center=(random.randint(50, 750), -50))
        self.speed = random.randint(1, 2)

    def hit(self):
        """
        Reduce la salud del enemigo en 1 y verifica si debe ser eliminado.
        
        :return: Retorna True si el enemigo debe ser eliminado.
        """
        self.health -= 1
        return self.health <= 0  # Retorna True si el enemigo debe ser eliminado

    def update(self):
        """
        Actualiza la posición del enemigo en el eje y y lo elimina si sale de la pantalla.
        """
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.kill()
