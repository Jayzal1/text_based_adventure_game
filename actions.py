import classes
from character_classes import current_player
import rooms
import config


def do_action(action):
    for element in action_dict.keys():
        if str(element) in str(action):
            target = action.replace(element, '')
            if not target:
                # action with no input
                target_function = action_dict[element]
                text = target_function()
                return True, text
            else:
                # action with an input
                target = action.replace(element + ' ', '')
                text = action_dict[element](target)
                return True, text

    return False, [config.command_fail_text]


def move_to_room(target):
    if current_player.current_room.name.lower() == target:
        print("you are already in this room")
        return True
    for element in rooms.room_instances:
        if element.name.lower() == target:
            print(element.name.lower())
            print(target)
            current_player.current_room = element
            print("you move to " + str(target))
            return True
    print("there is no such room here as " + str(target))
    return False


def look_at(target):
    current_room = current_player.current_room
    for element in current_room.items:
        if element.name == target:
            return [element.description]
    if target in current_player.inventory:
        return "this is in your inventory not in the room!"
    elif isinstance(target, classes.Item):
        target = str(target).replace("look at", '')
        if target in current_room.items:
            print(target.description(classes.Item.description))
    else:
        print("you see no " + "'" + target + "'" + " around")


def print_player_location():
    print("you are in the " + current_player.current_room.name)

# def attack(target):


def help():
    text = ['this is the help section', "Type 'actions' for a list of all the commands in the game"]
    # print("Type 'actions' for a list of all the commands in the game")
    return text


def check_for_action(input_action):
    result = callable(input_action)
    print(result)
    return result


def get_actions():
    actions = get_action_strings()
    return actions


def look():
    if not current_player.current_room.items:
        return "you see no items around you"
    text = ["you look around you and find the following items:"]
    for element in current_player.current_room.items:
        text.append(element.name)
    return text


def toggle_debug():
    config.debug = True
    print("Enabled Debug Outputs")


def test_function():
    pass
    # display.send_text('this is a test')


action_dict = {
        "look at": look_at,
        "help": help,
        "where am i?": print_player_location,
        "move to": move_to_room,
        "actions": get_actions,
        "look": look,
        "debug": toggle_debug,
        "test function": test_function,
    }


def get_action_strings():
    action_list = list(action_dict.keys())
    return action_list
