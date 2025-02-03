import pygame
import random
from config import WIDTH, HEIGHT, FPS
from player import Player
from enemy import Enemy
from bullet import Bullet

# Inicializar PyGame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Void Requiem: The Last Stand")
clock = pygame.time.Clock()

# Inicializar sistema de puntos
score = 0
font = pygame.font.Font(None, 36)

# Cargar imagen de fondo
background = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Cargar sonidos
shoot_sound = pygame.mixer.Sound("assets/laser.wav")
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")

# Grupos de sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Función para generar enemigos periódicamente
def spawn_enemy():
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Función para mostrar puntuación
def draw_score():
    score_text = font.render(f"Puntos: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Bucle principal del juego
running = True
while running:
    clock.tick(FPS)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Disparar con la tecla espacio
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()

    # Generar enemigos aleatoriamente
    if random.randint(1, 100) < 3:
        spawn_enemy()

    # Actualizar sprites
    keys = pygame.key.get_pressed()
    player.update(keys)
    # Actualizar todos los sprites excepto el jugador
    for sprite in all_sprites:
        if sprite != player:
            sprite.update() 

    # Colisiones de balas con enemigos
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        explosion_sound.play()
        score += 100  # Aumentar puntuación cuando se destruye un enemigo

    # Colisión de enemigos con el jugador (fin del juego)
    if pygame.sprite.spritecollide(player, enemies, True):
        running = False  # Fin del juego

    # Dibujar en pantalla
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    draw_score()  # Dibujar la puntuación

    # Actualizar pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()

