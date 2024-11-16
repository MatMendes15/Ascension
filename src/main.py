import pygame
from sys import exit
from cenas.menu import Menu
from utilidades.loading import Loading


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ascension")

    loading = Loading()
    menuBackground = pygame.transform.scale(pygame.image.load("assets/imagens/fundo/menuBackground.webp").convert(), (800, 600))
    menu = Menu(menuBackground, loading)
    
    menu.popUp(screen)