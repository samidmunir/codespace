import pygame as PG

from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    VORTAC_POS_X,
    VORTAC_POS_Y,
    VORTAC_RADIUS,
)

from vortac import Vortac

def main():
    PG.init()
    SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    PG.display.set_caption('Autonomous VOR-TAC')
    
    VORTAC = Vortac(name = 'S147', x = VORTAC_POS_X, y = VORTAC_POS_Y, radius = VORTAC_RADIUS)
    
    RUNNING = True
    while RUNNING:
        for event in PG.event.get():
            if event.type == PG.QUIT:
                RUNNING = False
            elif event.type == PG.KEYDOWN:
                if event.key == PG.K_ESCAPE:
                    RUNNING = False
        
        SCREEN.fill(BACKGROUND_COLOR)
        
        VORTAC.draw(screen = SCREEN)
        
        PG.display.update()

if __name__ == '__main__':
    main()