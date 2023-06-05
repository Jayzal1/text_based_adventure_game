import tkinter as tk
import actions
import config

root = tk.Tk()                      # global root
root.title(config.game_name)        # Sets the window title
root.geometry("400x300")            # Sets the window size
entry = tk.Entry(root)              # renders text entry box
entry.pack()


def send_text(*args):
    text = entry.get()    # gets text from entry box
    entry.delete(0, tk.END)             # clears entry box
    return_text = actions.do_action(text)     # send text to action factory
    return_text = return_text[1]
    # label = tk.Label(root, text='command: ' + text)   # creates a new label to display command
    # label.pack()
    if return_text:
        for element in return_text:
            return_label = tk.Label(root, text=element)
            return_label.pack()
    else:
        print('unrecognised command')
    root.update()


root.bind('<Return>', send_text)            # Binds the enter button
send_button = tk.Button(root, text="send", command=send_text)    # Renders send text button
send_button.pack()


def loop():
    root.mainloop()
