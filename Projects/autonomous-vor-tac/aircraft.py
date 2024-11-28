import math as MATH
import pygame as PG
from config import (
    AIRCRAFT_SIZE,
    AIRCRAFT_HEADING_VECTOR_LENGTH,
    AIRCRAFT_EXTENDED_HEADING_VECTOR_LENGTH,
    AIRCRAFT_TURN_RATE
)

PG.init()
font = PG.font.Font(None, 18)

class Aircraft:
    def __init__(self, name: str, x: float, y: float, speed: int, heading: float) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.current_speed = speed
        self.max_speed = 0.0575
        self.min_speed = 0.02
        self.heading = heading
        self.target_heading = heading
        self.turn_rate = AIRCRAFT_TURN_RATE
        self.current_route_index = 0
        self.trail = []
        self.last_trail_position = (self.x, self.y)
        self.target_waypoint = None
        self.selected = False
    
    def draw(self, screen):
        PG.draw.rect(screen, (0, 255, 0), (self.x - 5, self.y - 5, AIRCRAFT_SIZE, AIRCRAFT_SIZE))
        self.draw_heading_vector(screen, (0, 255, 0))
        self.draw_trail(screen = screen)
        font = PG.font.Font(None, 18)
        text_1 = f'{self.name}'
        text_2 = f'{int(self.current_speed)}kts | {int(self.heading)}'
        text_surface_1 = font.render(text_1, True, (0, 255, 0))
        text_surface_2 = font.render(text_2, True, (0, 255, 0))
        text_rect_1 = text_surface_1.get_rect(center = (self.x, self.y - 35))
        text_rect_2 = text_surface_2.get_rect(center = (self.x, self.y - 20))
        screen.blit(text_surface_1, text_rect_1)
        screen.blit(text_surface_2, text_rect_2)
        if self.selected:
            PG.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), 25, 2)
    
    def draw_heading_vector(self, screen, color):
        start_x = self.x
        start_y = self.y

        heading_radian = MATH.radians(self.heading)
        
        EXTENDED_HEADING_VECTOR_LENGTH = AIRCRAFT_EXTENDED_HEADING_VECTOR_LENGTH if self.selected else 0
        
        end_x = start_x + MATH.sin(heading_radian) * (AIRCRAFT_HEADING_VECTOR_LENGTH + EXTENDED_HEADING_VECTOR_LENGTH)
        end_y = start_y - MATH.cos(heading_radian) * (AIRCRAFT_HEADING_VECTOR_LENGTH + EXTENDED_HEADING_VECTOR_LENGTH)
        
        PG.draw.line(screen, color, (start_x, start_y), (end_x, end_y), 3)
        
        if self.heading != self.target_heading:
            heading_radian = MATH.radians(self.target_heading)
            end_x = start_x + MATH.sin(heading_radian) * (AIRCRAFT_HEADING_VECTOR_LENGTH + EXTENDED_HEADING_VECTOR_LENGTH)
            end_y = start_y - MATH.cos(heading_radian) * (AIRCRAFT_HEADING_VECTOR_LENGTH + EXTENDED_HEADING_VECTOR_LENGTH)
            PG.draw.line(screen, (255, 255, 255), (start_x, start_y), (end_x, end_y), 1)
    
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
    
    def update_target_heading_to_waypoint(self):
        dx = self.target_waypoint.x - self.x
        dy = self.target_waypoint.y - self.y
        target_angle = MATH.degrees(MATH.atan2(-dy, dx))
        self.target_heading = (90 - target_angle) % 360
        
    def is_at_waypoint(self):
        distance = MATH.sqrt((self.x - self.target_waypoint.x) ** 2 + (self.y - self.target_waypoint.y) ** 2)
        return distance < 2.5
    
    def update_position(self):
        rad_heading = MATH.radians(90 - self.heading)
        dx = MATH.cos(rad_heading) * self.max_speed
        dy = -MATH.sin(rad_heading) * self.max_speed
        self.x += dx
        self.y += dy
        
        if self.target_waypoint and self.is_at_waypoint():
            print(f'{self.name} reached waypoint {self.target_waypoint.name}')
            self.target_waypoint = None
    
    def move(self):
        if self.target_waypoint:
            self.update_target_heading_to_waypoint()
        self.smooth_turn()
        self.update_position()
        
        angle_diff = abs((self.target_heading - self.heading) % 360)
        if angle_diff > 180:
            angle_diff = 360 - angle_diff
        speed = self.max_speed - ((self.max_speed - self.min_speed) * (angle_diff / 180))
        
        rad_heading = MATH.radians(90 - self.heading)
        dx = MATH.cos(rad_heading) * speed
        dy = -MATH.sin(rad_heading) * speed
        self.x += dx
        self.y += dy
        
        trail_spacing = 10
        tx = self.x - self.last_trail_position[0]
        ty = self.y - self.last_trail_position[1]
        t_distance = MATH.sqrt(tx ** 2 + ty ** 2)
        if t_distance > trail_spacing:
            self.trail.append((self.x, self.y))
            self.last_trail_position = (self.x, self.y)
        if len(self.trail) > 1000:
            self.trail.pop(0)
        
    def smooth_turn(self):
        delta = (self.target_heading - self.heading) % 360
        if delta > 180:
            delta -= 360
        turn_step = min(abs(delta), self.turn_rate) * (1 if delta > 0 else -1)
        self.heading = (self.heading + turn_step) % 360
