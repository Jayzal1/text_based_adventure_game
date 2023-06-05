import tkinter as tk
import actions
import config

root = tk.Tk()                      # global root
root.title(config.game_name)        # Sets the window title
root.geometry("400x300")
input_container = tk.Frame(root)
input_container.pack()
# Sets the window size
entry = tk.Entry(input_container)              # renders text entry box
entry.pack()
output_container = tk.Frame(root)
output_container.pack()


def clear_frame_labels(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()


def send_text(*args):
    text = entry.get()    # gets text from entry box
    entry.delete(0, tk.END)             # clears entry box
    return_text = actions.do_action(text)[1]     # send text to action factory
    # return_text = return_text[1]
    # label = tk.Label(root, text='command: ' + text)   # creates a new label to display command
    # label.pack()
    clear_frame_labels(output_container)
    # output_container.delete(0, tk.end)  # clear the return text box
    if return_text:
        for index, element in enumerate(return_text):
            return_label = tk.Label(output_container, text=element)
            return_label.grid()
            root.update()


root.bind('<Return>', send_text)            # Binds the enter button
send_button = tk.Button(input_container, text="send", command=send_text)    # Renders send text button
send_button.pack()


def loop():
    root.mainloop()
