import pygame
from pygame.locals import *
import time
from rack import Rack
from shooter import Shooter

START_TIMER = 3000
MAX_SHOT_TIMER = 1000
DELAY_TIMER = 500
PERFECT_TIMING = 500

RED = (219, 59, 50)

TIMER_SIZE = 48
TIMER_POSITION = (271, 20)

SCORE_SIZE = 56
SCORE_POSITION = (50, 542)

METER_PERFECT_SIZING = 160
METER_MAX_SIZING = 204

class Game:
    def __init__(self, length, clock, fps):
        self.length = length
        self.clock = clock
        self.fps = fps

        self.game_timer = length
        self.start_timer = START_TIMER
        self.delay_timer = DELAY_TIMER
        self.shot_timer = 0

        self.start_timer_running = False
        self.active = False
        self.shooting = False
        self.started = False
        self.key_up = True

        self.rack_index = 0
        self.racks = self.generate_racks()
        self.shooter = Shooter("Rickea", "2", "Sparks")

        self.points = 0

        self.frame = pygame.image.load("assets/frame.png").convert_alpha()
        self.frame_rect = self.frame.get_rect()
        self.frame_rect.center = (300, 300)

        self.meter_frame = pygame.image.load("assets/meter_frame.png").convert_alpha()
        self.meter_frame_rect = self.meter_frame.get_rect()

        self.meter_background = pygame.image.load("assets/meter_background.png").convert_alpha()
        self.meter_background_rect = self.meter_background.get_rect()

        self.timing_bar = pygame.image.load("assets/timing_bar.png").convert_alpha()
        self.timing_bar_rect = self.timing_bar.get_rect()

        self.timer_font = pygame.font.Font("assets/fonts/LCD.tff", TIMER_SIZE)
        self.score_font = pygame.font.Font("assets/fonts/LCD.tff", SCORE_SIZE)

        print("PRESS SPACE TO START")

    def generate_racks(self):
        racks = []
        racks.append(Rack("standard", 0, PERFECT_TIMING))
        racks.append(Rack("standard", 1, PERFECT_TIMING))
        racks.append(Rack("deep", 2, PERFECT_TIMING))
        racks.append(Rack("standard", 3, PERFECT_TIMING))
        racks.append(Rack("deep", 4, PERFECT_TIMING))
        racks.append(Rack("standard", 5, PERFECT_TIMING))
        racks.append(Rack("money", 6, PERFECT_TIMING))
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
            self.update_timing_bar(time_passed)

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

    def update_timing_bar(self, time_passed):
        seconds_per_frame = 1000 / self.fps
        pixels_per_ms = (METER_PERFECT_SIZING / PERFECT_TIMING) * -1
        down_per_ms = (METER_MAX_SIZING / DELAY_TIMER)

        if self.shooting:
            if self.timing_bar_rect.y > -1 * METER_MAX_SIZING:
                self.timing_bar_rect.move_ip(0, pixels_per_ms * time_passed)
                if self.timing_bar_rect.y < -1 * METER_MAX_SIZING:
                    self.timing_bar_rect.y = -1 * METER_MAX_SIZING

        else:
            if self.timing_bar_rect.y < 0:
                self.timing_bar_rect.y = 0
                self.timing_bar_rect.move_ip(0, down_per_ms * time_passed)
                if self.timing_bar_rect.y > 0 * METER_MAX_SIZING:
                    self.timing_bar_rect.y = 0





    def draw(self, surface):
        self.shooter.draw(surface)

        surface.blit(self.frame, self.frame_rect)
        surface.blit(self.meter_frame, self.meter_frame_rect)
        surface.blit(self.meter_background, self.meter_background_rect)
        surface.blit(self.timing_bar, self.timing_bar_rect)

        if not self.rack_index >= len(self.racks):
            self.racks[self.rack_index].draw(surface)

        if not self.started:
            rounded_timer = f"{round(self.start_timer / 1000):02d}"
        else:
            rounded_timer = f"{round(self.game_timer / 1000):02d}"

        timer = self.timer_font.render(rounded_timer, 1, RED)
        surface.blit(timer, TIMER_POSITION)

        formatted_score = f"{self.points:02d}"
        score = self.score_font.render(formatted_score, 1, RED)
        surface.blit(score, SCORE_POSITION)


