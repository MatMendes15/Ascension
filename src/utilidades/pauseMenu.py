# src/utilidades/pause_menu.py

import pygame

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('assets/fontes/PressStart2PFont.ttf', 30)
        self.options = ['Continuar', 'Reiniciar', 'Menu Principal']
        self.selected_option = 0

    def display_menu(self):
        # Escurece o fundo
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))  # Preto semi-transparente
        self.screen.blit(overlay, (0, 0))

        # Exibe as opções
        for index, option in enumerate(self.options):
            if index == self.selected_option:
                color = (255, 255, 0)  # Opção selecionada em amarelo
            else:
                color = (255, 255, 255)
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, 200 + index * 60))
            self.screen.blit(text, text_rect)

    def navigate(self, direction):
        self.selected_option = (self.selected_option + direction) % len(self.options)

    def select(self):
        return self.options[self.selected_option]