
import math as MATH
import pygame as PG
from config import (
    AIRCRAFT_COLOR,
    AIRCRAFT_WIDTH,
    AIRCRAFT_HEIGHT,
    AIRCRAFT_SPEED_SCALAR,
    AIRCRAFT_HEADING_VECTOR_LENGTH,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)

PG.init()
font = PG.font.Font(None, 18)

class Aircraft:
    def __init__(self, flight_number: str, type: str, x: float, y: float, speed: float, altitude: float, heading: float):
        self.flight_number = flight_number
        self.type = type
        self.x = x
        self.y = y
        self.speed = speed
        self.altitude = altitude
        self.heading = heading
        self.trail = []
        self.last_trail_position = (self.x, self.y)
        self.selected = False
    
    def draw(self, screen, label_color):
        heading_vector_color = label_color
        aircraft_label_1 = f'{self.flight_number} - {self.type}'
        aircraft_label_2 = f'{self.speed}kts {self.altitude}ft'
        aircraft_label_3 = f'{int(self.heading)}°'
        self.draw_text(screen, aircraft_label_1, font, label_color, offset=(AIRCRAFT_WIDTH / 2, -60))
        self.draw_text(screen, aircraft_label_2, font, label_color, offset=(AIRCRAFT_WIDTH / 2, -40))
        self.draw_text(screen, aircraft_label_3, font, label_color, offset=(AIRCRAFT_WIDTH / 2, -20))
        left = self.x - (AIRCRAFT_WIDTH / 2)
        top = self.y - (AIRCRAFT_HEIGHT / 2)
        aircraft_rectangle = (left, top, AIRCRAFT_WIDTH, AIRCRAFT_HEIGHT)
        PG.draw.rect(surface = screen, color = AIRCRAFT_COLOR, rect = aircraft_rectangle)
        self.draw_heading_vector(screen, heading_vector_color)
        if self.selected:
            PG.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), 25, 2)
        self.draw_trail(screen)
    
    def move(self):
        if self.heading == 0 or self.heading == 360:
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 15:
            self.x += self.speed * (AIRCRAFT_SPEED_SCALAR / 3)
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 30:
            self.x += self.speed * (AIRCRAFT_SPEED_SCALAR / 2)
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 45:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 60:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * (AIRCRAFT_SPEED_SCALAR / 2)
        elif self.heading == 75:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * (AIRCRAFT_SPEED_SCALAR / 3)
        elif self.heading == 90:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 105:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
            self.y += self.speed * (AIRCRAFT_SPEED_SCALAR / 3)
        elif self.heading == 120:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
            self.y += self.speed * (AIRCRAFT_SPEED_SCALAR / 2)
        elif self.heading == 135:
            self.x += self.speed * AIRCRAFT_SPEED_SCALAR
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 150:
            self.x += self.speed * (AIRCRAFT_SPEED_SCALAR / 2)
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 165:
            self.x += self.speed * (AIRCRAFT_SPEED_SCALAR / 3)
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 180:
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 195:
            self.x -= self.speed * (AIRCRAFT_SPEED_SCALAR / 3)
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 210:
            self.x -= self.speed * (AIRCRAFT_SPEED_SCALAR / 2)
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 225:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y += self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 240:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y += self.speed * (AIRCRAFT_SPEED_SCALAR / 2)
        elif self.heading == 255:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y += self.speed * (AIRCRAFT_SPEED_SCALAR / 3)
        elif self.heading == 270:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 285:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * (AIRCRAFT_SPEED_SCALAR / 3)
        elif self.heading == 300:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * (AIRCRAFT_SPEED_SCALAR / 2)
        elif self.heading == 315:
            self.x -= self.speed * AIRCRAFT_SPEED_SCALAR
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 330:
            self.x -= self.speed * (AIRCRAFT_SPEED_SCALAR / 2)
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        elif self.heading == 345:
            self.x -= self.speed * (AIRCRAFT_SPEED_SCALAR / 3)
            self.y -= self.speed * AIRCRAFT_SPEED_SCALAR
        else:
            pass
        
        trail_spacing = 15
        dx = self.x - self.last_trail_position[0]
        dy = self.y - self.last_trail_position[1]
        distance = MATH.sqrt(dx ** 2 + dy ** 2)
        
        if distance > trail_spacing:
            self.trail.append((self.x, self.y))
            self.last_trail_position = (self.x, self.y)
        if (len(self.trail) > 1000):
            self.trail.pop(0)
    
    def draw_text(self, screen, text, font, color, offset = (0, -30)):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center = (self.x + offset[0], self.y + offset[1]))
        screen.blit(text_surface, text_rect)
    
    def draw_trail(self, screen):
        for i, (tx, ty) in enumerate(self.trail):
            factor = i / len(self.trail) if len(self.trail) > 0 else 0
            
            red = int((1 - factor) * 255)
            blue = int(factor * 255)
            color = (red, 0, blue)
            PG.draw.circle(screen, color, (int(tx), int(ty)), 5)

    def is_clicked(self, mouse_pos):
        distance = MATH.sqrt((mouse_pos[0] - self.x) ** 2 + (mouse_pos[1] - self.y ) ** 2)
        return distance < 20
    
    def draw_heading_vector(self, screen, color):
        start_x = self.x
        start_y = self.y
        
        # Convert heading from degrees to radians
        heading_radian = MATH.radians(self.heading)
        
        end_x = start_x + MATH.sin(heading_radian) * AIRCRAFT_HEADING_VECTOR_LENGTH
        end_y = start_y - MATH.cos(heading_radian) * AIRCRAFT_HEADING_VECTOR_LENGTH
        
        PG.draw.line(screen, color, (start_x, start_y), (end_x, end_y), 2)