import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.jogador_andando = []
        for i in range(1, 24):
            frame = pygame.image.load(f'assets/imagens/Player/corrida/corrida_{i}.PNG').convert_alpha()
            self.jogador_andando.append(frame)
        
        self.jogador_rasteira = []
        for i in range(1, 8):  
            frame = pygame.image.load(f'assets/imagens/Player/rasteira/rasteira_{i}.PNG').convert_alpha()
            self.jogador_rasteira.append(frame)
            
        self.indice_jogador = 0
        self.jogador_pulo = pygame.image.load('assets/imagens/Player/pulo.PNG').convert_alpha()

        self.fazendo_rasteira = False
        self.indice_rasteira = 0
        
        self.image = self.jogador_andando[self.indice_jogador]
        self.gravidade = 0

        self.som_pulo = pygame.mixer.Sound('assets/audio/jump.mp3')
        self.som_pulo.set_volume(0.5)

        self.altura_chao = 350
        self.rect = self.image.get_rect(midbottom=(80, self.altura_chao))
        self.posicao_original_chao = self.altura_chao

        self.offset_rasteira = 0

    def entrada_jogador(self):
        teclas = pygame.key.get_pressed()
        
        if teclas[pygame.K_UP] and self.rect.bottom >= self.altura_chao and not self.fazendo_rasteira:
            self.gravidade = -23
            self.som_pulo.play()
            
        if teclas[pygame.K_DOWN] and self.rect.bottom >= self.altura_chao and not self.fazendo_rasteira:
            self.fazendo_rasteira = True
            self.indice_rasteira = 0
            self.altura_chao += 35  # Desce 5 pixels
            self.rect.bottom = self.altura_chao

    def aplicar_gravidade(self):
        self.gravidade += 1
        self.rect.y += self.gravidade
        if self.rect.bottom >= self.altura_chao:
            self.rect.bottom = self.altura_chao

    def estado_animacao(self):
        if self.rect.bottom < self.altura_chao:
            self.image = self.jogador_pulo
        elif self.fazendo_rasteira:
            self.indice_rasteira += 0.17
            if self.indice_rasteira >= len(self.jogador_rasteira):
                self.fazendo_rasteira = False
                self.indice_rasteira = 0
                self.altura_chao = self.posicao_original_chao  # Retorna à posição original
                self.rect.bottom = self.altura_chao
                self.image = self.jogador_andando[int(self.indice_jogador)]
            else:
                self.image = self.jogador_rasteira[int(self.indice_rasteira)]
        else:
            self.indice_jogador += 0.2
            if self.indice_jogador >= len(self.jogador_andando):
                self.indice_jogador = 0
            self.image = self.jogador_andando[int(self.indice_jogador)]

    def update(self):
        self.entrada_jogador()
        self.aplicar_gravidade()
        self.estado_animacao()