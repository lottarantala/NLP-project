import pywsd
from tkinter import *
from tkinter import ttk

class GUI:

    def __init__(self):
        self.algorithm_options = ["Original Lesk", "Simple Lesk", "Adapted Lesk", "Cosine Lesk"]

        # Main window
        self.main = Tk()
        self.main.title("Word disambiguation GUI")

        # Create a frame for grouping items and add padding to it
        self.frame = Frame(self.main, padx=10, pady=10)
        self.frame.grid(row=0, column=0)

        # Text for entry box
        Label(self.frame, text='Sentence').grid(row=0, padx=5, pady=5) 
        Label(self.frame, text='Target word').grid(row=1, padx=5, pady=5)

        # Entry boxes for sentence and target word
        self.sentence = Entry(self.frame, width=40)
        self.target_word = Entry(self.frame, width=40)
        self.sentence.grid(row=0, column=1, padx=5, pady=5)
        self.target_word.grid(row=1, column=1, padx=5, pady=5)

        # Algorithm dropdown menu
        self.clicked = StringVar() 
        self.clicked.set("Original Lesk") 
        drop = OptionMenu(self.frame, self.clicked, *self.algorithm_options ) 
        drop.grid(row=2, padx=5, pady=5) 

        # Disambiguation button
        self.button = Button(self.frame, text='Disambiguate', width=25, command=self.disambiguate) 
        self.button.grid(row=3, padx=5, pady=5)

        # Label to display the result
        self.result_label = Label(self.main, text="", padx=10, pady=10)
        self.result_label.grid(row=1, column=0)

        self.main.mainloop()

    def disambiguate(self):
        algo = self.clicked.get()
        sentence = self.sentence.get()
        targetword = self.target_word.get()
        res = None

        if algo == "Original Lesk":
            res = self.origLesk(sentence, targetword)
        elif algo == "Simple Lesk":
            res = self.simpleLesk(sentence, targetword)
        elif algo == "Adapted Lesk":
            res = self.adaptedLesk(sentence, targetword)
        elif algo == "Cosine Lesk":
            res = self.cosLesk(sentence, targetword)
        else:
            pass

        if res is not None:
            self.result_label.config(text=res)
        else:
            self.result_label.config(text="No definition found.")

    def cosLesk(self, sentence, targetword):
        result = pywsd.cosine_lesk(sentence, targetword, hyperhypo=True)
        return result.definition() if result is not None else None

    def origLesk(self, sentence, targetword):
        result = pywsd.original_lesk(sentence, targetword)
        return result.definition() if result is not None else None

    def adaptedLesk(self, sentence, targetword):
        result = pywsd.adapted_lesk(sentence, targetword, hyperhypo=True)
        return result.definition() if result is not None else None

    def simpleLesk(self, sentence, targetword):
        result = pywsd.simple_lesk(sentence, targetword, hyperhypo=True)
        return result.definition() if result is not None else None
    
if __name__ == "__main__":
    gui = GUI()