# Python
import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        # Carrega os frames de animação do portal
        self.frames = []
        for i in range(1, 8):
            frame = pygame.image.load(f'assets/imagens/objetos/portal_{i}.png').convert_alpha()
            self.frames.append(frame)
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(center=position)
        self.animation_speed = 0.1

    def update(self):
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]