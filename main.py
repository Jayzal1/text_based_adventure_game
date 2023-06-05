import actions
import character_classes
import config
import rooms
import display


def print_new(*args, **kwargs):
    # Custom print logic
    display.send_text(args[0])

    # Call the original print function to retain some of the default behavior
    __builtins__.print(*args, **kwargs)


def request_input():
    result = actions.do_action(input(str).lower())
    if not result:
        print('found no command')
    request_input()


def start_game():
    if not character_classes.current_player:
        print("no valid player spawned, ending game")
        exit()
    print("you find yourself in a room with a few items lying about, what would you like to do?")
    request_input()


def finish_game(game_result):
    if game_result:
        text_output = 'completed'
    else:
        text_output = 'lost'
    print("you have " + text_output + ' the game!')
    print("would you like to play the game again? y/n")
    restart = input(str)
    if restart == 'y':
        start_game()
    elif restart == 'n':
        print("quitting the game...")
        exit()


if __name__ == "__main__":
    rooms.spawn_rooms()
    character_classes.spawn_player()
    # start_game()
    display.loop()
