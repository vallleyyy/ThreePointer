import pygame
import math
import random
from scipy.stats import norm
from pygame.locals import *

PERFECT_TIMING = 500
STANDARD_DENOM = 1.5
DEEP_DENOM = 0.5

class Rack:
    def __init__(self, rack_type, position):
        self.rack_type = rack_type
        self.position = position
        self.balls = self.create_balls_array()
        self.index = 0
        self.done = False
        self.perfect_timing = PERFECT_TIMING

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
        points = 0

        if self.is_make(timing):
            points = self.balls[self.index]

        print(timing, points, "/", self.balls[self.index])

        self.index += 1

        if self.index >= len(self.balls):
            self.done = True

        return points
    
    def is_make(self, timing):
        make_percentage = self.timing_odds(timing)
        luck = random.random()
        return luck <= make_percentage
    
    
    def timing_odds(self, timing):
        if self.rack_type == "deep":
            denominator = STANDARD_DENOM
        else:
            denominator = DEEP_DENOM

        scaled_perfect = self.perfect_timing / 100
        scaled_timing = timing / 100
        numerator = (scaled_timing - scaled_perfect)**2
        fraction = numerator / denominator
        exponent = -1 * fraction
        return math.e**exponent
