import pygame as PG
import random
import math as MATH
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    FPS,
    AIRCRAFT_WIDTH,
    MAX_NUMBER_AIRCRAFTS
)
from waypoint import Waypoint
from aircraft import Aircraft

def parse_waypoints_data():
    WAYPOINTS = []
    with open('waypoints_2.txt', 'r') as file:
        LINES = file.readlines()
        for LINE in LINES:
            data = LINE.strip().split(',')
            name = data[0]
            x = int(data[1])
            y = int(data[2])
            waypoint = Waypoint(name, x, y)
            WAYPOINTS.append(waypoint)
    return WAYPOINTS

def generate_random_aircraft(waypoints):
    flight_num = random.randint(0, 1000)
    type = random.choice(['C172', 'C208', 'B738', 'B77W', 'A20N', 'A320', 'A332', 'TBM9'])
    x = random.randint(100, 1300)
    y = random.randint(100, 1300)
    speed = 250
    altitude = 5000
    if type == 'C172' or type == 'C208':
        speed = random.randint(75, 120)
        altitude = random.randint(1000, 10000)
    elif type == 'TBM9':
        speed = random.randint(85, 230)
        altitude = random.randint(1000, 30000)
    else:
        speed = random.randint(160, 350)
        altitude = random.randint(2000, 40000)
    heading = random.choice([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 225, 240, 255, 270, 285, 300, 315, 330, 345, 360])
    # aircraft = Aircraft(flight_number = flight_num, type = type, x = x, y = y, speed = speed, altitude = altitude, heading = heading, waypoints = generate_random_route(x, y, waypoints, SCREEN_WIDTH, SCREEN_HEIGHT))
    route = generate_interpolated_route(x, y, 50, 800, waypoints)
    aircraft = Aircraft(flight_number = flight_num, type = type, x = x, y = y, speed = speed, altitude = altitude, heading = heading, waypoints = route)
    
    print(f'\n{flight_num}')
    for wp in route:
        print(wp.name)
    print('-----')
    
    return aircraft

def generate_interpolated_route(start_x, start_y, dest_x, dest_y, waypoints):
    waypoints = waypoints.copy()
    route = []
    
    route.append(Waypoint('I001', start_x, start_y))
    
    current_x, current_y = start_x, start_y
    
    while waypoints:
        nearest_waypoint = min(
            waypoints,
            key = lambda wp: MATH.sqrt((wp.x - current_x) ** 2 + (wp.y - current_y) ** 2)
        )
        route.append(nearest_waypoint)
        current_x, current_y = nearest_waypoint.x, nearest_waypoint.y
        waypoints.remove(nearest_waypoint)
    
        if all(
            MATH.sqrt((wp.x - current_x) ** 2 + (wp.y - current_y) ** 2) >= MATH.sqrt((dest_x - current_x) ** 2 + (dest_y - current_y) ** 2) for wp in waypoints
        ):
            break
    
    route.append(Waypoint('D001', dest_x, dest_y))
    
    return route

def generate_random_route(xi, yi, waypoints, airspace_width, airspace_height):
    route = []
    
    cx, cy = xi, yi
    
    nearest_waypoint = min(waypoints, key=lambda wp: MATH.sqrt((wp.x - cx) ** 2 + (wp.y - cy) ** 2))
    route.append(nearest_waypoint)
    
    while True:
        next_waypoint = None
        min_distance = float('inf')
        
        for wp in waypoints:
            if wp not in route:
                distance = MATH.sqrt((wp.x - cx) ** 2 + (wp.y - cy) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    next_waypoint = wp
        
        if not next_waypoint:
            break
        
        route.append(next_waypoint)
        cx, cy = next_waypoint.x, next_waypoint.y
    
    exit_waypoint = Waypoint('EX1', 50, 800)
    route.append(exit_waypoint)
    
    return route

def main():
    PG.init()
    SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    PG.display.set_caption('Air Traffic Simulation')
    CLOCK = PG.time.Clock()
    
    WAYPOINTS = parse_waypoints_data()
    
    AIRCRAFTS = []
    
    # aircraft_a = Aircraft(flight_number = 'N147SM', type = 'C172', x = 450, y = 450, speed = 95, altitude = 2500, heading = 0, waypoints = generate_random_route(450, 450, WAYPOINTS, SCREEN_WIDTH, SCREEN_HEIGHT))
    # aircraft_b = Aircraft(flight_number = 'JBU315', type = 'A20N', x = 600, y = 750, speed = 250, altitude = 8000, heading = 0, waypoints = generate_random_route(600, 750, WAYPOINTS, SCREEN_WIDTH, SCREEN_HEIGHT))
    # aircraft_c = Aircraft(flight_number = 'AAL527', type = 'B38M', x = 200, y = 200, speed = 300, altitude = 22000, heading = 0, waypoints = generate_random_route(200, 200, WAYPOINTS, SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # AIRCRAFTS.append(aircraft_a)
    # AIRCRAFTS.append(aircraft_b)
    # AIRCRAFTS.append(aircraft_c)
    
    PAUSED = False
    RUNNING = True
    while RUNNING:
        SCREEN.fill(BACKGROUND_COLOR)
        
        for EVENT in PG.event.get():
            if EVENT.type == PG.MOUSEBUTTONDOWN and not PAUSED:
                mouse_pos = PG.mouse.get_pos()
                for aircraft in AIRCRAFTS:
                    aircraft.selected = aircraft.is_clicked(mouse_pos)
            if EVENT.type == PG.KEYDOWN:
                if EVENT.key == PG.K_p:
                    PAUSED = not PAUSED
                if EVENT.key == PG.K_ESCAPE:
                    RUNNING = False
            if EVENT.type == PG.QUIT:
                RUNNING = False
        
        if not PAUSED:
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
        
            for waypoint in WAYPOINTS:
                waypoint.draw(screen = SCREEN)
            
            for aircraft in AIRCRAFTS:
                if aircraft.x < 0 or aircraft.x > SCREEN_WIDTH or aircraft.y < 0 or aircraft.y > SCREEN_HEIGHT:
                    AIRCRAFTS.remove(aircraft)
                label_color =  (255, 255, 255)
                if aircraft.selected:
                    label_color = (255, 255, 0)
                # aircraft.move()
                if aircraft.current_waypoint_index < len(aircraft.waypoints):
                    aircraft.move_toward_waypoint()
                aircraft.draw(screen = SCREEN, label_color = label_color)
            
            while (len(AIRCRAFTS) < MAX_NUMBER_AIRCRAFTS):
                aircraft = generate_random_aircraft(WAYPOINTS)
                AIRCRAFTS.append(aircraft)
        else:
            for waypoint in WAYPOINTS:
                waypoint.draw(screen = SCREEN)
                
            for aircraft in AIRCRAFTS:
                if aircraft.x < 0 or aircraft.x > SCREEN_WIDTH or aircraft.y < 0 or aircraft.y > SCREEN_HEIGHT:
                    AIRCRAFTS.remove(aircraft)
                label_color =  (255, 255, 255)
                if aircraft.selected:
                    label_color = (255, 255, 0)
                aircraft.draw(screen = SCREEN, label_color = label_color)
            
            font = PG.font.Font(None, 72)
            text = font.render('PAUSED', True, (255, 255, 255))
            text_rect = text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            SCREEN.blit(text, text_rect)
        
        PG.display.flip()
        CLOCK.tick(FPS)
    
    PG.quit()

if __name__ == '__main__':
    main()