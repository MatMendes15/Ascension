import pygame

pygame.init()
pygame.mixer.init()

class SoundManager(object):
    def __init__(self):
        self.enabled = True

    def toggle(self):
        if self.enabled == True:
            self.enabled = False #Desliga o som caso esteja habilitado
        elif self.enabled == False:
            self.enabled = True #Liga o som caso esteja desabilitado
    
    #Verifica se o som do jogo está (des)habilitado
    def statusCheck(self):
        if self.enabled == True:
            return True
        else:
            return False
        

    #Música de fundo    
    def backgroundMusic(self):
        if self.statusCheck() == True:
            sound = pygame.mixer.Sound("assets/audio/fundo.mp3")
            sound.play(loops=-1)
        else:
            pass


    #Som de pulo    
    def jumpSound(self):
        if self.statusCheck() == True:
            sound = pygame.mixer.Sound("assets/audio/jump.mp3")
            sound.play()
        else:
            pass
        
    
    #Som de seleção de item nos menus interativos        
    def selectSound(self):
        if self.statusCheck() == True:
            sound = pygame.mixer.Sound("assets/audio/select.mp3")
            sound.play()
        else:
            pass


    #Som de "impacto" entre o jogador e NPCs       
    def swordSound(self):
        if self.statusCheck() == True:
            sound = pygame.mixer.Sound("assets/audio/sword.mp3")
            sound.play()
        else:
            pass
    
    #Som de morte dos NPCs       
    def explosionSound(self):
        if self.statusCheck() == True:
            sound = pygame.mixer.Sound("assets/audio/explosion.wav")
            sound.play()
        else:
            pass

    #Som do portal       
    def portalSound(self):
        if self.statusCheck() == True:
            sound = pygame.mixer.Sound("assets/audio/portal.mp3")
            sound.play()
        else:
            pass


        
