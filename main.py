from tkinter import *
import math

scrn = 0

class calci(Tk):

    def dele(self):
        length = len(self.screen.get())
        self.screen.delete(length -2, 'end')

    def click(self, event):

        text = event.widget.cget("text")
        # print(text)
        if text == "=":
            if self.scrn.get().isdigit():
                val = int(self.scrn.get())
            else:
                val = eval(self.screen.get())
                self.scrn.set(val)
                self.screen.update()

        elif text == "AC":
                self.scrn.set("")

        else:
            self.scrn.set(self.scrn.get() + text)
            screen = self.update()

    def __init__(self):
        super().__init__()
        self.maxsize(310,220)
        self.title("My Calcuator")
        self.wm_iconbitmap("icon.ico")

    def screene(self):

        self.scrn = StringVar()
        self.focus_set()
        self.screen = Entry(textvariable = self.scrn, font = "lucida 12 bold")
        self.screen.grid(row=0, column=0, columnspan=175, padx = 40, pady=6)
        self.config(bg = "grey")


    def buttonee(self):
        Button(text = "1", font = "2").grid(row = 1, column  = 0, ipadx = 10, ipady = 10)
        self.bind("<Button-1>", self.click)
        Button(text = "2", font = "2", bg = "light grey").grid(row = 1, column  = 1, ipadx = 10, ipady = 10)
        Button(text = "3", font = "2", bg = "light grey").grid(row = 1, column  = 2, ipadx = 10, ipady = 10)
        Button(text = "4", font = "2", bg = "light grey").grid(row = 2, column  = 0, ipadx = 10, ipady = 10)
        Button(text = "5", font = "2", bg = "light grey").grid(row= 2, column  = 1, ipadx = 10, ipady = 10)
        Button(text = "6", font = "2", bg = "light grey").grid(row = 2, column  = 2, ipadx = 10, ipady = 10)
        Button(text = "7", font = "2",bg = "light grey").grid(row = 3, column  = 0, ipadx = 10, ipady = 10)
        Button(text = "8", font = "2", bg = "light grey").grid(row = 3, column  = 1, ipadx = 10, ipady = 10)
        Button(text = "9", font = "2", bg = "light grey").grid(row = 3, column  = 2, ipadx = 10, ipady = 10)
        Button(text="0", font="2", bg="white").grid(row=1, column=4, ipadx=11, ipady=10)
        Button(text = "+", font = "2", bg = "light blue").grid(row = 2, column = 4, ipadx = 10, ipady = 10)
        Button(text="-", font="2", bg = "light blue").grid(row=3, column=4, ipadx=12, ipady=10)
        Button(text="*", font="2", bg = "light blue").grid(row=2, column=5, ipadx=12, ipady=10)
        Button(text="/", font="2", bg = "light blue").grid(row=3, column=5, ipadx=13, ipady=10)
        Button(text="AC", font="2", bg = "red", fg="white").grid(row=1, column=5, ipadx=2, ipady=10)
        Button(text="C", font="2", bg = "light green", command = lambda: self.dele()).grid(row=1, column=6, ipadx=10, ipady=10)
        Button(text="=", font="2", bg = "white").grid(row=2, column=6, ipadx=11, ipady=40, rowspan = 10, columnspan=5)
        self.bind("<Button-1>", self.click)



if __name__ == '__main__':
    window = calci()
    window.screene()
    window.buttonee()
    window.mainloop()
