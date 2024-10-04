from totos.get_coord import get_coordinates
from totos.compute_distance import compute_distance
if __name__ == '__main__':
    first_place = input("What's your first address?")
    second_place = input("What's your second address?")

    first_coords = get_coord(first_place)
    second_coords = get_coord(second_place)

    distance = compute_distance(first_coords, second_coords)

    print(f""" The distance between {first_place} and {second_place} is {distance} """)
