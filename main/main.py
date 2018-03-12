import string
from tkinter import *

cypherText = "IUUBL ESBCJ GMANT ODRZC VUITT ALESA BJHGF RNBNT OMBUG HBTTH AUNBN"

strs = string.ascii_uppercase #reference string of ascii upercase letters

maxShift = 1

#algorithm based on
#https://stackoverflow.com/questions/14424500/text-shift-function-in-python
def shiftBy(shift, inputStr):
    inputStr = inputStr.upper()
    shiftText = ""
    for char in inputStr:
        if char in strs:
            shiftText += "" + strs[(strs.index(char) + shift) % 26]
        else:
            shiftText += "" +  char
    return shiftText

#Todo: invert current color
def highlight(event):
    if event.widget.cget("fg") == "red":
        event.widget.config(fg="black")
    else:
        event.widget.config(fg="red")



def createLabels(parent, shift, inputStr, rowStart, backwards=False, font='Helvetica 22 bold'):
    labelList = []
    if not backwards:
        for x in range(shift):
            labelList.append(
                createRow(parent, shiftBy(x + 1, inputStr), x+rowStart)
            )
    else:
        for x in range(shift, 0, 1):
            labelList.append(
                createRow(parent, shiftBy(x, inputStr), (-1*x)+rowStart)
            )

    return labelList

def createRow(parent, text, rowNum, font='Helvetica 22 bold'):
    labelList = []
    col =0
    for char in text:
        if char in strs:
            cLabel = Label(parent, text=char,
                       font=font)
            cLabel.bind("<Button-1>", highlight)
            cLabel.grid(row=rowNum, column=col)
            labelList.append(cLabel)

        else:
            cLabel = Label(parent, text=char,
                           font=font).grid(row=rowNum, column=col)
            labelList.append(cLabel)

        col+=1

    return labelList




if __name__ == '__main__':
    root = Tk()
    root.title("Shift Cipher Helper")
    mainFrame = Frame(root)

    mainFrame.grid(column=len(cypherText)+1, row=(maxShift*2)+1, sticky=(N, W, E, S))


    createLabels(mainFrame, -1 * maxShift, cypherText, 0, backwards=True)

    createRow(mainFrame, cypherText,  maxShift+1)

    createLabels(mainFrame, maxShift, cypherText, maxShift+2, backwards=False)

    #add all items to the grid layout in mainFrame
    # count = 0
    # for child in mainFrame.winfo_children():
    #     child.grid(column=0, row=count)
    #     count += 1

    root.mainloop()
