"""
 Create an app that tells a joke, then a punchline
"""
import tkinter as tk
import random
from tkinter import messagebox


# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class ChuckleClicker(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize 2 buttons (tk.Button)
        #  one button for the joke and another for the punchline
        self.joke_button = tk.Button(self, text = 'Joke', fg = 'black',
                                font = ('Times New Roman', 20, 'bold'))
        self.joke_button.place(relx = 0.02, rely = 0.1, relwidth = 0.5, relheight = 0.8)
        self.punchline_button = tk.Button(self, text='Punchline', fg='black',
                                font=('Times New Roman', 20, 'bold'))
        self.punchline_button.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.8)
        # TODO: Place the 2 buttons next to each other (see example image)

        # TODO: Call the joke button's bind() method to call the on_joke()
        #  method when a mouse button is pressed
        #  example: self.joke_button.bind('<ButtonPress>', self.on_joke)
        self.joke_button.bind('<ButtonPress>', self.on_joke)
        # TODO: Call the joke button's bind() method to call the on_punchline()
        #  method when a mouse button is pressed
        self.punchline_button.bind('<ButtonPress>', self.on_punchline)
    def on_joke(self, event):
        messagebox.showinfo(title = '', message = 'I asked a Frenchman if he played any video games...')

        # TODO: Write your joke below!

    def on_punchline(self, event):
        messagebox.showinfo(title = '', message = 'He said Wii....')

        # TODO: Write a punchline to your joke!


if __name__ == '__main__':
    laugh = ChuckleClicker()
    laugh.geometry('300x500')
    laugh.title('Joking')
    laugh.mainloop()
    pass
    # TODO: Create a new ChuckleClicker object and set the title and geometry.
    #  Remember to call mainloop() at the end

