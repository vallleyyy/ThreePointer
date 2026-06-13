import pygame
from scipy.stats import norm
from pygame.locals import *

class Rack:
    def __init__(self, distance, rack_type, position): # standard distance 22, deep distance 30, positions 0-6, deep should be 2 and 4
        self.distance = distance
        self.rack_type = rack_type
        self.position = position
        self.balls = self.create_balls_array()
        self.index = 0
        self.done = False

    def create_balls_array(self):
        if self.rack_type == "standard":
            return [
                1, 1, 1,
                1, 2
                ]
        if self.rack_type == "money":
              return [
                  2, 2, 2,
                  2, 2
                ]
        if self.rack_type == "deep":
            return [3]

    def shoot(self, timing):
        print(timing)
        points = 0

        if self.is_make(timing):
            points = self.balls[self.index]

        self.index += 1

        if self.index >= len(self.balls):
            self.done = True
        print(points)
        return points
    
    def is_make(self, timing):
        return timing > 400 and timing < 600

