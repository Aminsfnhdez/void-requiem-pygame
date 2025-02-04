import pygame

class Player(pygame.sprite.Sprite):
    """
    Clase que representa al jugador en el juego. Hereda de pygame.sprite.Sprite.
    """
    def __init__(self):
        """
        Inicializa el jugador con una imagen, posición y velocidad.
        """
        super().__init__()
        # Carga la imagen original del jugador
        original_image = pygame.image.load("assets/player.png").convert_alpha()
        # Redimensiona la imagen a un tamaño más apropiado (50x50 píxeles)
        self.image = pygame.transform.scale(original_image, (50, 50))
        # Establece la posición del jugador en el centro de la pantalla
        self.rect = self.image.get_rect(center=(400, 500))
        # Establece la velocidad del jugador
        self.speed = 7

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
