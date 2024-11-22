import pygame
from random import choice
from entidades.jogador import Jogador
from entidades.obstaculo import Obstaculo
from utilidades.fundoParallax import FundoParallax
from utilidades.pauseMenu import PauseMenu
from utilidades.gameOverMenu import GameOverMenu

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Ascension')
        self.relogio = pygame.time.Clock()
        self.fonte_pixel = pygame.font.Font('assets/fontes/PressStart2PFont.ttf', 20)
        
        self.jogo_ativo = True
        self.game_over = False
        self.paused = False
        self.tempo_inicio = 0
        self.pontuacao = 0

        self.musica_fundo = pygame.mixer.Sound('assets/audio/Lost Highway.mp3')
        self.musica_fundo.play(loops=-1)

        self.jogador = pygame.sprite.GroupSingle()
        self.jogador.add(Jogador())
        self.grupo_obstaculos = pygame.sprite.Group()

        self.fundo = FundoParallax()

        self.game_name = self.fonte_pixel.render('Ascension', False, (111, 196, 169))
        self.game_name_rect = self.game_name.get_rect(center=(400, 80))

        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)

        self.velocidade_obstaculos = 6  # Velocidade inicial dos obstáculos ajustada

        self.paused = False
        self.pause_menu = PauseMenu(self.tela)
        self.game_over_menu = GameOverMenu(self.tela)
        self.quit_game = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.jogo_ativo:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused  # Alterna o estado de pausa
                        if self.paused:
                            self.fundo.pausar()  # Pause background
                            pygame.mixer.music.pause()
                        else:
                            self.fundo.despausar()  # Unpause background
                            pygame.mixer.music.unpause()
                    elif not self.paused:
                        # Controles do jogo quando não está pausado
                        if event.key == pygame.K_UP and self.jogador.sprite.rect.bottom >= self.jogador.sprite.altura_chao:
                            self.jogador.sprite.gravidade = -23
                            self.jogador.sprite.som_pulo.play()

                if event.type == self.obstacle_timer and not self.paused:
                    current_scenario_index = self.fundo.current_scenario_index

                    if current_scenario_index in [0, 1, 2]:  # 'floresta', 'campo2', 'campo3'
                        possible_obstacles = ['morcego', 'cogumelo']
                    elif current_scenario_index in range(3, 11):  # 'ceu' até 'ceu8'
                        possible_obstacles = ['fantasma', 'bicho']
                    elif current_scenario_index == 11:  # 'espaco'
                        possible_obstacles = ['monstro', 'alien']
                    else:
                        # Caso padrão, se o índice do cenário não corresponder a nenhum dos anteriores
                        possible_obstacles = ['morcego', 'cogumelo']

                    tipo_obstaculo = choice(possible_obstacles)
                    novo_obstaculo = Obstaculo(tipo_obstaculo, self.velocidade_obstaculos)
                    self.grupo_obstaculos.add(novo_obstaculo)

                if self.paused:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.pause_menu.navigate(-1)
                        elif event.key == pygame.K_DOWN:
                            self.pause_menu.navigate(1)
                        elif event.key == pygame.K_RETURN:
                            selection = self.pause_menu.select()
                            if selection == 'Continuar':
                                self.paused = False
                                self.fundo.despausar()  # Adicionar esta linha
                                pygame.mixer.music.unpause()
                            elif selection == 'Reiniciar':
                                self.start_game()
                                self.paused = False
                                self.fundo.despausar()
                            elif selection == 'Menu Principal':
                                self.quit_game = True  # Sinaliza para sair do loop
                                self.paused = False
            else:
                if self.game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.game_over_menu.navigate(-1)
                        elif event.key == pygame.K_DOWN:
                            self.game_over_menu.navigate(1)
                        elif event.key == pygame.K_RETURN:
                            selection = self.game_over_menu.select()
                            if selection == 'Reiniciar':
                                self.start_game()
                            elif selection == 'Menu Principal':
                                self.quit_game = True  # Sinaliza para sair do loop
                else:
                    pass

    def run(self):
        while not self.quit_game:
            self.events()
            if self.jogo_ativo:
                if self.paused:
                    self.update_pause_menu()
                else:
                    self.update_game()
            else:
                self.update_menu()
            pygame.display.update()
            self.relogio.tick(60)

    def update_game(self):
        # Índices onde a velocidade deve ser incrementada
        indices_incremento = [4, 10]
        
        # Calcula o número de incrementos com base no cenário atual
        incrementos = sum(1 for indice in indices_incremento if self.fundo.current_scenario_index >= indice)
        
        # Define a velocidade dos obstáculos
        self.velocidade_obstaculos = 6 + incrementos

        self.fundo.update()
        self.fundo.draw(self.tela)
        
        self.display_score()
        self.jogador.draw(self.tela)
        self.jogador.update()
        self.grupo_obstaculos.draw(self.tela)
        self.grupo_obstaculos.update()

        # Mostra a barra de carregamento do golpe
        self.desenhar_barra_carregamento()

        # Verifica colisão com o portal
        if self.fundo.portal_active:
            colisao_portal = pygame.sprite.spritecollide(self.jogador.sprite, self.fundo.portal_group, False)
            if colisao_portal:
                self.pontuacao += 1
                self.fundo.alternar_cenario()
                # Removida a atribuição do tempo_ultimo_cenario aqui
                self.fundo.portal_group.empty()
                self.portal_active = False

        # Verifica colisão com obstáculos
        colisao = pygame.sprite.spritecollide(self.jogador.sprite, self.grupo_obstaculos, False)
        if colisao:
            if self.jogador.sprite.pode_atacar:
                self.jogador.sprite.fazendo_ataque = True
                self.jogador.sprite.pode_atacar = False
                self.jogador.sprite.tempo_ultimo_ataque = pygame.time.get_ticks()

                self.jogador.sprite.indice_barra = 0

                for obstaculo in colisao:
                    obstaculo.kill()
            else:
                self.jogo_ativo = False
                self.game_over = True

    def update_menu(self):
        if self.game_over:
            # Mostra estado atual do jogo congelado
            self.fundo.draw(self.tela)
            self.jogador.draw(self.tela)
            self.grupo_obstaculos.draw(self.tela)
            self.display_score()
            self.desenhar_barra_carregamento()
            # Exibe o menu de fim de jogo
            self.game_over_menu.display_menu()

    def display_score(self):
        score_surf = self.fonte_pixel.render(f'Pontuação: {self.pontuacao}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(670, 35))
        self.tela.blit(score_surf, score_rect)

   # def verificar_incremento_dificuldade(self):
       # tempo_atual = pygame.time.get_ticks()
       # if tempo_atual - self.tempo_ultimo_incremento >= self.intervalo_incremento:
         #   self.velocidade_obstaculos += 1
          #  self.tempo_ultimo_incremento = tempo_atual

    def desenhar_barra_carregamento(self):
        barra_image = self.jogador.sprite.barra_carregamento_frames[self.jogador.sprite.indice_barra]
        barra_rect = barra_image.get_rect(center=(170, 35))
        self.tela.blit(barra_image, barra_rect)

    def update_pause_menu(self):
        # Mostra estado atual do jogo congelado
        self.fundo.draw(self.tela)
        self.jogador.draw(self.tela)
        self.grupo_obstaculos.draw(self.tela)
        self.display_score()
        self.desenhar_barra_carregamento()
        # Exibe o menu de pausa
        self.pause_menu.display_menu()

    def start_game(self):
        self.jogo_ativo = True
        self.paused = False
        self.game_over = False
        self.tempo_inicio = int(pygame.time.get_ticks() / 1000)
        self.pontuacao = 0
        self.grupo_obstaculos.empty()
        self.jogador.sprite.rect.midbottom = (80, self.jogador.sprite.altura_chao)
        self.jogador.sprite.gravidade = 0

        # Reinicia o cenário e a velocidade
        self.fundo.current_scenario_index = 0
        self.fundo.current_scenario = self.fundo.scenario_order[0]
        self.fundo.camadas = self.fundo.scenarios[self.fundo.current_scenario]
        self.velocidade_obstaculos = 6  # Reinicia para a velocidade inicial

        self.fundo.portal_active = False
        self.fundo.portal_group.empty()
        self.fundo.tempo_ultimo_cenario = pygame.time.get_ticks()
        self.fundo.update_floor_image()