import pygame
from utilidades.portal import Portal

class FundoParallax:
    def __init__(self):
        self.largura_tela = 800
        self.altura_tela = 400

        # Carrega as camadas dos cenários
        self.scenarios = {
            'floresta': [
                {'imagem': pygame.image.load('assets/imagens/fundo/floresta/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/floresta/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/floresta/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/floresta/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
                {'imagem': pygame.image.load('assets/imagens/fundo/floresta/fundo_5.png').convert_alpha(), 'posicao': 0, 'velocidade': 5},
            ],
            'ceu': [
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu/fundo_5.png').convert_alpha(), 'posicao': 0, 'velocidade': 5},
            ],
            'campo2': [
                {'imagem': pygame.image.load('assets/imagens/fundo/campo2/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/campo2/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/campo2/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/campo2/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
            ],
            'campo3': [
                {'imagem': pygame.image.load('assets/imagens/fundo/campo3/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/campo3/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/campo3/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/campo3/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/campo3/fundo_5.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/campo3/fundo_6.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
                {'imagem': pygame.image.load('assets/imagens/fundo/campo3/fundo_7.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
            ],
            'ceu2': [
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu2/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu2/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu2/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu2/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
            ],
            'ceu3': [
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu3/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu3/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu3/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu3/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu3/fundo_5.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
            ],
            'ceu4': [
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu4/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu4/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu4/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu4/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
            ],
            'ceu5': [
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu5/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu5/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu5/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu5/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu5/fundo_5.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu5/fundo_6.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
            ],
            'ceu6': [
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu6/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu6/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu6/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu6/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
            ],
            'ceu7': [
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu7/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu7/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu7/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu7/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
            ],
            'ceu8': [
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu8/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu8/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu8/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/ceu8/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
            ],
        }

        # Ordem dos cenários
        self.scenario_order = ['floresta', 'campo2', 'campo3', 'ceu', 'ceu2', 'ceu3', 'ceu4', 'ceu5', 'ceu6', 'ceu7', 'ceu8']
        self.current_scenario_index = 0
        self.current_scenario = self.scenario_order[self.current_scenario_index]
        self.camadas = self.scenarios[self.current_scenario]

        # Redimensiona as imagens
        for scenario in self.scenarios.values():
            for camada in scenario:
                camada['imagem'] = pygame.transform.scale(camada['imagem'], (self.largura_tela, self.altura_tela))

        # Configura o chão
        self.chao = pygame.image.load('assets/imagens/fundo/grama_piso.png').convert_alpha()
        altura_chao = 70
        self.chao = pygame.transform.scale(self.chao, (self.largura_tela, altura_chao))
        self.posicao_chao = 0
        self.altura_chao = self.altura_tela - altura_chao

        # Controle de tempo para trocar o cenário
        self.tempo_ultimo_cenario = pygame.time.get_ticks()
        self.intervalo_cenario = 30000  # 30 segundos em milissegundos

        # Gerenciamento do portal
        self.portal_group = pygame.sprite.Group()
        self.portal_active = False
        self.tempo_portal_mostrar = 5000  # Portal aparece 5 segundos antes
        self.tempo_portal_inicio = 0

    def update(self):
        # Atualiza as posições das camadas
        for camada in self.camadas:
            camada['posicao'] -= camada['velocidade']
            if camada['posicao'] <= -self.largura_tela:
                camada['posicao'] = 0

        self.posicao_chao -= 5
        if self.posicao_chao <= -self.largura_tela:
            self.posicao_chao = 0

        tempo_atual = pygame.time.get_ticks()

        # Verifica se é hora de mostrar o portal
        if (tempo_atual - self.tempo_ultimo_cenario >= self.intervalo_cenario - self.tempo_portal_mostrar) and not self.portal_active:
            self.spawn_portal()
            self.portal_active = True
            self.tempo_portal_inicio = tempo_atual

        # Remove o portal após a troca de cenário
        if tempo_atual - self.tempo_portal_inicio >= self.tempo_portal_mostrar and self.portal_active:
            self.portal_group.empty()
            self.portal_active = False
            # Caso queira forçar a troca de cenário mesmo sem interação:
            # self.alternar_cenario()
            # self.tempo_ultimo_cenario = tempo_atual

        # Atualiza o portal
        self.portal_group.update()

    def draw(self, tela):
        # Desenha as camadas do cenário atual
        for camada in self.camadas:
            tela.blit(camada['imagem'], (camada['posicao'], 0))
            tela.blit(camada['imagem'], (camada['posicao'] + self.largura_tela, 0))

        # Desenha o chão
        tela.blit(self.chao, (self.posicao_chao, self.altura_chao))
        tela.blit(self.chao, (self.posicao_chao + self.largura_tela, self.altura_chao))

        # Desenha o portal
        self.portal_group.draw(tela)

    def spawn_portal(self):
        # Define a posição do portal
        self.altura_portal = 195
        portal_pos = (self.largura_tela - 220, self.altura_portal)
        portal = Portal(position=portal_pos)
        self.portal_group.add(portal)

    def alternar_cenario(self):
        # Avança para o próximo cenário na lista
        self.current_scenario_index = (self.current_scenario_index + 1) % len(self.scenario_order)
        self.current_scenario = self.scenario_order[self.current_scenario_index]
        self.camadas = self.scenarios[self.current_scenario]

        # Reseta as posições das camadas
        for camada in self.camadas:
            camada['posicao'] = 0
        self.posicao_chao = 0