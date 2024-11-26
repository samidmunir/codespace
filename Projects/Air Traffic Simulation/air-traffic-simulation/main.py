#         # event handling
#         # keys = pygame.key.get_pressed()
#         # if keys[pygame.K_LEFT]:
#         #     aircraft.turn('left')
#         # if keys[pygame.K_RIGHT]:
#         #     aircraft.turn('right')
import pygame as PG
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    FPS,
)
from aircraft import Aircraft

def main():
    PG.init()
    SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    PG.display.set_caption('Air Traffic Simulation')
    CLOCK = PG.time.Clock()
    
    aircraft = Aircraft(flight_number = 'N147SM', type = 'C172', x = 450, y = 450, speed = 95, altitude = 2500, heading = 0)
    
    RUNNING = True
    while RUNNING:
        SCREEN.fill(BACKGROUND_COLOR)
        
        for EVENT in PG.event.get():
            if EVENT.type == PG.KEYDOWN and EVENT.key == PG.K_LEFT:
                if (aircraft.heading - 90 < 0):
                    aircraft.heading = 360
                aircraft.heading -= 90
                print('left pressed')
            if EVENT.type == PG.KEYDOWN and EVENT.key == PG.K_RIGHT:
                if (aircraft.heading + 90 > 360):
                    aircraft.heading = 0
                aircraft.heading += 90
                print('right pressed')
            
            if EVENT.type == PG.KEYDOWN:
                if EVENT.key == PG.K_ESCAPE:
                    RUNNING = False
            if EVENT.type == PG.QUIT:
                RUNNING = False
        
        aircraft.move()
        aircraft.draw(screen = SCREEN)
        
        PG.display.flip()
        CLOCK.tick(FPS)
    
    PG.quit()

if __name__ == '__main__':
    main()