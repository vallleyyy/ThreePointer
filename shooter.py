import pygame
from pygame.locals import *

class Shooter(pygame.sprite.Sprite):
    def __init__(self, name, number, team):
        super().__init__()
        self.name = name
        self.number = number
        self.team = team
        self.image = pygame.image.load("assets/sample3.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300

    def update(self, time_passed, shot_timer, shooting):
        if shooting:
            if self.rect.y > 220:
                self.rect.move_ip(0, -5)
        else:
            if self.rect.y < 300:
                self.rect.move_ip(0, 10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
