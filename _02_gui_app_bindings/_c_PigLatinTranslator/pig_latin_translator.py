"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
from PigLatinConverter import PigLatinConverter

class PigLatinTranslator(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize an Entry (tk.Entry) for the input text
        self.input = tk.Entry(self)
        self.input.place(relx = 0.05,rely=0.1,relwidth = 0.9,relheight = 0.1)
        # TODO: Declare and initialize a Button (tk.Button) that will translate
        #  the input text to pig latin when pressed
        self.b = tk.Button(self, text = 'Translate', bg = 'green', fg = 'black',
                           font = ('courier new', 13, 'bold'), relief = 'solid')
        self.b.place(relx = 0.37, rely = 0.196, relwidth = 0.2, relheight= 0.106)
        # TODO: Declare and initialize an label (tk.Label) for the translated
        #  text
        self.label = tk.Label(self, text= '', bg='grey', fg='black',
                              font=('Times New Roman', 10, 'bold'), relief='solid')
        self.label.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.1)
        # TODO: Look at the example image () and place all the
        #  components in the same order

        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released
        self.b.bind('<ButtonPress>', self.on_key_press)

    def on_key_press(self, event):
        print('button pressed!')
        recieve = self.input.get()
        Converter = PigLatinConverter.translate(recieve)
        self.label.configure(text = Converter)


        # TODO: Use the _c_PigLatinTranslator.translate() method to translate
        #  the text in the input entry and set the text in the output entry


if __name__ == '__main__':
    pig_latin = PigLatinTranslator()
    pig_latin.geometry('600x300')
    pig_latin.title('Pig Latin')
    pig_latin.mainloop()
    pass
    # TODO: Create a new _c_PigLatinTranslator object and set the title and geometry.
    #  Remember to call mainloop() at the end
