import pygame
from sys import exit
from random import randint, choice
from Loading import Loading

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        jogador_andando_1 = pygame.image.load('assets/imagens/Player/jogador_correndo_1.PNG').convert_alpha()
        jogador_andando_2 = pygame.image.load('assets/imagens/Player/jogador_correndo_2.PNG').convert_alpha()
        self.jogador_andando = [jogador_andando_1, jogador_andando_2]
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
            self.indice_jogador += 0.1
            if self.indice_jogador >= len(self.jogador_andando):
                self.indice_jogador = 0
            self.image = self.jogador_andando[int(self.indice_jogador)]

    def update(self):
        self.entrada_jogador()
        self.aplicar_gravidade()
        self.estado_animacao()

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        if tipo == 'morcego':
            morcego_1 = pygame.image.load('assets/imagens/inimigo_voador/morcego_1.png').convert_alpha()
            morcego_2 = pygame.image.load('assets/imagens/inimigo_voador/morcego_2.png').convert_alpha()
            self.frames = [morcego_1, morcego_2]
            pos_y = 300
        else:
            cogumelo_1 = pygame.image.load('assets/imagens/inimigo_terrestre/cogumelo_1.png').convert_alpha()
            cogumelo_2 = pygame.image.load('assets/imagens/inimigo_terrestre/cogumelo_2.png').convert_alpha()
            self.frames = [cogumelo_1, cogumelo_2]
            pos_y = 340

        self.indice_animacao = 0
        self.image = self.frames[self.indice_animacao]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), pos_y))

    def animation_state(self):
        self.indice_animacao += 0.1
        if self.indice_animacao >= len(self.frames):
            self.indice_animacao = 0
        self.image = self.frames[int(self.indice_animacao)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

class Menu:
    def __init__(self, background, loading):
        self.background = background
        self.loading = loading

    def show(self, screen):
        pygame.display.set_caption('Menu')

        # Carrega as fontes e textos
        title_font = pygame.font.Font(None, 74)
        button_font = pygame.font.Font(None, 50)
        title = title_font.render('Ascension', True, (255, 255, 255))
        start = button_font.render('Iniciar', True, (255, 255, 255))
        creditos = button_font.render('Créditos', True, (255, 255, 255))
        quit_text = button_font.render('Sair', True, (255, 255, 255))

        running = True
        while running:
            screen.fill((0, 0, 0))
            screen.blit(self.background, (0, 0))
            start_pos = (screen.get_width() // 2 - start.get_width() // 2, 250)
            creditos_pos = (screen.get_width() // 2 - creditos.get_width() // 2, 350)
            quit_pos = (screen.get_width() // 2 - quit_text.get_width() // 2, 450)

            screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 100))
            screen.blit(start, start_pos)
            screen.blit(creditos, creditos_pos)
            screen.blit(quit_text, quit_pos)

            startRect = pygame.Rect(start_pos[0], start_pos[1], start.get_width(), start.get_height())
            creditosRect = pygame.Rect(creditos_pos[0], creditos_pos[1], creditos.get_width(), creditos.get_height())
            quitRect = pygame.Rect(quit_pos[0], quit_pos[1], quit_text.get_width(), quit_text.get_height())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if startRect.collidepoint(mouse_pos):
                        self.start(screen)
                    elif creditosRect.collidepoint(mouse_pos):
                        self.creditos(screen)
                    elif quitRect.collidepoint(mouse_pos):
                        self.quit()

            pygame.display.flip()

    def start(self, screen):
        self.loading.load(screen)
        game = Jogo()
        game.run()

    def creditos(self, screen):
        pass

    def quit(self):
        pygame.quit()
        exit()

    def popUp(self, screen):
        self.show(screen)

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Corredor')
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

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ascension")

    loading = Loading()
    menuBackground = pygame.transform.scale(pygame.image.load("assets/imagens/fundo/menuBackground.webp").convert(), (800, 600))
    menu = Menu(menuBackground, loading)
    
    menu.popUp(screen)