
import math as MATH
import pygame as PG
from config import (
    AIRCRAFT_COLOR,
    AIRCRAFT_WIDTH,
    AIRCRAFT_HEIGHT,
    AIRCRAFT_SPEED_SCALAR,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)

class Aircraft:
    def __init__(self, flight_number: str, type: str, x: float, y: float, speed: float, altitude: float, heading: float):
        self.flight_number = flight_number
        self.type = type
        self.x = x
        self.y = y
        self.speed = speed
        self.altitude = altitude
        self.heading = heading
    
    def draw(self, screen):
        left = self.x - (AIRCRAFT_WIDTH / 2)
        top = self.y - (AIRCRAFT_HEIGHT / 2)
        aircraft_rectangle = (left, top, AIRCRAFT_WIDTH, AIRCRAFT_HEIGHT)
        PG.draw.rect(surface = screen, color = AIRCRAFT_COLOR, rect = aircraft_rectangle)
    
    def move(self):
        if self.heading == 0 or self.heading == 360:
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 15:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 30:
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.x += self.speed * (AIRCRAFT_SPEED_SCALAR)
        elif self.heading == 45:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 60:
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 75:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 90:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 105:
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 135:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 150:
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 165:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 180:
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 195:
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 210:
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 225:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 240:
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 265:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 270:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 285:
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 300:
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 315:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 330:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 345:
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
        else:
            pass