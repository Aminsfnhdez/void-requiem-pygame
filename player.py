import pygame
import os

class Player(pygame.sprite.Sprite):
    """
    Clase que representa al jugador en el juego. Hereda de pygame.sprite.Sprite.
    """
    def __init__(self):
        """
        Inicializa el jugador con una imagen, posición y velocidad.
        """
        super().__init__()
        # Obtener el directorio base y cargar la imagen
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        original_image = pygame.image.load(os.path.join(BASE_DIR, "assets", "player.png")).convert_alpha()
        # Redimensiona la imagen a un tamaño más apropiado (50x50 píxeles)
        self.image = pygame.transform.scale(original_image, (50, 50))
        # Establece la posición del jugador en el centro de la pantalla
        self.rect = self.image.get_rect(center=(400, 500))
        # Establece la velocidad del jugador
        self.speed = 7
        # Agrega la variable double_shot
        self.double_shot = False
        self.double_shot_timer = 0
        self.DOUBLE_SHOT_DURATION = 5000  # 5 segundos en milisegundos

    def update(self, keys):
        """
        Actualiza la posición del jugador según las teclas presionadas.
        
        :param keys: Un diccionario de teclas presionadas.
        """
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            # Mueve el jugador a la izquierda si la tecla izquierda está presionada y no está en el borde izquierdo
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            # Mueve el jugador a la derecha si la tecla derecha está presionada y no está en el borde derecho
            self.rect.x += self.speed
        # Actualizar el temporizador del doble disparo
        if self.double_shot:
            current_time = pygame.time.get_ticks()
            if current_time - self.double_shot_timer >= self.DOUBLE_SHOT_DURATION:
                self.double_shot = False
