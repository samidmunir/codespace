import random as RANDOM
import string as STRING

from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

OUTPUT_FILE = './waypoints_config.txt'
NUMBER_OF_WAYPOINTS = 50
WAYPOINTS = []

def generate_random_name():
    length = RANDOM.randint(4, 5)
    name = ''.join(RANDOM.choice(STRING.ascii_letters) for _ in range(length))
    return name

def main():
    for i in range(NUMBER_OF_WAYPOINTS):
        name = generate_random_name()
        x = RANDOM.randint(50, SCREEN_WIDTH - 50)
        y = RANDOM.randint(50, SCREEN_HEIGHT - 50)
        waypoint = (name, x, y)
        WAYPOINTS.append(waypoint)
        
    with open(OUTPUT_FILE, 'w') as FILE:
        for waypoint in WAYPOINTS:
            FILE.write(f'{waypoint[0].upper()}, {waypoint[1]}, {waypoint[2]}\n')
    FILE.close()
        
if __name__ == '__main__':
    main()