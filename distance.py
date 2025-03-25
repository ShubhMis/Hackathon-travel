import openrouteservice

# Initialize OpenRouteService Client
API_KEY = "5b3ce3597851110001cf624884beac4eb5d94998be0e19ba1041bf5a"  # Replace with your actual API key
client = openrouteservice.Client(key=API_KEY)

def get_coordinates(place_name):
    """
    Convert a place name into (longitude, latitude) coordinates using OpenRouteService.
    :param place_name: Name of the place (e.g., "New York, USA")
    :return: Tuple (longitude, latitude) or None if not found
    """
    try:
        result = client.pelias_search(place_name)
        if result and 'features' in result and len(result['features']) > 0:
            coords = result['features'][0]['geometry']['coordinates']
            return tuple(coords)  # Returns (longitude, latitude)
        else:
            return None
    except Exception as e:
        return None

def get_distance_all_modes(origin_name, destination_name):
    """
    Fetch distance and travel time for all transport modes using OpenRouteService API.
    
    :param origin_name: Place name for the origin
    :param destination_name: Place name for the destination
    :return: Dictionary containing a single distance value & travel times for each mode
    """
    try:
        # Convert place names to coordinates
        origin_coords = get_coordinates(origin_name)
        destination_coords = get_coordinates(destination_name)

        if not origin_coords or not destination_coords:
            return {"error": "Could not find coordinates for one or both locations."}

        # Travel modes to check
        travel_modes = ["driving-car", "cycling-regular", "foot-walking"]
        results = {}

        # Get distance and travel time for driving-car first (to use the same distance for all)
        route = client.directions(
            coordinates=[origin_coords, destination_coords],
            profile="driving-car",
            format="geojson"
        )
        
        distance_km = route['features'][0]['properties']['segments'][0]['distance'] / 1000  # Convert meters to km
        
        # Fetch travel times for each mode (keeping the same distance)
        for mode in travel_modes:
            route = client.directions(
                coordinates=[origin_coords, destination_coords],
                profile=mode,
                format="geojson"
            )
            duration_min = route['features'][0]['properties']['segments'][0]['duration'] / 60  # Convert seconds to minutes
            
            results[mode] = round(duration_min, 2)  # Store only travel time
        
        return {
            "origin": origin_name,
            "destination": destination_name,
            "distance_km": round(distance_km, 2),  # Keep distance same for all modes
            "travel_time_min": results  # Only travel times for each mode
        }
    
    except Exception as e:
        return {"error": str(e)}

# Example Usage
origin_place = input("Enter the starting place: ")  # Example: "Bangalore, India"
destination_place = input("Enter the destination: ")  # Example: "Hyderabad, India"

result = get_distance_all_modes(origin_place, destination_place)
print(result)
