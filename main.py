import pygame
from pygame.locals import *
from app import App

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 30
NAME = "Three Point Contest"

if __name__ == "__main__" :
    theApp = App(SCREEN_WIDTH, SCREEN_HEIGHT, NAME, FPS)
    theApp.on_execute()
