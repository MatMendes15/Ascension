import pygame
from sys import exit
from cenas.menu import Menu
from utilidades.loading import Loading
from utilidades.soundManager import SoundManager


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Ascension")
    soundManager = SoundManager()
    loading = Loading()
    menu = Menu(screen, loading, soundManager)
    while True:
        menu.show()