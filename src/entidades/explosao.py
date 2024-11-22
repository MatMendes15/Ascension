import pygame

class Explosao(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.frames = []
        for i in range(1, 12):
            frame = pygame.image.load(f'assets/imagens/efeito_morte/efeito_explosao{i}.png').convert_alpha()
            self.frames.append(frame)
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center=position)
        self.animation_speed = 0.4

    def update(self):
        self.index += self.animation_speed
        if self.index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.index)]