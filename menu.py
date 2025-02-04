import pygame
from config import WIDTH, HEIGHT
import os

class Menu:
    def __init__(self):
        # Cargar imágenes del menú y UI
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.font = pygame.font.Font(None, 36)
        # self.start_button_img = pygame.image.load("assets/start.png")
        self.start_button_img = pygame.image.load(os.path.join(BASE_DIR, "assets", "start.png"))
        self.start_button_img = pygame.transform.scale(self.start_button_img, (200, 80))
        self.start_button_hover = pygame.transform.scale(self.start_button_img, (220, 88))
        # self.pause_button_img = pygame.image.load("assets/pause.png")
        self.pause_button_img = pygame.image.load(os.path.join(BASE_DIR, "assets", "pause.png"))
        self.pause_button_img = pygame.transform.scale(self.pause_button_img, (40, 40))
        # self.background = pygame.image.load("assets/background.jpg")
        self.background = pygame.image.load(os.path.join(BASE_DIR, "assets", "background.jpg"))
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    def draw_menu(self, screen):
        screen.blit(self.background, (0, 0))
        title_font = pygame.font.Font(None, 74)
        button_font = pygame.font.Font(None, 46)
        
        # Título del juego
        title = title_font.render("Void Requiem: The Last Stand", True, (255, 255, 255))
        title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//3))
        screen.blit(title, title_rect)
        
        # Obtener posición del mouse
        mouse_pos = pygame.mouse.get_pos()
        
        # Botón de inicio con imagen
        start_rect = self.start_button_img.get_rect(center=(WIDTH//2, HEIGHT//2))
        if start_rect.collidepoint(mouse_pos):
            hover_rect = self.start_button_hover.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(self.start_button_hover, hover_rect)
            start_rect = hover_rect
        else:
            screen.blit(self.start_button_img, start_rect)
        
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

    def draw_help_screen(self, screen):
        screen.blit(self.background, (0, 0))
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

    def draw_pause_button(self, screen):
        pause_rect = self.pause_button_img.get_rect()
        pause_rect.topright = (WIDTH - 10, 10)
        screen.blit(self.pause_button_img, pause_rect)
        
        pause_font = pygame.font.Font(None, 24)
        pause_text = pause_font.render("Pause", True, (255, 255, 255))
        text_rect = pause_text.get_rect()
        text_rect.centerx = pause_rect.centerx
        text_rect.top = pause_rect.bottom + 5
        screen.blit(pause_text, text_rect)
        
        return pause_rect

    def draw_pause_screen(self, screen):
        s = pygame.Surface((WIDTH, HEIGHT))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        screen.blit(s, (0, 0))
        
        font = pygame.font.Font(None, 74)
        text = font.render("PAUSED", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)
        
        continue_font = pygame.font.Font(None, 46)
        continue_text = continue_font.render("Click anywhere to continue", True, (255, 255, 255))
        continue_rect = continue_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 60))
        screen.blit(continue_text, continue_rect) 