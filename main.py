import pygame
import random
from config import WIDTH, HEIGHT, FPS
from player import Player
from enemy import Enemy
from bullet import Bullet
from buff import Buff

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
buffs = pygame.sprite.Group()

# Cargar imágenes del menú
start_button_img = pygame.image.load("assets/start.png")
start_button_img = pygame.transform.scale(start_button_img, (200, 80))  # Ajusta el tamaño según tu imagen
start_button_hover = pygame.transform.scale(start_button_img, (220, 88))  # Versión más grande para hover

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
    # Hacer que el mensaje parpadea usando una función seno
    if (pygame.time.get_ticks() // 200) % 2:  # Parpadeo cada 200ms
        wave_message = font.render(f"WAVE {current_wave}", True, (255, 255, 255))
        message_rect = wave_message.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(wave_message, message_rect)

# Función para dibujar el menú
def draw_menu():
    screen.blit(background, (0, 0))
    title_font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 46)
    
    # Título del juego
    title = title_font.render("Void Requiem: The Last Stand", True, (255, 255, 255))
    title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//3))
    screen.blit(title, title_rect)
    
    # Obtener posición del mouse
    mouse_pos = pygame.mouse.get_pos()
    
    # Botón de inicio con imagen
    start_rect = start_button_img.get_rect(center=(WIDTH//2, HEIGHT//2))
    if start_rect.collidepoint(mouse_pos):
        hover_rect = start_button_hover.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(start_button_hover, hover_rect)
        start_rect = hover_rect
    else:
        screen.blit(start_button_img, start_rect)
    
    # Botón Help
    help_text = button_font.render("Help", True, (255, 255, 255))
    help_rect = help_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 60))
    if help_rect.collidepoint(mouse_pos):
        help_text = pygame.font.Font(None, 52).render("Help", True, (255, 255, 0))
        help_rect = help_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 60))
    screen.blit(help_text, help_rect)
    
    # Botón Quit
    quit_text = button_font.render("Quit", True, (255, 255, 255))
    quit_rect = quit_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 120))
    if quit_rect.collidepoint(mouse_pos):
        quit_text = pygame.font.Font(None, 52).render("Quit", True, (255, 255, 0))
        quit_rect = quit_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 120))
    screen.blit(quit_text, quit_rect)
    
    return start_rect, help_rect, quit_rect

def draw_help_screen():
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 46)
    title_font = pygame.font.Font(None, 74)
    
    # Título
    title = title_font.render("Controls", True, (255, 255, 255))
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))
    
    # Controles
    controls = [
        "Move Left: LEFT ARROW",
        "Move Right: RIGHT ARROW",
        "Shoot: SPACE",
        "",
        "Collect power-ups to get double shot!",
        "Survive all waves to win!"
    ]
    
    y = HEIGHT//3
    for line in controls:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, y))
        y += 50
    
    # Botón Back
    back_text = font.render("Back to Menu", True, (255, 255, 255))
    back_rect = back_text.get_rect(center=(WIDTH//2, HEIGHT - 100))
    
    # Efecto hover para el botón Back
    mouse_pos = pygame.mouse.get_pos()
    if back_rect.collidepoint(mouse_pos):
        back_text = pygame.font.Font(None, 52).render("Back to Menu", True, (255, 255, 0))
        back_rect = back_text.get_rect(center=(WIDTH//2, HEIGHT - 100))
    
    screen.blit(back_text, back_rect)
    return back_rect

# Estado del juego
game_state = "menu"  # Puede ser "menu", "playing" o "help"

# Bucle principal del juego
running = True
while running:
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()

    if game_state == "menu":
        # Dibujar menú
        start_rect, help_rect, quit_rect = draw_menu()
        
        # Manejar eventos del menú
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_pos):
                    game_state = "playing"
                    # Reiniciar variables del juego
                    score = 0
                    current_wave = 1
                    enemies_in_wave = 0
                    wave_transition = True
                    wave_transition_timer = 0
                    # Limpiar grupos de sprites
                    all_sprites.empty()
                    enemies.empty()
                    bullets.empty()
                    buffs.empty()
                    # Crear nuevo jugador
                    player = Player()
                    all_sprites.add(player)
                elif help_rect.collidepoint(mouse_pos):
                    game_state = "help"
                elif quit_rect.collidepoint(mouse_pos):
                    running = False
        
        pygame.display.flip()
        continue
    
    elif game_state == "help":
        back_rect = draw_help_screen()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    game_state = "menu"
        
        pygame.display.flip()
        continue

    # El resto del código del juego solo se ejecuta si game_state == "playing"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Disparar con la tecla espacio
        if event.type == pygame.KEYDOWN and not wave_transition:
            if event.key == pygame.K_SPACE:
                if player.double_shot:
                    # Crear dos balas paralelas
                    bullet1 = Bullet(player.rect.centerx - 20, player.rect.top)  # Bala izquierda
                    bullet2 = Bullet(player.rect.centerx + 20, player.rect.top)  # Bala derecha
                    all_sprites.add(bullet1, bullet2)
                    bullets.add(bullet1, bullet2)
                    shoot_sound.play()
                else:
                    # Disparo normal
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

    # Generar buff cuando el score alcanza múltiplos de 1000
    if score > 0 and score % 1000 == 0 and len(buffs) == 0:
        buff = Buff()
        all_sprites.add(buff)
        buffs.add(buff)
    
    # Colisión del jugador con el buff
    buff_hits = pygame.sprite.spritecollide(player, buffs, True)
    if buff_hits:
        player.double_shot = True
        player.double_shot_timer = pygame.time.get_ticks()  # Iniciar el temporizador

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

