"""
    config.py
    - This file handles the configuration constants & settings for the air-traffic-simulation.
"""
import pygame as PG

# General configuration
FPS = 120

# Screen configuration
BACKGROUND_COLOR = (38, 38, 38)
PG.display.set_mode((0, 0), PG.FULLSCREEN)
SCREEN_INFO = PG.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_INFO.current_w, SCREEN_INFO.current_h

# Aircraft configuration
MAX_NUMBER_AIRCRAFTS = 1
AIRCRAFT_COLOR = (0, 153, 255)
AIRCRAFT_WIDTH = 10
AIRCRAFT_HEIGHT = 10
AIRCRAFT_SPEED_SCALAR = 0.0005
# AIRCRAFT_SPEED_SCALAR = 0.00025
AIRCRAFT_HEADING_VECTOR_LENGTH = 50

# Waypoint configuration
WAYPOINT_SIZE = 7