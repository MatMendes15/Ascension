import pygame

class FundoParallax:
    def __init__(self):
        self.largura_tela = 800
        self.altura_tela = 400
        
        self.camadas = [
            {
                'imagem': pygame.image.load('assets/imagens/fundo/fundo_1.png').convert_alpha(),
                'posicao': 0,
                'velocidade': 1
            },
            {
                'imagem': pygame.image.load('assets/imagens/fundo/fundo_2.png').convert_alpha(),
                'posicao': 0,
                'velocidade': 2
            },
            {
                'imagem': pygame.image.load('assets/imagens/fundo/fundo_3.png').convert_alpha(),
                'posicao': 0,
                'velocidade': 3
            },
            {
                'imagem': pygame.image.load('assets/imagens/fundo/fundo_4.png').convert_alpha(),
                'posicao': 0,
                'velocidade': 4
            },
            {
                'imagem': pygame.image.load('assets/imagens/fundo/fundo_5.png').convert_alpha(),
                'posicao': 0,
                'velocidade': 5
            }
        ]
        
        self.chao = pygame.image.load('assets/imagens/fundo/grama_piso.png').convert_alpha()
        
        for camada in self.camadas:
            camada['imagem'] = pygame.transform.scale(
                camada['imagem'], 
                (self.largura_tela, self.altura_tela)
            )
            
        altura_chao = 70
        self.chao = pygame.transform.scale(
            self.chao, 
            (self.largura_tela, altura_chao)
        )
        self.posicao_chao = 200
        self.altura_chao = self.altura_tela - altura_chao

    def update(self):
        for camada in self.camadas:
            camada['posicao'] -= camada['velocidade']
            if camada['posicao'] <= -self.largura_tela:
                camada['posicao'] = 0
                
        self.posicao_chao -= 5
        if self.posicao_chao <= -self.largura_tela:
            self.posicao_chao = 0

    def draw(self, tela):
        for camada in self.camadas:
            tela.blit(camada['imagem'], (camada['posicao'], 0))
            tela.blit(camada['imagem'], (camada['posicao'] + self.largura_tela, 0))
            
        tela.blit(self.chao, (self.posicao_chao, self.altura_chao))
        tela.blit(self.chao, (self.posicao_chao + self.largura_tela, self.altura_chao))