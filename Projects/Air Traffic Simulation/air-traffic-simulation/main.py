import pygame as PG
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    FPS,
    AIRCRAFT_WIDTH,
)
from aircraft import Aircraft

def main():
    PG.init()
    SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    PG.display.set_caption('Air Traffic Simulation')
    CLOCK = PG.time.Clock()
    
    AIRCRAFTS = []
    
    aircraft_a = Aircraft(flight_number = 'N147SM', type = 'C172', x = 450, y = 450, speed = 95, altitude = 2500, heading = 0)
    aircraft_b = Aircraft(flight_number = 'JBU315', type = 'A20N', x = 600, y = 750, speed = 250, altitude = 8000, heading = 0)
    aircraft_c = Aircraft(flight_number = 'AAL527', type = 'B38M', x = 200, y = 200, speed = 300, altitude = 22000, heading = 0)
    
    AIRCRAFTS.append(aircraft_a)
    AIRCRAFTS.append(aircraft_b)
    AIRCRAFTS.append(aircraft_c)
    
    RUNNING = True
    while RUNNING:
        SCREEN.fill(BACKGROUND_COLOR)
        
        for EVENT in PG.event.get():
            if EVENT.type == PG.MOUSEBUTTONDOWN:
                mouse_pos = PG.mouse.get_pos()
                for aircraft in AIRCRAFTS:
                    aircraft.selected = aircraft.is_clicked(mouse_pos)
            for aircraft in AIRCRAFTS:
                if aircraft.selected:
                    if EVENT.type == PG.KEYDOWN and EVENT.key == PG.K_LEFT:
                        if (aircraft.heading - 15 < 0):
                            aircraft.heading = 360
                        aircraft.heading -= 15
                    if EVENT.type == PG.KEYDOWN and EVENT.key == PG.K_RIGHT:
                        if (aircraft.heading + 15 > 360):
                            aircraft.heading = 0
                        aircraft.heading += 15
            if EVENT.type == PG.KEYDOWN:
                if EVENT.key == PG.K_ESCAPE:
                    RUNNING = False
            if EVENT.type == PG.QUIT:
                RUNNING = False
        
        for aircraft in AIRCRAFTS:
            if aircraft.x < 0 or aircraft.x > SCREEN_WIDTH or aircraft.y < 0 or aircraft.y > SCREEN_HEIGHT:
                AIRCRAFTS.remove(aircraft)
            label_color =  (255, 255, 255)
            if aircraft.selected:
                label_color = (255, 255, 0)
            aircraft.move()
            aircraft.draw(screen = SCREEN, label_color = label_color)
        
        PG.display.flip()
        CLOCK.tick(FPS)
    
    PG.quit()

if __name__ == '__main__':
    main()