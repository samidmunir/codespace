import math as MATH
import pygame as PG
from collections import defaultdict

class RouteNetwork:
    def __init__(self, waypoints: list):
        self.waypoints = waypoints
        self.route_network = None

def generate_route_network(waypoints: list, max_distance: int):
    def calculate_distance(x1, y1, x2, y2):
        return MATH.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
    graph = defaultdict(list)
    for i in range(len(waypoints)):
        name_1 = waypoints[i].name
        x_1, y_1 = waypoints[i].x, waypoints[i].y
        for j in range(len(waypoints)) :
            if i != j:
                name_2 = waypoints[j].name
                x_2, y_2 = waypoints[j].x, waypoints[j].y
                distance = calculate_distance(x_1, y_1, x_2, y_2)
                if distance >= 125 and distance <= 150:
                    graph[name_1].append((name_2, distance))
                    graph[name_2].append((name_1, distance))
    return graph

def draw_routes(screen: PG.Surface, waypoints: list, graph):
    waypoint_positions = {waypoint.name: (waypoint.x, waypoint.y) for waypoint in waypoints}

    for start, neighbors in graph.items():
        start_pos = waypoint_positions[start]  # Starting waypoint position
        for end, _ in neighbors:  # Each connected waypoint and its distance
            end_pos = waypoint_positions[end]  # Connected waypoint position
            # Draw a line between waypoints
            PG.draw.line(screen, (255, 255, 255), start_pos, end_pos, 2)  # Green line with thickness 2