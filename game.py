import pygame
from pygame.locals import *
from pynput import keyboard
import time
from rack import Rack
from shooter import Shooter

START_TIMER = 3000
MAX_SHOT_TIMER = 2000

class Game:
    def __init__(self, length, clock):
        self.length = length
        self.game_timer = length
        self.start_timer = START_TIMER
        self.start_timer_running = False
        self.clock = clock
        self.racks = self.generate_racks()
        self.shooter = Shooter("Rickea", "2", "Sparks")
        self.started = False
        self.active = False
        self.points = 0
        self.shooting = False
        self.shot_timer = 0
        print("PRESS SPACE TO START")

    def generate_racks(self):
        racks = []
        racks.append(Rack(22, "standard", 0))
        racks.append(Rack(22, "standard", 1))
        racks.append(Rack(22, "deep", 2))
        racks.append(Rack(22, "standard", 3))
        racks.append(Rack(22, "deep", 4))
        racks.append(Rack(22, "standard", 5))
        racks.append(Rack(22, "money", 6))
        return racks

    def update(self):
        time_passed = self.clock.get_time()
        pressed_keys = pygame.key.get_pressed()

        # start timer
        if not self.started and not self.active and not self.start_timer_running:
            if pressed_keys[K_SPACE]:
                self.start_timer_running = True
                print("STARTING IN 3")

        if self.start_timer_running:
            self.start_timer -= time_passed

            if self.start_timer <= 0:
                print("STARTING")
                self.started = True
                self.active = True
                self.start_timer_running = False
                self.start_timer = START_TIMER

        if self.started and self.active:
            self.game_timer -= time_passed

            # Shooting logic HERE
            if pressed_keys[K_SPACE] and not self.shooting:
                self.shooting = True


            if self.shooting and pressed_keys[K_SPACE]:
                self.shot_timer += time_passed

            if (self.shooting and not pressed_keys[K_SPACE]) or self.shot_timer > MAX_SHOT_TIMER:
                print(self.shot_timer)
                self.shooting = False
                self.shot_timer = 0

            if self.game_timer <= 0:
                self.active = False
                print("Game Over")


        # get how long space bar has been pressed down
        # pass it into rack object
        # if make, add points to game points
        # iterate to next ball/rack
        # update timer
        pass

    def draw(self):
        # shooter is drawn by shooter, includes ball in all stages except make/miss
        # rack is drawn by rack
        # game checks rack position for camera angle
        # game draws scoreboard and stuff
        pass


