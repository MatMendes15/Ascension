import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.jogador_andando = []
        for i in range(1, 24):  # loop de 1 a 24 da personagem correndo
            frame = pygame.image.load(f'assets/imagens/Player/corrida/corrida_{i}.PNG').convert_alpha()
            self.jogador_andando.append(frame)
            
        self.indice_jogador = 0
        self.jogador_pulo = pygame.image.load('assets/imagens/Player/pulo.PNG').convert_alpha()

        self.image = self.jogador_andando[self.indice_jogador]
        self.gravidade = 0

        self.som_pulo = pygame.mixer.Sound('assets/audio/jump.mp3')
        self.som_pulo.set_volume(0.5)

        self.altura_chao = 350
        self.rect = self.image.get_rect(midbottom=(80, self.altura_chao))

    def entrada_jogador(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and self.rect.bottom >= self.altura_chao:
            self.gravidade = -23
            self.som_pulo.play()

    def aplicar_gravidade(self):
        self.gravidade += 1
        self.rect.y += self.gravidade
        if self.rect.bottom >= self.altura_chao:
            self.rect.bottom = self.altura_chao

    def estado_animacao(self):
        if self.rect.bottom < 300:
            self.image = self.jogador_pulo
        else:
            self.indice_jogador += 0.2  # Quanto menor o valor, mais lenta a animação
            if self.indice_jogador >= len(self.jogador_andando):
                self.indice_jogador = 0
            self.image = self.jogador_andando[int(self.indice_jogador)]

    def update(self):
        self.entrada_jogador()
        self.aplicar_gravidade()
        self.estado_animacao()