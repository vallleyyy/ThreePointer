import pygame
from pygame.locals import *
from game import Game

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GAME_LENGTH = 70 * 1000

class App:
    def __init__(self, width, height, name, fps):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = width, height
        self.name = name
        self.fps = fps
        self.clock = None
        self.game = None


    def on_init(self):
        pygame.init()

        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(self.name)

        self.clock = pygame.time.Clock()
        self.game = Game(GAME_LENGTH, self.clock, self.fps)

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.game.update()

    def on_render(self):
        self._display_surf.fill(WHITE)
        self.game.draw(self._display_surf)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.clock.tick(self.fps)
        self.on_cleanup()
