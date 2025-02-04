import pygame
import random
from config import WIDTH, HEIGHT, FPS
from player import Player
from enemy import Enemy
from bullet import Bullet
from buff import Buff
from menu import Menu

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

# Crear instancia del menú
menu = Menu()

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
    if (pygame.time.get_ticks() // 200) % 2:  # Parpadeo cada 200ms
        # Determinar el mensaje y color según la oleada
        if current_wave == 10:
            wave_text = "FINAL WAVE"
            difficulty_text = "BOSS BATTLE"
            color = (255, 0, 0)  # Rojo para el jefe
        else:
            wave_text = f"WAVE {current_wave}"
            if current_wave <= 3:
                difficulty_text = "EASY"
                color = (0, 255, 0)  # Verde
            elif current_wave <= 6:
                difficulty_text = "MEDIUM"
                color = (255, 165, 0)  # Naranja
            else:
                difficulty_text = "HARD"
                color = (255, 0, 0)  # Rojo

        # Renderizar textos
        wave_message = font.render(wave_text, True, (255, 255, 255))
        difficulty_message = font.render(difficulty_text, True, color)
        
        # Posicionar textos
        wave_rect = wave_message.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
        diff_rect = difficulty_message.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
        
        # Dibujar textos
        screen.blit(wave_message, wave_rect)
        screen.blit(difficulty_message, diff_rect)

# Estado del juego
game_state = "menu"  # Puede ser "menu", "playing", "help" o "paused"

# Bucle principal del juego
running = True
while running:
    clock.tick(FPS)
    current_time = pygame.time.get_ticks()

    if game_state == "menu":
        # Dibujar menú
        start_rect, help_rect, quit_rect = menu.draw_menu(screen)
        
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
        back_rect = menu.draw_help_screen(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    game_state = "menu"
        
        pygame.display.flip()
        continue

    elif game_state == "paused":
        menu.draw_pause_screen(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_state = "playing"
        
        pygame.display.flip()
        continue

    elif game_state == "playing":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                pause_rect = menu.draw_pause_button(screen)
                if pause_rect.collidepoint(mouse_pos):
                    game_state = "paused"
                    continue

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
            # Victoria - mostrar mensaje y volver al menú
            victory_font = pygame.font.Font(None, 48)
            victory_text = victory_font.render("¡La galaxia está a salvo gracias a tus valientes hazañas, guerrero!", True, (255, 255, 255))
            victory_rect = victory_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(victory_text, victory_rect)
            pygame.display.flip()
            pygame.time.wait(3000)  # Esperar 3 segundos
            # Reiniciar el estado del juego
            game_state = "menu"
            Enemy.boss_has_spawned = False
            continue
        else:
            # Iniciar transición a la siguiente oleada
            wave_transition = True
            wave_transition_timer = 0

    # Colisión de enemigos con el jugador (fin del juego)
    if pygame.sprite.spritecollide(player, enemies, True):
        # Mostrar mensaje de game over
        game_over_font = pygame.font.Font(None, 48)
        game_over_text = game_over_font.render("¡Game Over!", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(game_over_text, game_over_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Esperar 2 segundos
        
        # Reiniciar el juego y volver al menú
        game_state = "menu"
        Enemy.boss_has_spawned = False
        continue

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
    draw_score()
    menu.draw_pause_button(screen)
    
    # Dibujar barra de vida del jefe si existe
    for enemy in enemies:
        if hasattr(enemy, 'is_boss') and enemy.is_boss:
            enemy.draw_health_bar(screen)
    
    if wave_transition:
        draw_wave_message()

    pygame.display.flip()

    if current_wave > max_waves:
        Enemy.boss_has_spawned = False  # Reiniciar el estado del jefe

# Salir del juego
pygame.quit()

