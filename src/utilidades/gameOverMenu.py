# src/utilidades/gameOverMenu.py

import pygame

class GameOverMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('assets/fontes/PressStart2PFont.ttf', 30)
        self.options = ['Reiniciar', 'Menu Principal']
        self.selected_option = 0

    def display_menu(self):
        # Escurece o fundo
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        message = self.font.render('Você Perdeu!', True, (255, 0, 0))
        message_rect = message.get_rect(center=(self.screen.get_width() // 2, 150))
        self.screen.blit(message, message_rect)

        # Exibe as opções
        for index, option in enumerate(self.options):
            if index == self.selected_option:
                color = (255, 255, 0)  # Opção selecionada em amarelo
            else:
                color = (255, 255, 255)
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, 250 + index * 60))
            self.screen.blit(text, text_rect)

    def navigate(self, direction):
        self.selected_option = (self.selected_option + direction) % len(self.options)
        print(f"Navegar para: {self.options[self.selected_option]}")  # Debug

    def select(self):
        selection = self.options[self.selected_option]
        print(f"Selecionado: {selection}")  # Debug
        return selection