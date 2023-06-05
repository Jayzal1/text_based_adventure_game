import config
import item_classes
import rooms
import classes


class Player(classes.Character):
    health = 200
    inventory = [item_classes.Sword]
    current_room = None
    coordinates = 0, 0


current_player: Player = Player()


def spawn_player():
    global current_player
    main_hall = rooms.find_room(config.spawn_location)
    current_player.current_room = main_hall[1]
    if config.debug:
        print("Spawned Player")
