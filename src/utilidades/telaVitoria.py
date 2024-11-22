import pygame
from utilidades.loading import Loading

class TelaVitoria:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('assets/fontes/PressStart2PFont.ttf', 30)
        self.image = pygame.image.load('assets/imagens/jogo_fim/imagem_vitoria.png').convert()
        self.image = pygame.transform.scale(self.image, (800, 400))
        self.display_time = 10000  # 10 segundos em milissegundos
        self.start_time = None
        self.clock = pygame.time.Clock()

    def show(self):
        self.start_time = pygame.time.get_ticks()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Exibe a imagem de fundo
            self.screen.blit(self.image, (0, 0))

            # Renderiza o texto
            text = self.font.render('Parabéns, você venceu!', True, (255, 255, 0))
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(text, text_rect)

            pygame.display.flip()
            self.clock.tick(60)

            # Verifica se o tempo expirou
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= self.display_time:
                running = False

        # Importa Menu aqui para evitar importação circular
        from cenas.menu import Menu
        loading = Loading()
        menu = Menu(self.screen, loading)
        menu.show()