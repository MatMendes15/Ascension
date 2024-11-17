import pygame
from cenas.jogo import Jogo

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
        while True:
            self.loading.load(screen)
            game = Jogo()
            game.run()
            
            if game.quit_game:
                self.popUp(screen)
                break

    def creditos(self, screen):
        pass

    def quit(self):
        pygame.quit()
        exit()

    def popUp(self, screen):
        self.show(screen)