import pygame

class Loading(object):
    def __init__(self):
        self.background = (0, 0, 0)
        pygame.font.init()
        self.font = pygame.font.Font("assets/fontes/PressStart2PFont.ttf", 30)
        self.fontColor = (230, 230, 230)
    
    def load(self, screen):
        screen.fill(self.background)
        text = self.font.render("LOADING...", True, self.fontColor)
        text_pos = (screen.get_width() // 2 - text.get_width() // 2, 300)
        screen.blit(text, text_pos)

        pygame.display.flip()
        pygame.time.delay(4000)
