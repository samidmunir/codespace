import pygame as PG
import math as MATH
from config import (
    VORTAC_COLOR
)

PG.init()
font = PG.font.Font(None, 18)

class Vortac:
    def __init__(self, name: str, x: float, y: float, radius: float, sweep_angle: float, sweep_speed: float) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.sweep_angle = sweep_angle # radar sweep angle
        self.sweep_speed = sweep_speed # degrees per frame
        self.sweep_surface = PG.Surface((self.radius * 2, self.radius * 2), PG.SRCALPHA)
    
    def draw(self, screen):
        PG.draw.circle(surface = screen, color = VORTAC_COLOR, center = (self.x, self.y), radius = self.radius, width = 3)
        self.draw_radar_sweep(screen = screen)
        self.draw_label(screen = screen, text = self.name, font = font, color = VORTAC_COLOR, offset = (0, 0))
    
    def draw_label(self, screen, text, font, color, offset = (0, 0)):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center = (self.x + offset[0], self.y + offset[1]))
        screen.blit(text_surface, text_rect)
    
    def draw_radar_sweep(self, screen):
        # Clear the transparent surface
        self.sweep_surface.fill((0, 0, 0, 0))

        # Draw the sweeping arc with a gradient
        for alpha, angle_offset in zip(range(255, 0, -15), range(0, 30, 2)):  # Adjust gradient density here
            start_angle = MATH.radians(self.sweep_angle - angle_offset)
            end_angle = MATH.radians(self.sweep_angle)
            color = (0, 255, 0, alpha)  # Green color with decreasing alpha
            
            # Draw the arc segment
            PG.draw.arc(
                self.sweep_surface,
                color,
                (0, 0, self.radius * 2, self.radius * 2),
                start_angle,
                end_angle,
                3,  # Arc width
            )
        
        # Blit the transparent surface onto the screen
        screen.blit(self.sweep_surface, (self.x - self.radius, self.y - self.radius), special_flags=PG.BLEND_RGBA_ADD)

        # Draw the radar line
        sweep_radians = MATH.radians(self.sweep_angle)
        end_x = self.x + MATH.cos(sweep_radians) * self.radius
        end_y = self.y - MATH.sin(sweep_radians) * self.radius
        PG.draw.line(screen, VORTAC_COLOR, (self.x, self.y), (end_x, end_y), 2)

        # Update the sweep angle
        self.sweep_angle = (self.sweep_angle + self.sweep_speed) % 360