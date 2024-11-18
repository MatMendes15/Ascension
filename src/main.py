import pygame
from sys import exit
from cenas.menu import Menu
from utilidades.loading import Loading


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Ascension")

    loading = Loading()
    menu = Menu(screen, loading)
    menu.show()