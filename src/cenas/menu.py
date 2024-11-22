import pygame
from cenas.jogo import Jogo
from utilidades.loading import Loading
from utilidades.soundManager import SoundManager

class Menu:
    def __init__(self, screen, loading, soundManager):
        self.soundManager = soundManager
        self.screen = screen
        self.loading = loading
        self.frames = []
        for i in range(1, 108):  # Ajuste o intervalo conforme o número de frames
            frame = pygame.image.load(f'assets/imagens/fundo/menu/fundoMenu{i}.png').convert()
            frame = pygame.transform.scale(frame, (800, 400))
            self.frames.append(frame)
        self.current_frame = 0
        self.animation_speed = 0.1  # Ajuste a velocidade conforme necessário
        self.clock = pygame.time.Clock()

        # Opções do menu
        self.options = ['Iniciar Jogo', 'Créditos', 'Configurações', 'Sair do Jogo']
        self.selected_option = 0
        self.font = pygame.font.Font('assets/fontes/PressStart2PFont.ttf', 30)

    def show(self):
        running = True
        while running:
            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        self.select_option()

            # Atualiza o frame da animação
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.frames):
                self.current_frame = 0

            # Mostra o frame atual
            frame = self.frames[int(self.current_frame)]
            self.screen.blit(frame, (0, 0))

            title_text = self.font.render('ASCENSION', True, (213, 108, 245))
            title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, 50))
            self.screen.blit(title_text, title_rect)

            # Mostra as opções do menu
            for index, option in enumerate(self.options):
                if index == self.selected_option:
                    color = (255, 255, 0)  # Amarelo para a opção selecionada
                else:
                    color = (255, 255, 255)
                text = self.font.render(option, True, color)
                text_rect = text.get_rect(center=(self.screen.get_width() // 2, 150 + index * 60))
                self.screen.blit(text, text_rect)

            pygame.display.flip()
            self.clock.tick(60)

    def start_game(self):
        # Exibe a tela de carregamento
        self.loading.load(self.screen)
        game = Jogo(self.soundManager)
        # Inicia o loop principal do jogo
        game.run()

    def creditos(self, screen):
        pass

    def quit(self):
        pygame.quit()
        exit()

    def popUp(self, screen):
        self.show(screen)

    def select_option(self):
        option = self.options[self.selected_option]
        self.soundManager.selectSound()
        if option == 'Iniciar Jogo':
            self.start_game()
        elif option == 'Créditos':
            self.show_credits()
        elif option == 'Configurações':
            self.show_settings()
        elif option == 'Sair do Jogo':
            pygame.quit()
            exit()

    def show_credits(self):
        running = True
        clock = pygame.time.Clock()
        screen = self.screen

        #Exibição do texto
        credits_font = pygame.font.Font('assets/fontes/PressStart2PFont.ttf', 10)
        credits = [
            "<<DESENVOLVEDORE>>",
            "",
            "MATEUS MENDES CABRAL",
            "THIAGO FELIPE GARCIA",
            "",
            "",
            "<<PROFESSORES>>",
            "",
            "LEANDRO PUPO NATALE",
            "LUIZ CARLOS MACHI LOZANO",
            "",
            "",
            "",
            "JOGOS DIGITAIS [04J]",
            "UNIVERSIDADE PRESBITERIANA MACKENZIE",
        ]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            #Fundo
            frame = self.frames[int(self.current_frame)]
            screen.blit(frame, (0, 0))
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            y_offset = 40
            for line in credits:
                text = credits_font.render(line, True, (255, 255, 0))
                text_rect = text.get_rect(center=(screen.get_width() // 2, y_offset))
                screen.blit(text, text_rect)
                y_offset += 20 

            pygame.display.flip()
            clock.tick(60)


    def show_settings(self):
        running = True
        clock = pygame.time.Clock()
        screen = self.screen

        settings_font = pygame.font.Font('assets/fontes/PressStart2PFont.ttf', 10)
        settings = [
            "<<CONFIGURAÇÕES>>",
            "",
            "MÚSICA E EFEITOS SONOROS:",
            "SIM" if self.soundManager.statusCheck() else "NÃO" #Estado do som
        ]
        
        selected_option = 3  #Começa na opção "SIM" ou "NÃO"

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_UP:
                        selected_option = 3 if selected_option == 4 else selected_option - 1
                    elif event.key == pygame.K_DOWN:
                        selected_option = 3 if selected_option == 2 else selected_option + 1
                    elif event.key == pygame.K_RETURN:
                        if selected_option == 3:  #MÚSICA E EFEITOS SONOROS
                            self.soundManager.toggle()  #Alterna o estado do som
                            settings[3] = "SIM" if self.soundManager.statusCheck() else "NÃO"  # Atualiza a opção "SIM/NÃO"

            #Fundo
            frame = self.frames[int(self.current_frame)]
            screen.blit(frame, (0, 0))
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            
            y_offset = 40
            for index, line in enumerate(settings):
                color = (255, 255, 0) if index == selected_option else (255, 255, 255)
                text = settings_font.render(line, True, color)
                text_rect = text.get_rect(center=(screen.get_width() // 2, y_offset))
                screen.blit(text, text_rect)
                y_offset += 20

            pygame.display.flip()
            clock.tick(60)