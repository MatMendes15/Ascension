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

        self.jogador_pulo = []
        for i in range(1, 12):
            frame = pygame.image.load(f'assets/imagens/Player/pulo/pulo_{i}.PNG').convert_alpha()
            self.jogador_pulo.append(frame)
        
        self.indice_pulo = 0

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

        self.jogador_golpe = []
        for i in range(1, 15):
            frame = pygame.image.load(f'assets/imagens/Player/golpe/golpe_{i}.PNG').convert_alpha()
            self.jogador_golpe.append(frame)
        self.indice_golpe = 0.15

        self.fazendo_ataque = False
        self.pode_atacar = True
        self.tempo_ultimo_ataque = 0
        self.cooldown_ataque = 20000 # 20 segundos

        self.barra_carregamento_frames = []
        for i in range(1, 151):  # De 1 a 151
            frame = pygame.image.load(f'assets/imagens/barra_golpe/barra_golpe{i}.png').convert_alpha()
            self.barra_carregamento_frames.append(frame)
        self.indice_barra = 0

    def entrada_jogador(self):
        teclas = pygame.key.get_pressed()
        velocidade_acelerar = 3
        velocidade_recuo = 2
        
        if teclas[pygame.K_UP] and self.rect.bottom >= self.altura_chao and not self.fazendo_rasteira:
            self.gravidade = -23
            self.som_pulo.play()
            
        if teclas[pygame.K_DOWN] and self.rect.bottom >= self.altura_chao and not self.fazendo_rasteira:
            self.fazendo_rasteira = True
            self.indice_rasteira = 0
            self.altura_chao += 35
            self.rect.bottom = self.altura_chao

        if teclas[pygame.K_RIGHT]:
            self.rect.x += velocidade_acelerar
        if teclas[pygame.K_LEFT]:
            self.rect.x -= velocidade_recuo

    def aplicar_gravidade(self):
        self.gravidade += 1
        self.rect.y += self.gravidade
        if self.rect.bottom >= self.altura_chao:
            self.rect.bottom = self.altura_chao
            self.gravidade = 0
            self.indice_pulo = 0

    def estado_animacao(self):
        if self.fazendo_ataque:
            self.indice_golpe += 0.3
            if self.indice_golpe >= len(self.jogador_golpe):
                self.indice_golpe = 0
                self.fazendo_ataque = False
            self.image = self.jogador_golpe[int(self.indice_golpe)]
        
        elif self.rect.bottom < self.altura_chao:
            self.indice_pulo += 0.32
            if self.indice_pulo >= len(self.jogador_pulo):
                self.indice_pulo = len(self.jogador_pulo) - 1
            self.image = self.jogador_pulo[int(self.indice_pulo)]
        
        elif self.fazendo_rasteira:
            self.indice_rasteira += 0.17
            if self.indice_rasteira >= len(self.jogador_rasteira):
                self.fazendo_rasteira = False
                self.indice_rasteira = 0
                self.altura_chao = self.posicao_original_chao
                self.rect.bottom = self.altura_chao
            self.image = self.jogador_rasteira[int(self.indice_rasteira)]
        
        else:
            self.indice_jogador += 0.2
            if self.indice_jogador >= len(self.jogador_andando):
                self.indice_jogador = 0
            self.image = self.jogador_andando[int(self.indice_jogador)]

    def update(self):
        self.entrada_jogador()
        self.aplicar_gravidade()
        self.atualizar_ataque()
        self.estado_animacao()
        self.atualizar_barra_carregamento()  # Atualiza a barra de carregamento

    def atualizar_ataque(self):
        if not self.pode_atacar:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.tempo_ultimo_ataque >= self.cooldown_ataque:
                self.pode_atacar = True
        else:
            self.indice_barra = len(self.barra_carregamento_frames) - 1  # Garante que a barra fique completa

    def atualizar_barra_carregamento(self):
        if not self.pode_atacar:
            tempo_atual = pygame.time.get_ticks()
            tempo_passado = tempo_atual - self.tempo_ultimo_ataque
            progresso = tempo_passado / self.cooldown_ataque
            self.indice_barra = int(progresso * (len(self.barra_carregamento_frames) - 1))
        else:
            self.indice_barra = len(self.barra_carregamento_frames) - 1