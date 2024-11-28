import math as MATH
import pygame as PG
from config import (
    FPS,
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
        self.smooth_turn()
        
        angle_diff = abs((self.target_heading - self.heading) % 360)
        if angle_diff > 180:
            angle_diff = 360 - angle_diff
        speed = self.max_speed - ((self.max_speed - self.min_speed) * (angle_diff / 180))
        
        rad_heading = MATH.radians(90 - self.heading)
        dx = MATH.cos(rad_heading) * speed
        dy = -MATH.sin(rad_heading) * speed
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
        
    def smooth_turn(self):
        delta = (self.target_heading - self.heading) % 360
        if delta > 180:
            delta -= 360
        turn_step = min(abs(delta), self.turn_rate) * (1 if delta > 0 else -1)
        self.heading = (self.heading + turn_step) % 360

# class Aircraft:
#     def __init__(self, name: str, x: float, y: float, speed: int, heading: float) -> None:
#         self.name = name
#         self.x = x
#         self.y = y
#         self.current_speed = speed  # Speed in knots
#         self.max_speed = speed  # Maximum speed in knots
#         self.min_speed = max(speed * 0.5, 150)  # Minimum speed in knots
#         self.heading = heading
#         self.target_heading = heading
#         self.turn_rate = AIRCRAFT_TURN_RATE
#         self.pixels_per_nautical_mile = 10  # Scale for 1 nautical mile = 10 pixels
#         self.selected = False
#         self.trail = []
#         self.last_trail_position = (self.x, self.y)

#     def draw(self, screen):
#         PG.draw.rect(screen, (0, 255, 0), (self.x - 5, self.y - 5, AIRCRAFT_SIZE, AIRCRAFT_SIZE))
#         self.draw_heading_vector(screen, (0, 255, 0))
#         self.draw_trail(screen)

#         # Display the aircraft's speed and heading
#         font = PG.font.Font(None, 18)
#         text = f'{self.name} | {int(self.current_speed)} kts | {int(self.heading)}°'
#         text_surface = font.render(text, True, (0, 255, 0))
#         text_rect = text_surface.get_rect(center=(self.x, self.y - 30))
#         screen.blit(text_surface, text_rect)

#         if self.selected:
#             PG.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), 25, 2)
        
#     def draw_heading_vector(self, screen, color):
#         start_x = self.x
#         start_y = self.y

#         heading_radian = MATH.radians(self.heading)
        
#         EXTENDED_HEADING_VECTOR_LENGTH = AIRCRAFT_EXTENDED_HEADING_VECTOR_LENGTH if self.selected else 0
        
#         end_x = start_x + MATH.sin(heading_radian) * (AIRCRAFT_HEADING_VECTOR_LENGTH + EXTENDED_HEADING_VECTOR_LENGTH)
#         end_y = start_y - MATH.cos(heading_radian) * (AIRCRAFT_HEADING_VECTOR_LENGTH + EXTENDED_HEADING_VECTOR_LENGTH)
        
#         PG.draw.line(screen, color, (start_x, start_y), (end_x, end_y), 3)
    
#     def draw_trail(self, screen):
#         for i, (tx, ty) in enumerate(self.trail):
#             factor = i / len(self.trail) if len(self.trail) > 0 else 0
#             red = int((1 - factor) * 255)
#             blue = int(factor * 255)
#             color = (red, 0, blue)
#             PG.draw.circle(screen, color, (int(tx), int(ty)), 5)

#     # def move(self):
#     #     self.smooth_turn()

#     #     # Calculate angle difference for speed adjustment
#     #     angle_diff = abs((self.target_heading - self.heading) % 360)
#     #     if angle_diff > 180:
#     #         angle_diff = 360 - angle_diff

#     #     # Convert knots to pixels/frame
#     #     base_pixel_speed = (self.max_speed * self.pixels_per_nautical_mile) / FPS
#     #     min_pixel_speed = (self.min_speed * self.pixels_per_nautical_mile) / FPS
#     #     pixel_speed = base_pixel_speed - ((base_pixel_speed - min_pixel_speed) * (angle_diff / 180))

#     #     # Update current speed (for display in knots)
#     #     self.current_speed = (pixel_speed * FPS) / self.pixels_per_nautical_mile

#     #     # Apply movement
#     #     rad_heading = MATH.radians(90 - self.heading)
#     #     dx = MATH.cos(rad_heading) * pixel_speed
#     #     dy = -MATH.sin(rad_heading) * pixel_speed
#     #     self.x += dx
#     #     self.y += dy

#     #     # Update trail
#     #     trail_spacing = 15
#     #     tx = self.x - self.last_trail_position[0]
#     #     ty = self.y - self.last_trail_position[1]
#     #     t_distance = MATH.sqrt(tx ** 2 + ty ** 2)
#     #     if t_distance > trail_spacing:
#     #         self.trail.append((self.x, self.y))
#     #         self.last_trail_position = (self.x, self.y)
#     #     if len(self.trail) > 1000:
#     #         self.trail.pop(0)
    
#     def move(self):
#         self.smooth_turn()

#         # Calculate angle difference for speed adjustment
#         angle_diff = abs((self.target_heading - self.heading) % 360)
#         if angle_diff > 180:
#             angle_diff = 360 - angle_diff

#         # Convert knots to pixels/frame
#         # Ensure pixels_per_nautical_mile is a reasonable value (e.g., 10 pixels = 1 nautical mile)
#         pixels_per_nautical_mile = 10  # Adjust based on your screen scaling
#         base_pixel_speed = (self.max_speed * pixels_per_nautical_mile) / FPS
#         min_pixel_speed = (self.min_speed * pixels_per_nautical_mile) / FPS

#         # Dynamically adjust speed based on turn intensity
#         pixel_speed = base_pixel_speed - ((base_pixel_speed - min_pixel_speed) * (angle_diff / 180))

#         # Debug: Print calculated pixel speeds
#         print(f'{self.name}: Base={base_pixel_speed:.3f}, Min={min_pixel_speed:.3f}, Current={pixel_speed:.3f} pixels/frame')

#         # Update current speed (in knots) for display
#         self.current_speed = (pixel_speed * FPS) / pixels_per_nautical_mile

#         # Apply movement vector
#         rad_heading = MATH.radians(90 - self.heading)
#         dx = MATH.cos(rad_heading) * pixel_speed
#         dy = -MATH.sin(rad_heading) * pixel_speed

#         # Debug: Print movement deltas
#         print(f'{self.name} Moving: dx={dx:.3f}, dy={dy:.3f}')

#         self.x += dx
#         self.y += dy

#         # Update trail
#         trail_spacing = 15
#         tx = self.x - self.last_trail_position[0]
#         ty = self.y - self.last_trail_position[1]
#         t_distance = MATH.sqrt(tx ** 2 + ty ** 2)
#         if t_distance > trail_spacing:
#             self.trail.append((self.x, self.y))
#             self.last_trail_position = (self.x, self.y)
#         if len(self.trail) > 1000:
#             self.trail.pop(0)


#     def smooth_turn(self):
#         delta = (self.target_heading - self.heading) % 360
#         if delta > 180:
#             delta -= 360
#         turn_step = min(abs(delta), self.turn_rate) * (1 if delta > 0 else -1)
#         self.heading = (self.heading + turn_step) % 360
