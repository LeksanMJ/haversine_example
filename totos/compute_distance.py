from haversine import haversine
def compute_distance (first_place: str, second_place: str) -> float:
    return haversine(first_place, second_place) 