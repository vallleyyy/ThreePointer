import pygame
from pygame.locals import *
import time
from rack import Rack
from shooter import Shooter

START_TIMER = 3000
MAX_SHOT_TIMER = 1000
DELAY_TIMER = 500
RED = (219, 59, 50)
TIMER_SIZE = 48
TIMER_POSITION = (271, 20)
SCORE_SIZE = 56
SCORE_POSITION = (50, 542)

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
        self.key_up = True
        self.delay_timer = DELAY_TIMER
        self.rack_index = 0
        self.frame = pygame.image.load("assets/frame.png").convert_alpha()
        self.frame_rect = self.frame.get_rect()
        self.frame_rect.center = (300, 300)
        self.timer_font = pygame.font.Font("assets/fonts/LCD.tff", TIMER_SIZE)
        self.score_font = pygame.font.Font("assets/fonts/LCD.tff", SCORE_SIZE)
        print("PRESS SPACE TO START")

    def generate_racks(self):
        racks = []
        racks.append(Rack("standard", 0))
        racks.append(Rack("standard", 1))
        racks.append(Rack("deep", 2))
        racks.append(Rack("standard", 3))
        racks.append(Rack("deep", 4))
        racks.append(Rack("standard", 5))
        racks.append(Rack("money", 6))
        return racks

    def update(self):
        time_passed = self.clock.get_time()
        pressed_keys = pygame.key.get_pressed()
        if not pressed_keys[K_SPACE]:
            self.key_up = True

        # start timer
        if not self.started and not self.active and not self.start_timer_running:
            if pressed_keys[K_SPACE]:
                self.key_up = False
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
            self.delay_timer -= time_passed

            # Shooting logic HERE
            if pressed_keys[K_SPACE] and not self.shooting and self.key_up and self.delay_timer <= 0:
                self.key_up = False
                self.shooting = True

            if self.shooting and pressed_keys[K_SPACE]:
                self.shot_timer += time_passed

            self.shooter.update(time_passed, self.shot_timer, self.shooting)

            if (self.shooting and not pressed_keys[K_SPACE]) or self.shot_timer > MAX_SHOT_TIMER:
                self.shooting = False

                current_rack = self.racks[self.rack_index]
                self.points += current_rack.shoot(self.shot_timer)

                if current_rack.done:
                    self.rack_index += 1

                if self.rack_index >= len(self.racks):
                    self.game_timer = 0

                self.shot_timer = 0
                self.delay_timer = DELAY_TIMER

            if self.game_timer <= 0:
                self.active = False
                print("Game Over:", self.points, 'points')

    def draw(self, surface):
        self.shooter.draw(surface)
        surface.blit(self.frame, self.frame_rect)
        if not self.rack_index >= len(self.racks):
            self.racks[self.rack_index].draw(surface)

        rounded_timer = f"{round(self.game_timer / 1000):02d}"
        timer = self.timer_font.render(rounded_timer, 1, RED)
        surface.blit(timer, TIMER_POSITION)

        formatted_score = f"{self.points:02d}"
        score = self.score_font.render(formatted_score, 1, RED)
        surface.blit(score, SCORE_POSITION)
        # shooter is drawn by shooter, includes ball in all stages except make/miss
        # rack is drawn by rack
        # game checks rack position for camera angle
        # game draws scoreboard and stuff
        pass


