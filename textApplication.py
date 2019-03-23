from tkinter import *
from tkinter import messagebox
import re

class CountingApp:
    def __init__(self, master):
        self.master = master
        master.title("Counter Application")

        self.letterBox = Entry(master, bg = "grey")
        self.letterBox.grid(row=0, column = 0)

        self.buttonCountLetters = Button(master, text="Count Letters", command=self.countLetters)
        self.buttonCountLetters.grid(row=0, column=1)

        self.buttonCountWords = Button(master, text="Count Words", command=self.countWords)
        self.buttonCountWords.grid(row=2, column=1)

        self.buttonQuit = Button(master, text="Quit", command=self.quitProg)
        self.buttonQuit.grid(row=0, column = 3)

        self.letterNumber = Label(master, text = "Number of Letters:")
        self.letterNumber.grid(row=1, column=0)

        self.wordNumber = Label(master, text="Number of Words:")
        self.wordNumber.grid(row=3, column=0)

        self.textBox2 = Text(master, bg = "grey", height = 5, width = 25)
        self.textBox2.grid(row=2, column=0)

    def quitProg(self):
        messagebox.showinfo("Exit", "Thanks for using the application!")
        exit()

    def countLetters(self):
        new = self.letterNumber

        count = 0
        foo = self.letterBox.get()

        foo = re.sub(r'[^\w\s]','',foo)
        foo = foo.replace(" ", "")

        for x in foo:
            count = count + 1

        new.configure(text= "Number of Letters: " + str(count))

    def countWords(self):
        new = self.wordNumber

        count = 0

        #https://tkdocs.com/tutorial/text.html
        foo = self.textBox2.get('0.0', 'end')

        foo = foo.split()

        for x in foo:
            count = count + 1

        new.configure(text= "Number of words: " + str(count))


if __name__ == '__main__':
    root = Tk()
    root.configure(background = 'white')
    App = CountingApp(root) #creates instance of my class app
    root.mainloop()
