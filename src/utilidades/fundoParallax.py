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
            'espaco': [
                {'imagem': pygame.image.load('assets/imagens/fundo/espaco/fundo_8.png').convert_alpha(), 'posicao': 0, 'velocidade': 1},
                {'imagem': pygame.image.load('assets/imagens/fundo/espaco/fundo_7.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/espaco/fundo_6.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/espaco/fundo_5.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
                {'imagem': pygame.image.load('assets/imagens/fundo/espaco/fundo_4.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/espaco/fundo_3.png').convert_alpha(), 'posicao': 0, 'velocidade': 3},
                {'imagem': pygame.image.load('assets/imagens/fundo/espaco/fundo_2.png').convert_alpha(), 'posicao': 0, 'velocidade': 4},
                {'imagem': pygame.image.load('assets/imagens/fundo/espaco/fundo_1.png').convert_alpha(), 'posicao': 0, 'velocidade': 2},
            ]
        }

        # Ordem dos cenários
        self.scenario_order = ['floresta', 'campo2', 'campo3', 'ceu', 'ceu2', 'ceu3', 'ceu4', 'ceu5', 'ceu6', 'ceu7', 'ceu8', 'espaco']
        self.current_scenario_index = 0
        self.current_scenario = self.scenario_order[self.current_scenario_index]
        self.camadas = self.scenarios[self.current_scenario]

        # Redimensiona as imagens
        for scenario in self.scenarios.values():
            for camada in scenario:
                camada['imagem'] = pygame.transform.scale(camada['imagem'], (self.largura_tela, self.altura_tela))

        # Inicializa o chão
        self.update_floor_image()
        self.posicao_chao = 0

        # Controle de tempo para trocar o cenário
        self.tempo_ultimo_cenario = pygame.time.get_ticks()
        self.intervalo_cenario = 8000  # 8 segundos em milissegundos

        # Gerenciamento do portal
        self.portal_group = pygame.sprite.Group()
        self.portal_active = False
        self.tempo_portal_mostrar = 5000  # Portal aparece 5 segundos antes
        self.tempo_portal_inicio = 0

        self.tempo_pausa_inicio = 0
        self.tempo_pausa_total = 0
        self.pausado = False

    def update_floor_image(self):
        if self.current_scenario_index in [0, 1, 2]:  # 'floresta', 'campo2', 'campo3'
            floor_image_name = 'grama_piso.png'
        elif self.current_scenario_index == 3:
            floor_image_name = 'nuvens_piso0.png'    
        elif self.current_scenario_index in range(3, 6):  # 'ceu' até 'ceu3'
            floor_image_name = 'nuvens_piso.png'
        elif self.current_scenario_index in range(6, 9):  # 'ceu4' até 'ceu6'
            floor_image_name = 'nuvens_piso1.png'
        elif self.current_scenario_index == 9:
            floor_image_name = 'nuvens_piso2.png'
        elif self.current_scenario_index == 10:
            floor_image_name = 'nuvens_piso3.png'
        elif self.current_scenario_index == 11:
            floor_image_name = 'lua_piso.png'
        else:
            floor_image_name = 'grama_piso.png'

        self.chao = pygame.image.load(f'assets/imagens/fundo/{floor_image_name}').convert_alpha()
        altura_chao = 70
        self.chao = pygame.transform.scale(self.chao, (self.largura_tela, altura_chao))
        self.altura_chao = self.altura_tela - altura_chao

    def pausar(self):
        if not self.pausado:
            self.pausado = True
            self.tempo_pausa_inicio = pygame.time.get_ticks()

    def despausar(self):
        if self.pausado:
            self.pausado = False
            tempo_atual = pygame.time.get_ticks()
            tempo_pausado = tempo_atual - self.tempo_pausa_inicio
            self.tempo_pausa_total += tempo_pausado
            
            # Define o tempo do último cenário para o tempo atual menos o tempo total de pausa
            self.tempo_ultimo_cenario = tempo_atual - self.tempo_pausa_total
            
            # Se o portal estiver ativo, ajusta seu tempo também
            if self.portal_active:
                self.tempo_portal_inicio += tempo_pausado

    def update(self):
        if not self.pausado:
            tempo_atual = pygame.time.get_ticks()
            tempo_ajustado = tempo_atual - self.tempo_pausa_total
            tempo_desde_ultimo_cenario = tempo_ajustado - self.tempo_ultimo_cenario

            # Reduzir os prints de debug
            print(f"DEBUG: tempo_desde_ultimo={tempo_desde_ultimo_cenario}, intervalo={self.intervalo_cenario}")
            
            # Verifica se é hora de mostrar o portal (3 segundos antes do fim do intervalo)
            if (not self.portal_active and 
                tempo_desde_ultimo_cenario >= self.intervalo_cenario - self.tempo_portal_mostrar):
                print("DEBUG: Spawning portal!")
                self.spawn_portal()
                self.portal_active = True
                self.tempo_portal_inicio = tempo_ajustado

            # Atualiza as posições das camadas
            for camada in self.camadas:
                camada['posicao'] -= camada['velocidade']
                if camada['posicao'] <= -self.largura_tela:
                    camada['posicao'] = 0

            self.posicao_chao -= 5
            if self.posicao_chao <= -self.largura_tela:
                self.posicao_chao = 0

            # Update portal animation
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
        # Avança para o próximo cenário
        self.current_scenario_index = (self.current_scenario_index + 1) % len(self.scenario_order)
        self.current_scenario = self.scenario_order[self.current_scenario_index]
        self.camadas = self.scenarios[self.current_scenario]

        # Reset posições
        for camada in self.camadas:
            camada['posicao'] = 0
        self.posicao_chao = 0

        # Atualiza a imagem do chão
        self.update_floor_image()

        # Atualiza tempo do último cenário com tempo ajustado
        tempo_atual = pygame.time.get_ticks()
        self.tempo_ultimo_cenario = tempo_atual - self.tempo_pausa_total
        
        # Reset estado do portal
        self.portal_active = False
        self.portal_group.empty()