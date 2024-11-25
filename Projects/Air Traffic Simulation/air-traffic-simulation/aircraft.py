import math
import pygame

from config import (
    AIRCRAFT_SPEED,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    AIRCRAFT_COLOR,
    TURN_RATE,
)

class Aircraft:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading
        
    def move(self):
        # convert heading to radians for calculations
        rad = math.radians(self.heading)
        self.x += math.cos(rad) * AIRCRAFT_SPEED
        self.y += math.sin(rad) * AIRCRAFT_SPEED
        
        # keep within screen bounds (wrap around)
        self.x %= SCREEN_WIDTH
        self.y %= SCREEN_HEIGHT
    
    def draw(self, screen):
        # calculate triangle points based on heading
        size = 20 # size of aircraft triangle
        angle = math.radians(self.heading)
        p1 = (self.x + math.cos(angle) * size, self.y - math.sin(angle) * size)
        p2 = (self.x + math.cos(angle + 2.5) * size, self.y - math.sin(angle + 2.5) * size)
        p3 = (self.x + math.cos(angle - 2.5) * size, self.y - math.sin(angle - 2.5) * size)
        
        pygame.draw.polygon(screen, AIRCRAFT_COLOR, [p1, p2, p3])
    
    def turn(self, direction):
        if direction == 'left':
            self.heading = (self.heading + TURN_RATE) % 360
        elif direction == 'right':
            self.heading = (self.heading - TURN_RATE) % 360
            