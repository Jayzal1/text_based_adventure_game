import item_classes
import config
import random


room_instances = []
# room_coordinates = {}


def spawn_items_in_room(room):
    Room.items = [item_classes.Sword()]


class Room:

    def __init__(self):
        spawn_items_in_room(self)

    name = str
    size = 10
    items = []
    coordinates = 0, 0


class MainHall(Room):
    name = "Main Hall"


class Cupboard(Room):
    name = "Cupboard"


# need to write this function
def find_room_by_coordinates(coordinates):
    global room_instances
    for element in room_instances:
        if element.coordinates == coordinates:
            return True, element


# need to write this function
def find_adjacent_rooms(target_room):
    # from character_classes import Player
    coordinates = target_room.coordinates
    search_locations = [
        # north, south, east, west
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]
    adjacent_rooms = []
    for element in search_locations:
        coordinates_to_check = coordinates[0] + element[0], coordinates[1] + element[1]
        result = find_room_by_coordinates(coordinates_to_check)
        if result:
            adjacent_rooms.append(result[1])
    return adjacent_rooms


def find_room(target):
    for element in room_instances:
        if element.name.lower() == target.lower():
            return True, element
    return False, 'None'


def find_free_adjacent_coordinate(target_room):
    current_adjacent_rooms = find_adjacent_rooms(target_room)
    if len(current_adjacent_rooms) <= 2:
        search_locations = [
            # north, south, east, west
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        random.shuffle(search_locations)
        for target in search_locations:
            # element.coordinates
            search_target = target[0] + target_room.coordinates[0], target[1] + target_room.coordinates[1]
            if not find_room_by_coordinates(search_target):
                return True, search_target
    return False, [0, 0]


def spawn_rooms():
    # return
    global room_instances
    index = 0
    for subclass in Room.__subclasses__():
        spawned_instance = subclass()
        if index == 0:
            spawned_instance.coordinates = config.spawn_coordinates
        else:
            local_instances = room_instances
            random.shuffle(local_instances)
            for element in local_instances:
                free_coordinates = find_free_adjacent_coordinate(element)
                if free_coordinates[0]:
                    spawned_instance.coordinates = free_coordinates[1]
                    break
        index = index + 1
        room_instances.append(spawned_instance)
