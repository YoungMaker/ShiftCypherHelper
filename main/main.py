import string
from tkinter import *
from tkinter import ttk

cypherText = "IUUBL ESBCJ GMANT ODRZC VUITT ALESA BJHGF RNBNT OMBUG HBTTH AUNBN"

strs = string.ascii_uppercase

maxShift = 1

#algorithm based on
#https://stackoverflow.com/questions/14424500/text-shift-function-in-python
def shiftBy(shift, inputStr):
    inputStr = inputStr.upper()
    shiftText = ""
    for char in inputStr:
        if char in strs:
            shiftText += " " + strs[(strs.index(char) + shift) % 26]
        else:
            shiftText += "" +  char
    return shiftText

def createLabels(parent, shift, inputStr, backwards=False, font='Helvetica 22 bold'):
    labelList = []
    if not backwards:
        for x in range(shift):
            labelList.append(
                ttk.Label(parent, text=shiftBy(x+1, inputStr),
                      font=font))
    else:
        for x in range(shift, 0, 1):
            print x
            labelList.append(
                ttk.Label(mainFrame, text=shiftBy(x, inputStr),
                          font=font))

    return labelList


if __name__ == '__main__':
    root = Tk()
    root.title("Shift Cipher Helper")
    mainFrame = ttk.Frame(root)

    mainFrame.grid(column=0, row=(maxShift*2)+1, sticky=(N, W, E, S))

    createLabels(mainFrame, -1 * maxShift, cypherText, backwards=True)

    cText = ttk.Label(mainFrame, text=shiftBy(0, cypherText),
                      font='Helvetica 22 bold')


    createLabels(mainFrame, maxShift, cypherText)





    count = 0
    for child in mainFrame.winfo_children():
        child.grid(column=0, row=count)
        count += 1

    root.mainloop()
