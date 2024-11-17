import pygame
from random import randint

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        if tipo == 'morcego':
            morcego_1 = pygame.image.load('assets/imagens/inimigo_voador/morcego_1.png').convert_alpha()
            morcego_2 = pygame.image.load('assets/imagens/inimigo_voador/morcego_2.png').convert_alpha()
            self.frames = [morcego_1, morcego_2]
            pos_y = 270
        else:
            cogumelo_1 = pygame.image.load('assets/imagens/inimigo_terrestre/cogumelo_1.png').convert_alpha()
            cogumelo_2 = pygame.image.load('assets/imagens/inimigo_terrestre/cogumelo_2.png').convert_alpha()
            self.frames = [cogumelo_1, cogumelo_2]
            pos_y = 340

        self.indice_animacao = 0
        self.image = self.frames[self.indice_animacao]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), pos_y))

    def animation_state(self):
        self.indice_animacao += 0.1
        if self.indice_animacao >= len(self.frames):
            self.indice_animacao = 0
        self.image = self.frames[int(self.indice_animacao)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()