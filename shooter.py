import pygame
from pygame.locals import *

class Shooter(pygame.sprite.Sprite):
    def __init__(self, name, number, team):
        super().__init__()
        self.name = name
        self.number = number
        self.team = team
        self.image = pygame.image.load("assets/shooter.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = 50

    def update(self, time_passed, shot_timer, shooting):
        if shooting:
            if self.rect.y > -30:
                self.rect.move_ip(0, -5)
        else:
            if self.rect.y < 50:
                self.rect.move_ip(0, 10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
