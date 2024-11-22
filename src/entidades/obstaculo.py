import pygame
from random import randint

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, tipo, velocidade):
        super().__init__()
        if tipo == 'morcego':
            morcego_1 = pygame.image.load('assets/imagens/inimigo_voador/morcego_1.png').convert_alpha()
            morcego_2 = pygame.image.load('assets/imagens/inimigo_voador/morcego_2.png').convert_alpha()
            self.frames = [morcego_1, morcego_2]
            pos_y = 270
        elif tipo == 'cogumelo':
            cogumelo_1 = pygame.image.load('assets/imagens/inimigo_terrestre/cogumelo_1.png').convert_alpha()
            cogumelo_2 = pygame.image.load('assets/imagens/inimigo_terrestre/cogumelo_2.png').convert_alpha()
            self.frames = [cogumelo_1, cogumelo_2]
            pos_y = 340
        elif tipo == 'fantasma':
            fantasma_1 = pygame.image.load('assets/imagens/inimigo_voador/fantasma_1.png').convert_alpha()
            fantasma_2 = pygame.image.load('assets/imagens/inimigo_voador/fantasma_2.png').convert_alpha()
            self.frames = [fantasma_1, fantasma_2]
            pos_y = 270
        elif tipo == 'bicho':
            bicho_1 = pygame.image.load('assets/imagens/inimigo_terrestre/bicho_1.png').convert_alpha()
            bicho_2 = pygame.image.load('assets/imagens/inimigo_terrestre/bicho_2.png').convert_alpha()
            self.frames = [bicho_1, bicho_2]
            pos_y = 340
        elif tipo == 'monstro':
            monstro_1 = pygame.image.load('assets/imagens/inimigo_voador/monstro_1.png').convert_alpha()
            monstro_2 = pygame.image.load('assets/imagens/inimigo_voador/monstro_2.png').convert_alpha()
            self.frames = [monstro_1, monstro_2]
            pos_y = 260
        elif tipo == 'alien':
            alien_1 = pygame.image.load('assets/imagens/inimigo_terrestre/alien_1.png').convert_alpha()
            alien_2 = pygame.image.load('assets/imagens/inimigo_terrestre/alien_2.png').convert_alpha()
            self.frames = [alien_1, alien_2]
            pos_y = 350
        else:
            # Caso padrão, se o tipo não for reconhecido
            cogumelo_1 = pygame.image.load('assets/imagens/inimigo_terrestre/cogumelo_1.png').convert_alpha()
            cogumelo_2 = pygame.image.load('assets/imagens/inimigo_terrestre/cogumelo_2.png').convert_alpha()
            self.frames = [cogumelo_1, cogumelo_2]
            pos_y = 340

        self.indice_animacao = 0
        self.image = self.frames[self.indice_animacao]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), pos_y))
        self.velocidade = velocidade

    def animation_state(self):
        self.indice_animacao += 0.1
        if self.indice_animacao >= len(self.frames):
            self.indice_animacao = 0
        self.image = self.frames[int(self.indice_animacao)]

    def update(self):
        self.animation_state()
        self.rect.x -= self.velocidade
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()