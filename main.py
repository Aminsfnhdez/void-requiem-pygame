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

# Inicializar sistema de puntos y oleadas
score = 0
current_wave = 1
enemies_in_wave = 0
max_waves = 10
enemies_per_wave = 10
wave_transition = True  # variable para controlar la transición entre oleadas
wave_transition_timer = 0  # Temporizador para la transición
WAVE_TRANSITION_DURATION = 2000  # Duración de la transición en milisegundos
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
    global enemies_in_wave
    if enemies_in_wave < enemies_per_wave:
        enemy = Enemy(current_wave)
        all_sprites.add(enemy)
        enemies.add(enemy)
        enemies_in_wave += 1

# Función para mostrar puntuación y oleada
def draw_score():
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    wave_text = font.render(f"Wave: {current_wave}/{max_waves}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(wave_text, (10, 50))

# Función para mostrar mensaje de oleada
def draw_wave_message():
    # Hacer que el mensaje parpadee usando una función seno
    if (pygame.time.get_ticks() // 200) % 2:  # Parpadeo cada 200ms
        wave_message = font.render(f"WAVE {current_wave}", True, (255, 255, 255))
        message_rect = wave_message.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(wave_message, message_rect)

# Bucle principal del juego
running = True
while running:
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Disparar con la tecla espacio
        if event.type == pygame.KEYDOWN and not wave_transition:  # No disparar durante la transición
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()

    # Manejar transición entre oleadas
    if wave_transition:
        if wave_transition_timer == 0:
            wave_transition_timer = current_time
        elif current_time - wave_transition_timer >= WAVE_TRANSITION_DURATION:
            wave_transition = False
            wave_transition_timer = 0
    
    # Generar enemigos aleatoriamente (solo si no estamos en transición)
    if not wave_transition and random.randint(1, 100) < 3:
        spawn_enemy()

    # Actualizar sprites
    keys = pygame.key.get_pressed()
    player.update(keys)
    # Actualizar todos los sprites excepto el jugador
    for sprite in all_sprites:
        if sprite != player:
            sprite.update()

    # Colisiones de balas con enemigos
    hits = pygame.sprite.groupcollide(enemies, bullets, False, True)
    for enemy in hits:
        if enemy.hit():  # Si el enemigo debe ser eliminado
            explosion_sound.play()
            score += 100
            enemy.kill()
            
    # Verificar si la oleada actual ha terminado
    if enemies_in_wave >= enemies_per_wave and len(enemies) == 0:
        current_wave += 1
        enemies_in_wave = 0
        if current_wave > max_waves:
            # Victoria - el jugador ha completado todas las oleadas
            victory_text = font.render("¡Victoria!", True, (255, 255, 255))
            screen.blit(victory_text, (WIDTH//2 - 50, HEIGHT//2))
            pygame.display.flip()
            pygame.time.wait(2000)  # Esperar 2 segundos
            running = False
        else:
            # Iniciar transición a la siguiente oleada
            wave_transition = True
            wave_transition_timer = 0

    # Colisión de enemigos con el jugador (fin del juego)
    if pygame.sprite.spritecollide(player, enemies, True):
        running = False  # Fin del juego

    # Dibujar en pantalla
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    draw_score()  # Dibujar la puntuación
    
    # Mostrar mensaje de oleada durante la transición
    if wave_transition:
        draw_wave_message()

    # Actualizar pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()

