import pygame as PG

from config import (
    VORTAC_COLOR
)

PG.init()
font = PG.font.Font(None, 18)

class Vortac:
    def __init__(self, name: str, x: float, y: float, radius: float) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        PG.draw.circle(surface = screen, color = VORTAC_COLOR, center = (self.x, self.y), radius = self.radius, width = 3)
        self.draw_label(screen = screen, text = self.name, font = font, color = VORTAC_COLOR, offset = (0, 0))
    
    def draw_label(self, screen, text, font, color, offset = (0, 0)):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center = (self.x + offset[0], self.y + offset[1]))
        screen.blit(text_surface, text_rect)