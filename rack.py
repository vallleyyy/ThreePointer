import pygame
from pygame.locals import *

class Rack:
    def __init__(self, distance, rack_type, position): # standard distance 22, deep distance 30, positions 0-6, deep should be 2 and 4
        self.distance = distance
        self.rack_type = rack_type
        self.balls = self.create_balls_array()
        self.index = 0
        self.done = False

    def create_balls_array(self):
        if self.rack_type == "standard":
            return [
                (1, False),
                (1, False),
                (1, False),
                (1, False),
                (2, False),
                ]
        if self.rack_type == "money":
              return [
                (2, False),
                (2, False),
                (2, False),
                (2, False),
                (2, False),
                ]
        if self.rack_type == "deep":
            return [
                (3, False)
                ]

    def shoot(self, make):
        pass
