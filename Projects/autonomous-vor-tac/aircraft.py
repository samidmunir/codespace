import pygame as PG
import math as MATH
from config import (
    AIRCRAFT_SIZE,
    AIRCRAFT_HEADING_VECTOR_LENGTH
)

PG.init()
font = PG.font.Font(None, 18)

class Aircraft:
    def __init__(self, name: str, x: float, y: float, heading: float) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.heading = heading
        self.first_waypoint = None
        self.route = []
        self.current_route_index = 0
        self.trail = []
        self.last_trail_position = (self.x, self.y)
        self.selected = False
    
    def draw(self, screen):
        PG.draw.rect(screen, (0, 255, 0), (self.x - 5, self.y - 5, AIRCRAFT_SIZE, AIRCRAFT_SIZE))
        self.draw_heading_vector(screen, (0, 255, 0))
        self.draw_trail(screen = screen)
        font = PG.font.Font(None, 18)
        text = f'{self.name} | {self.heading}'
        text_surface = font.render(text, True, (0, 255, 0))
        text_rect = text_surface.get_rect(center = (self.x, self.y - 30))
        screen.blit(text_surface, text_rect)
        if self.selected:
            PG.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), 25, 2)
    
    def draw_heading_vector(self, screen, color):
        start_x = self.x
        start_y = self.y

        heading_radian = MATH.radians(self.heading)
        
        EXTENDED_HEADING_VECTOR_LENGTH = 25 if self.selected else 0
        
        end_x = start_x + MATH.sin(heading_radian) * (AIRCRAFT_HEADING_VECTOR_LENGTH + EXTENDED_HEADING_VECTOR_LENGTH)
        end_y = start_y - MATH.cos(heading_radian) * (AIRCRAFT_HEADING_VECTOR_LENGTH + EXTENDED_HEADING_VECTOR_LENGTH)
        
        PG.draw.line(screen, color, (start_x, start_y), (end_x, end_y), 3)
    
    def draw_trail(self, screen):
        for i, (tx, ty) in enumerate(self.trail):
            factor = i / len(self.trail) if len(self.trail) > 0 else 0
            red = int((1 - factor) * 255)
            blue = int(factor * 255)
            color = (red, 0, blue)
            PG.draw.circle(screen, color, (int(tx), int(ty)), 5)
        
    def is_clicked(self, mouse_pos):
        distance = MATH.sqrt((mouse_pos[0] - self.x) ** 2 + (mouse_pos[1] - self.y) ** 2)
        return distance <= 20
    
    def move(self):
        rad_heading = MATH.radians(90 - self.heading)
        dx = MATH.cos(rad_heading) * 0.0575
        dy = -MATH.sin(rad_heading) * 0.0575
        self.x += dx
        self.y += dy
        
        trail_spacing = 15
        tx = self.x - self.last_trail_position[0]
        ty = self.y - self.last_trail_position[1]
        t_distance = MATH.sqrt(tx ** 2 + ty ** 2)
        if t_distance > trail_spacing:
            self.trail.append((self.x, self.y))
            self.last_trail_position = (self.x, self.y)
        if len(self.trail) > 1000:
            self.trail.pop(0)