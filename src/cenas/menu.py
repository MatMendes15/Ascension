import pygame
from cenas.jogo import Jogo
from utilidades.loading import Loading

class Menu:
    def __init__(self, screen, loading):
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
        
        # instância do jogo
        game = Jogo()
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
        pass

    def show_settings(self):
        pass