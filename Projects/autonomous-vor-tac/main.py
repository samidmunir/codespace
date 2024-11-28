# import random as RANDOM
# import string as STRING
# import pygame as PG

# from config import (
#     FPS,
#     SCREEN_WIDTH,
#     SCREEN_HEIGHT,
#     BACKGROUND_COLOR,
#     INPUT_BOX_X,
#     INPUT_BOX_Y,
#     INPUT_BOX_WIDTH,
#     INPUT_BOX_HEIGHT,
#     VORTAC_POS_X,
#     VORTAC_POS_Y,
#     VORTAC_RADIUS,
#     MAX_NUMBER_AIRCRAFTS
# )
# from vortac import Vortac
# from waypoint import Waypoint
# from aircraft import Aircraft

# class InputBox:
#     def __init__(self, x, y, w, h):
#         self.rect = PG.Rect(x, y, w, h)
#         self.color_inactive = (255, 255, 255)
#         self.color_active = (0, 255, 0)
#         self.color = self.color_inactive
#         self.text = ''
#         self.font = PG.font.Font(None, 32)
#         self.active = False
    
#     def handle_event(self, event) -> str:
#         if event.type == PG.MOUSEBUTTONDOWN:
#             self.active = self.rect.collidepoint(event.pos)
#             self.color = self.color_active if self.active else self.color_inactive
#         if event.type == PG.KEYDOWN and self.active:
#             if event.key == PG.K_RETURN:
#                 entered_text = self.text
#                 self.text = ''
#                 return entered_text
#             elif event.key == PG.K_BACKSPACE:
#                 self.text = self.text[:-1]
#             else:
#                 self.text += event.unicode
#         return None
    
#     def draw(self, screen):
#         txt_surface = self.font.render(self.text, True, (0, 255, 0))
#         width = max(200, txt_surface.get_width() + 10)
#         self.rect.w = width
#         screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
#         PG.draw.rect(screen, self.color, self.rect, 2)

# def generate_random_aircraft_name() -> str:
#     LENGTH = RANDOM.randint(2, 3)
#     NAME = ''.join(RANDOM.choice(STRING.ascii_letters) for _ in range(LENGTH))
#     NAME += str(RANDOM.randint(1, 1000))
#     return NAME

# def gen_random_aircraft() -> Aircraft:
#     name = generate_random_aircraft_name()
#     x = RANDOM.randint(50, SCREEN_WIDTH - 50)
#     y = RANDOM.randint(50, SCREEN_HEIGHT - 50)
#     heading = RANDOM.randint(0, 360)
#     return Aircraft(name = name.upper(), x = x, y = y, heading = heading)

# def get_waypoints(filename: str) -> list:
#     waypoints = []
#     with open(filename, 'r') as FILE:
#         for line in FILE:
#             name, x, y = line.strip().split(',')
#             waypoint = Waypoint(name = name, x = float(x), y = float(y))
#             waypoints.append(waypoint)
#     FILE.close()
#     return waypoints

# def main() -> None:
#     PG.init()
#     SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     PG.display.set_caption('Autonomous VOR-TAC')
#     CLOCK = PG.time.Clock()
    
#     VORTAC = Vortac(name = 'S147', x = VORTAC_POS_X, y = VORTAC_POS_Y, radius = VORTAC_RADIUS)
    
#     WAYPOINTS = get_waypoints('waypoints_config.txt')
    
#     AIRCRAFTS = []
    
#     INPUT_BOX = InputBox(INPUT_BOX_X, INPUT_BOX_Y, INPUT_BOX_WIDTH, INPUT_BOX_HEIGHT)
    
#     RUNNING = True
#     PAUSED = False
    
#     running = True

#     while running:
#         for event in PG.event.get():
#             if event.type == PG.QUIT:
#                 running = False
            
#             # Handle textbox input
#             entered_text = INPUT_BOX.handle_event(event)
#             if entered_text:
#                 try:
#                     new_heading = float(entered_text)
#                     for aircraft in AIRCRAFTS:
#                         if aircraft.selected:
#                             aircraft.target_heading = new_heading
#                             print(f'New target heading for {aircraft.name}: {new_heading}')
#                             break
#                         else:
#                             print('no aircraft selected!')
#                 except ValueError:
#                     print("Invalid heading entered. Please enter a number.")

#             # Handle aircraft selection
#             if event.type == PG.MOUSEBUTTONDOWN:
#                 if not INPUT_BOX.rect.collidepoint(event.pos):
#                     for aircraft in AIRCRAFTS:
#                         aircraft.selected = aircraft.is_clicked(event.pos)

#         # Update screen
#         SCREEN.fill((38, 38, 38))
#         VORTAC.draw(screen = SCREEN)
#         for waypoint in WAYPOINTS:
#             waypoint.draw(screen = SCREEN)
#         for aircraft in AIRCRAFTS:
#             aircraft.draw(screen = SCREEN)
#             aircraft.move()
#         while (len(AIRCRAFTS) < MAX_NUMBER_AIRCRAFTS):
#             AIRCRAFTS.append(gen_random_aircraft())
#         INPUT_BOX.draw(screen = SCREEN)

#         PG.display.flip()
#         CLOCK.tick(FPS)

#     PG.quit()
    
    
#     """
#     while RUNNING:
#         SCREEN.fill(BACKGROUND_COLOR)
        
#         for EVENT in PG.event.get():
#             # Handle mouse events for selection/input box.
#             if EVENT.type == PG.MOUSEBUTTONDOWN and not PAUSED:
#                 if INPUT_BOX.rect.collidepoint(EVENT.pos):
#                     INPUT_BOX.handle_event(EVENT)
#                 else:    
#                     MOUSE_POS = PG.mouse.get_pos()
#                     for AIRCRAFT in AIRCRAFTS:
#                         AIRCRAFT.selected = AIRCRAFT.is_clicked(mouse_pos = MOUSE_POS)
#             # Handle pause/escape functionality.
#             if EVENT.type == PG.KEYDOWN:
#                 if EVENT.key == PG.K_p:
#                     PAUSED = not PAUSED
#                 if EVENT.key == PG.K_ESCAPE:
#                     RUNNING = False
#             # Handle quitting functionality.
#             if EVENT.type == PG.QUIT:
#                 RUNNING = False
        
#         if not PAUSED:
#             for EVENT in PG.event.get():    
#                 for AIRCRAFT in AIRCRAFTS:
#                     if AIRCRAFT.selected:
#                         target_heading = INPUT_BOX.handle_event(EVENT)
#                         if target_heading:
#                             try:
#                                 AIRCRAFT.target_heading = float(target_heading)
#                             except ValueError:
#                                 print('Invalid heading entered. Please enter a number.')
            
#             VORTAC.draw(screen = SCREEN)
#             for waypoint in WAYPOINTS:
#                 waypoint.draw(screen = SCREEN)
#             for aircraft in AIRCRAFTS:
#                 aircraft.draw(screen = SCREEN)
#                 aircraft.move()
#             while (len(AIRCRAFTS) < MAX_NUMBER_AIRCRAFTS):
#                 AIRCRAFTS.append(gen_random_aircraft())
#             INPUT_BOX.draw(screen = SCREEN)
#         else:
#             VORTAC.draw(screen = SCREEN)
#             for waypoint in WAYPOINTS:
#                 waypoint.draw(screen = SCREEN)
#             for aircraft in AIRCRAFTS:
#                 aircraft.draw(screen = SCREEN)
#             INPUT_BOX.draw(screen = SCREEN)
#             FONT = PG.font.Font(None, 72)
#             TEXT = FONT.render('PAUSED', True, (255, 0, 0))
#             TEXT_RECT = TEXT.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
#             SCREEN.blit(TEXT, TEXT_RECT)
        
#         PG.display.flip()
#         CLOCK.tick(FPS)
    
#     PG.quit()
# """

# if __name__ == '__main__':
#     main()

import random as RANDOM
import string as STRING
import pygame as PG

from config import (
    FPS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    INPUT_BOX_X,
    INPUT_BOX_Y,
    INPUT_BOX_WIDTH,
    INPUT_BOX_HEIGHT,
    VORTAC_POS_X,
    VORTAC_POS_Y,
    VORTAC_RADIUS,
    MAX_NUMBER_AIRCRAFTS
)
from vortac import Vortac
from waypoint import Waypoint
from aircraft import Aircraft

class InputBox:
    def __init__(self, x, y, w, h):
        self.rect = PG.Rect(x, y, w, h)
        self.color_inactive = (255, 255, 255)
        self.color_active = (0, 255, 0)
        self.color = self.color_inactive
        self.text = ''
        self.font = PG.font.Font(None, 32)
        self.active = False
    
    def handle_event(self, event) -> str:
        if event.type == PG.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == PG.KEYDOWN and self.active:
            if event.key == PG.K_RETURN:
                entered_text = self.text
                self.text = ''
                return entered_text
            elif event.key == PG.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return None
    
    def draw(self, screen):
        txt_surface = self.font.render(self.text, True, (0, 255, 0))
        width = max(200, txt_surface.get_width() + 10)
        self.rect.w = width
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
        PG.draw.rect(screen, self.color, self.rect, 2)

def generate_random_aircraft_name() -> str:
    LENGTH = RANDOM.randint(2, 3)
    NAME = ''.join(RANDOM.choice(STRING.ascii_letters) for _ in range(LENGTH))
    NAME += str(RANDOM.randint(1, 1000))
    return NAME

def gen_random_aircraft() -> Aircraft:
    name = generate_random_aircraft_name()
    x = RANDOM.randint(50, SCREEN_WIDTH - 50)
    y = RANDOM.randint(50, SCREEN_HEIGHT - 50)
    speed = RANDOM.randint(150, 350)
    heading = RANDOM.randint(0, 360)
    return Aircraft(name=name.upper(), x=x, y=y, speed = speed, heading=heading)

def get_waypoints(filename: str) -> list:
    waypoints = []
    with open(filename, 'r') as FILE:
        for line in FILE:
            name, x, y = line.strip().split(',')
            waypoint = Waypoint(name=name, x=float(x), y=float(y))
            waypoints.append(waypoint)
    return waypoints

def main() -> None:
    PG.init()
    SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    PG.display.set_caption('Autonomous VOR-TAC')
    CLOCK = PG.time.Clock()
    
    VORTAC = Vortac(name='S147', x=VORTAC_POS_X, y=VORTAC_POS_Y, radius=VORTAC_RADIUS)
    WAYPOINTS = get_waypoints('waypoints_config.txt')
    AIRCRAFTS = []
    INPUT_BOX = InputBox(INPUT_BOX_X, INPUT_BOX_Y, INPUT_BOX_WIDTH, INPUT_BOX_HEIGHT)

    running = True

    while running:
        for event in PG.event.get():
            if event.type == PG.QUIT:
                running = False
            
            # Handle textbox input
            entered_text = INPUT_BOX.handle_event(event)
            if entered_text:
                try:
                    new_heading = float(entered_text)
                    selected_aircraft = next((a for a in AIRCRAFTS if a.selected), None)
                    if selected_aircraft:
                        selected_aircraft.target_heading = new_heading
                        print(f'New target heading for {selected_aircraft.name}: {new_heading}')
                    else:
                        print("No aircraft selected!")
                except ValueError:
                    print("Invalid heading entered. Please enter a number.")

            # Handle aircraft selection
            if event.type == PG.MOUSEBUTTONDOWN:
                if not INPUT_BOX.rect.collidepoint(event.pos):
                    # Deselect all aircraft first
                    for aircraft in AIRCRAFTS:
                        aircraft.selected = False
                    # Select the clicked aircraft
                    for aircraft in AIRCRAFTS:
                        if aircraft.is_clicked(event.pos):
                            aircraft.selected = True
                            break

        # Update screen
        SCREEN.fill(BACKGROUND_COLOR)
        VORTAC.draw(screen=SCREEN)
        for waypoint in WAYPOINTS:
            waypoint.draw(screen=SCREEN)
        for aircraft in AIRCRAFTS:
            aircraft.draw(screen=SCREEN)
            aircraft.move()
            
            if aircraft.x < 0 or aircraft.x > SCREEN_WIDTH or aircraft.y < 0 or aircraft.y > SCREEN_HEIGHT:
                AIRCRAFTS.remove(aircraft)
        while len(AIRCRAFTS) < MAX_NUMBER_AIRCRAFTS:
            AIRCRAFTS.append(gen_random_aircraft())
        # INPUT_BOX.draw(screen=SCREEN)
        
        if any(aircraft.selected for aircraft in AIRCRAFTS):
            INPUT_BOX.draw(screen = SCREEN)

        PG.display.flip()
        CLOCK.tick(FPS)

    PG.quit()

if __name__ == '__main__':
    main()