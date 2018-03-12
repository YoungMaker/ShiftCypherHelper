import string
from tkinter import *
from tkinter import ttk

cypherText = "IUUBL ESBCJ GMANT ODRZC VUITT ALESA BJHGF RNBNT OMBUG HBTTH AUNBN"

strs = string.ascii_uppercase

def shiftBy(shift, inputStr):
    inputStr = inputStr.upper()
    shiftText = ""
    for char in inputStr:
        if char in strs:
            shiftText += " " + strs[(strs.index(char) + shift) % 26]
        else:
            shiftText += "" +  char
    return shiftText

if __name__ == '__main__':
    root = Tk()
    root.title("Shift Cipher Helper")
    mainFrame = ttk.Frame(root)

    textShift1 = ttk.Label(mainFrame, text = shiftBy(-1, cypherText)).pack()
    cText = ttk.Label(mainFrame, text=shiftBy(0, cypherText)).pack()
    textShift2 = ttk.Label(mainFrame, text = shiftBy(1, cypherText)).pack()

    mainFrame.pack()


    root.mainloop()
