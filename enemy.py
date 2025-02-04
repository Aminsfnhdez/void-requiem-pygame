import random
import pygame

class Enemy(pygame.sprite.Sprite):
    """
    Clase que representa a los enemigos en el juego. Hereda de pygame.sprite.Sprite.
    """
    # Variable de clase para controlar si el jefe ya apareció
    boss_has_spawned = False

    def __init__(self, wave):
        """
        Inicializa el enemigo con una imagen, posición, velocidad y salud basado en la oleada.
        
        :param wave: El número de la oleada actual.
        """
        super().__init__()
        # Determinar qué tipo de enemigo crear basado en la oleada
        if wave == 10 and not Enemy.boss_has_spawned:  # Verificar si el jefe no ha aparecido
            original_image = pygame.image.load("assets/boss-final.png").convert_alpha()
            self.image = pygame.transform.scale(original_image, (120, 120))  # Tamaño más grande para el jefe
            self.health = 20  # 20 impactos para derrotar al jefe
            self.is_boss = True
            self.max_health = 20  # Para la barra de vida
            Enemy.boss_has_spawned = True  # Marcar que el jefe ya apareció
        elif wave >= 5 and random.random() < 0.4:
            original_image = pygame.image.load("assets/enemy2.png").convert_alpha()
            self.image = pygame.transform.scale(original_image, (40, 40))
            self.health = 2
            self.is_boss = False
        else:
            original_image = pygame.image.load("assets/enemy.png").convert_alpha()
            self.image = pygame.transform.scale(original_image, (40, 40))
            self.health = 1
            self.is_boss = False
            
        self.rect = self.image.get_rect()
        if self.is_boss:
            self.rect.centerx = 400  # Centrar el jefe horizontalmente
            self.rect.top = -120  # Comenzar fuera de la pantalla
            self.speed = 2  # Velocidad fija para el jefe
        else:
            self.rect.center = (random.randint(50, 750), -50)
            # Determinar velocidad según la dificultad de la oleada
            if wave <= 3:  # Fácil
                self.speed = random.randint(1, 1)
            elif wave <= 6:  # Medio
                self.speed = random.randint(1, 2)
            else:  # Difícil (oleadas 7-9)
                self.speed = random.randint(2, 3)

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

    def draw_health_bar(self, screen):
        """
        Dibuja la barra de vida del jefe final.
        """
        if self.is_boss:
            bar_width = 200
            bar_height = 20
            bar_x = 300  # Centrada horizontalmente
            bar_y = 20   # Cerca de la parte superior
            
            # Barra de fondo (roja)
            pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
            # Barra de vida actual (verde)
            health_width = (self.health / self.max_health) * bar_width
            pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, health_width, bar_height))
