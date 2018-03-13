import string
from tkinter import *
from tkinter.ttk import Separator, Style
import os

cipherText = ""

strs = string.ascii_uppercase #reference string of ascii upercase letters

maxShift = 1

outputVarList = []

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
        col = event.widget.grid_info()["column"]
        updateRow(outputVarList, int(col), "")

    else:
        event.widget.config(fg="red")
        col = event.widget.grid_info()["column"]

        updateRow(outputVarList, int(col),  event.widget.cget('text'))

def updateRow(labelList, col, text):
    labelList[int(col)].set(text)


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
    varList = []
    col =0
    for char in text:
        if char in strs:
            cLabelVar = StringVar()
            cLabelVar.set(char)
            cLabel = Label(parent, textvariable=cLabelVar,
                       font=font)
            varList.append(cLabelVar)
            cLabel.bind("<Button-1>", highlight)
            cLabel.grid(row=rowNum, column=col)


        else:
            cLabelVar = StringVar()
            cLabelVar.set(char)
            Label(parent, textvariable=cLabelVar,
                           font=font).grid(row=rowNum, column=col)
            varList.append(cLabelVar)

        col+=1

    return varList


def loadFromFile(fname):
    global cipherText
    global maxShift

    if os.path.isfile(fname):
        f = open(fname, "r")
        #reads first line of file as ciphertext
        cipherText = f.readline().rstrip()
        cipherText = cipherText.upper()

        numShifts = f.readline()
        try:
            int(numShifts)
        except ValueError:
            print "number of shifts not present. Exiting"
            exit(-1)
        maxShift = int(numShifts)
        f.close()
    else:
        print "no ciphertext file found"
        exit(-1)



if __name__ == '__main__':
    loadFromFile("cipherText.txt")

    #just used to setup the row.
    outputStr = ""
    for char in cipherText:
        outputStr += " "

    root = Tk()
    root.title("Shift Cipher Helper")
    root.resizable(width=False, height=False)
    mainFrame = Frame(root)

    mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))


    createLabels(mainFrame, -1 * maxShift, cipherText, 0, backwards=True)

    createRow(mainFrame, cipherText, maxShift + 1)

    #createLabels(mainFrame, maxShift, cipherText, maxShift + 2, backwards=False)

    sep = Separator(root, orient="horizontal")
    sep.grid(column= 1, row =(maxShift*2)+1, sticky="ws")

    outputVarList = createRow(mainFrame, outputStr, (maxShift*2)+2)


    #add all items to the grid layout in mainFrame
    # count = 0
    # for child in mainFrame.winfo_children():
    #     child.grid(column=0, row=count)
    #     count += 1

    root.mainloop()
