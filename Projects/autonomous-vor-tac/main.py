import random as RANDOM
import string as STRING
import pygame as PG

from config import (
    FPS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    VORTAC_POS_X,
    VORTAC_POS_Y,
    VORTAC_RADIUS,
    MAX_NUMBER_AIRCRAFTS
)
from vortac import Vortac
from waypoint import Waypoint
from aircraft import Aircraft

def generate_random_aircraft_name() -> str:
    LENGTH = RANDOM.randint(2, 3)
    NAME = ''.join(RANDOM.choice(STRING.ascii_letters) for _ in range(LENGTH))
    NAME += str(RANDOM.randint(1, 1000))
    return NAME

def gen_random_aircraft() -> Aircraft:
    name = generate_random_aircraft_name()
    x = RANDOM.randint(50, SCREEN_WIDTH - 50)
    y = RANDOM.randint(50, SCREEN_HEIGHT - 50)
    heading = RANDOM.randint(0, 360)
    return Aircraft(name = name.upper(), x = x, y = y, heading = heading)

def get_waypoints(filename: str) -> list:
    waypoints = []
    with open(filename, 'r') as FILE:
        for line in FILE:
            name, x, y = line.strip().split(',')
            waypoint = Waypoint(name = name, x = float(x), y = float(y))
            waypoints.append(waypoint)
    FILE.close()
    return waypoints

def main() -> None:
    PG.init()
    SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    PG.display.set_caption('Autonomous VOR-TAC')
    CLOCK = PG.time.Clock()
    
    VORTAC = Vortac(name = 'S147', x = VORTAC_POS_X, y = VORTAC_POS_Y, radius = VORTAC_RADIUS)
    
    WAYPOINTS = get_waypoints('waypoints_config.txt')
    
    AIRCRAFTS = []
    
    RUNNING = True
    PAUSED = False
    while RUNNING:
        SCREEN.fill(BACKGROUND_COLOR)
        
        for EVENT in PG.event.get():
            if EVENT.type == PG.MOUSEBUTTONDOWN and not PAUSED:
                MOUSE_POS = PG.mouse.get_pos()
                for AIRCRAFT in AIRCRAFTS:
                    AIRCRAFT.selected = AIRCRAFT.is_clicked(mouse_pos = MOUSE_POS)
            if EVENT.type == PG.KEYDOWN:
                if EVENT.key == PG.K_p:
                    PAUSED = not PAUSED
                if EVENT.key == PG.K_ESCAPE:
                    RUNNING = False
            if EVENT.type == PG.QUIT:
                RUNNING = False
        
        if not PAUSED:
            for AIRCRAFT in AIRCRAFTS:
                if AIRCRAFT.selected:
                    pass
            
            VORTAC.draw(screen = SCREEN)
            for waypoint in WAYPOINTS:
                waypoint.draw(screen = SCREEN)
            for aircraft in AIRCRAFTS:
                aircraft.draw(screen = SCREEN)
                aircraft.move()
            while (len(AIRCRAFTS) < MAX_NUMBER_AIRCRAFTS):
                AIRCRAFTS.append(gen_random_aircraft())
        else:
            VORTAC.draw(screen = SCREEN)
            for waypoint in WAYPOINTS:
                waypoint.draw(screen = SCREEN)
            for aircraft in AIRCRAFTS:
                aircraft.draw(screen = SCREEN)
            FONT = PG.font.Font(None, 72)
            TEXT = FONT.render('PAUSED', True, (255, 0, 0))
            TEXT_RECT = TEXT.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            SCREEN.blit(TEXT, TEXT_RECT)
        
        PG.display.flip()
        CLOCK.tick(FPS)
    
    PG.quit()

if __name__ == '__main__':
    main()