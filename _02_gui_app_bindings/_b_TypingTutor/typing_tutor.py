"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
import random

# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class TypingTutor(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize a member variable to hold a
        #  random letter to type
        self.random_letter = generate_random_letter() # 'w'
        # TODO: Declare and initialize a label (tk.Label) and set the text to the random letter
        self.label = tk.Label(self, text = self.random_letter, bg = 'blue', fg = 'black',
                              font = ('Times New Roman', 20, 'bold'),relief = 'solid')
        self.label.place(relx = 0.2, rely= 0.2, relwidth = 0.5, relheight = 0.3)
        # TODO: Place the label in the center of the window
        self.label.focus_set()
        # TODO: Call the label's focus_set() method so key presses can be detected

        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released
        #  example: self.label.bind('<KeyRelease>', self.on_key_release)
        self.label.bind('<KeyRelease>', self.on_key_release)

    def on_key_release(self, event):
        letter_pressed = event.char
        print('key ' + letter_pressed + ' released!')
        if letter_pressed == self.random_letter:
            self.label.configure(bg='green')
            self.random_letter = generate_random_letter() # 't'
            self.label.configure(text=self.random_letter)

        else:
            self.label.configure(bg = 'red')
        # TODO: If the user pressed the correct key,
        #         change the label's background to green
        #       If the user pressed the wrong key,
        #         change the label's background to red
        #  example: self.label.configure(bg='green')

        # TODO: Get a new random letter and place it on the label
        #  example: self.label.configure(text=self.rand_letter)


if __name__ == '__main__':
    typing = TypingTutor()
    typing.title('Typing')
    typing.geometry('500x500')
    typing.mainloop()
    pass
    # TODO: Create a new _b_TypingTutor object and set the title and geometry.
    #  Remember to call mainloop() at the end
