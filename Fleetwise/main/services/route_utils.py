# services/route_utils.py

import osmnx as ox
import networkx as nx
from geopy.geocoders import Nominatim

def geocode_address(address):
    geolocator = Nominatim(user_agent="fleetwise_optimizer")
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        raise ValueError(f"Could not geocode address: {address}")

def compute_route_and_stats(start_address, end_address):
    start_coords = geocode_address(start_address)
    end_coords = geocode_address(end_address)
    center_point = ((start_coords[0] + end_coords[0]) / 2, (start_coords[1] + end_coords[1]) / 2)
    G = ox.graph_from_point(center_point, dist=2000, network_type='drive')
    orig_node = ox.distance.nearest_nodes(G, start_coords[1], start_coords[0])
    dest_node = ox.distance.nearest_nodes(G, end_coords[1], end_coords[0])
    route = nx.shortest_path(G, orig_node, dest_node, weight='length')
    route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]
    length_m = nx.path_weight(G, route, weight='length')
    distance_km = length_m / 1000
    # Estimate duration at 40km/h for example
    duration_min = (distance_km / 40) * 60
    return {
        'route_coords': route_coords,
        'distance_km': distance_km,
        'duration_min': duration_min,
    }
