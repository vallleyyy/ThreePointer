import pygame
from pygame.locals import *

class Shooter(pygame.sprite.Sprite):
    def __init__(self, name, number, team):
        super().__init__()
        self.name = name
        self.number = number
        self.team = team
        self.image = pygame.image.load("assets/sample3.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)
