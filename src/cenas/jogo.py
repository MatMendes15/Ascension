import pygame
from random import choice
from entidades.jogador import Jogador
from entidades.obstaculo import Obstaculo
from utilidades.fundoParallax import FundoParallax

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Ascension')
        self.relogio = pygame.time.Clock()
        self.fonte_pixel = pygame.font.Font('assets/fontes/PressStart2PFont.ttf', 20)
        self.jogo_ativo = False
        self.tempo_inicio = 0
        self.pontuacao = 0

        self.musica_fundo = pygame.mixer.Sound('assets/audio/Running From My Shadow.mp3')
        self.musica_fundo.play(loops=-1)

        self.jogador = pygame.sprite.GroupSingle()
        self.jogador.add(Jogador())
        self.grupo_obstaculos = pygame.sprite.Group()

        self.fundo = FundoParallax()

        player_stand = pygame.image.load('assets/imagens/Player/fundo_aguardando.png').convert_alpha()
        self.player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
        self.player_stand_rect = self.player_stand.get_rect(center=(400, 200))
        self.game_name = self.fonte_pixel.render('Ascension', False, (111, 196, 169))
        self.game_name_rect = self.game_name.get_rect(center=(400, 80))
        self.game_message = self.fonte_pixel.render('Pressione seta para iniciar', False, (111, 196, 169))
        self.game_message_rect = self.game_message.get_rect(center=(400, 330))

        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)

    def run(self):
        while True:
            self.events()
            if self.jogo_ativo:
                self.update_game()
            else:
                self.update_menu()
            pygame.display.update()
            self.relogio.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if self.jogo_ativo:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.jogador.sprite.rect.bottom >= 300:
                        self.jogador.sprite.gravidade = -20
                if event.type == self.obstacle_timer:
                    self.grupo_obstaculos.add(Obstaculo(choice(['morcego', 'cogumelo', 'cogumelo', 'cogumelo'])))
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.start_game()

    def start_game(self):
        self.jogo_ativo = True
        self.tempo_inicio = int(pygame.time.get_ticks() / 1000)
        self.pontuacao = 0
        self.grupo_obstaculos.empty()
        self.jogador.sprite.rect.midbottom = (80, 300)
        self.jogador.sprite.gravidade = 0

    def update_game(self):
        self.fundo.update()
        self.fundo.draw(self.tela)
        
        self.pontuacao = self.display_score()
        self.jogador.draw(self.tela)
        self.jogador.update()
        self.grupo_obstaculos.draw(self.tela)
        self.grupo_obstaculos.update()

        if pygame.sprite.spritecollide(self.jogador.sprite, self.grupo_obstaculos, False):
            self.jogo_ativo = False

    def update_menu(self):
        self.tela.fill((94, 129, 162))
        self.tela.blit(self.player_stand, self.player_stand_rect)
        self.tela.blit(self.game_name, self.game_name_rect)
        if self.pontuacao == 0:
            self.tela.blit(self.game_message, self.game_message_rect)
        else:
            score_message = self.fonte_pixel.render(f'Sua Pontuação:{self.pontuacao}', False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center=(400, 330))
            self.tela.blit(score_message, score_message_rect)

    def display_score(self):
        current_time = int(pygame.time.get_ticks() / 1000) - self.tempo_inicio
        score_surf = self.fonte_pixel.render(f'Pontuação:{current_time}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(670, 35))
        self.tela.blit(score_surf, score_rect)
        return current_time