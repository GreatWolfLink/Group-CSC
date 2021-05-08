#### number pad ####
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk


FGLabelColor = "navy"
BGLabelColor = "light blue"
FGButtonColor = "pink"
BGButtonColor = "navy"

class NumberPad():
    def __init__(self, numOfInputs, canvas,frame, page):
        self.window = tk.Tk()
        self.window.config(bg="light blue")
        self.window.resizable(0,0)
        self.window.title("Number Pad")
        xspace=10
        yspace=10

        self.page = page
        self.frame = frame

        self.canvas = canvas

        self.numOfInputs = numOfInputs
        self.currentInput = 0
        self.Inputs = []

        self.labelText = "   "
        
        for row in range(1,7):
            tk.Grid.rowconfigure(self.window,row,weight=1)

        for column in range(1,3):
            tk.Grid.columnconfigure(self.window,row,weight=1)

        self.labelHelp = tk.Label(self.window,fg=FGLabelColor,bg=BGLabelColor)
        self.labelHelp.grid(row=1,column=1,columnspan=3)
        self.labelHelp.config(text = "Enter Left Bound")

        self.label = tk.Label(self.window,text = self.labelText, relief = "solid")
        self.label.grid(row=2,column=1,columnspan=3)

        One = tk.Button(self.window,text="1",command=lambda:self.Input("1"),fg=FGButtonColor,bg=BGButtonColor).grid(row=3,column=1,padx=xspace,pady=yspace)
        Two = tk.Button(self.window,text="2",command=lambda:self.Input("2"),fg=FGButtonColor,bg=BGButtonColor).grid(row=3,column=2,padx=xspace,pady=yspace)
        Three = tk.Button(self.window,text="3",command=lambda:self.Input("3"),fg=FGButtonColor,bg=BGButtonColor).grid(row=3,column=3,padx=xspace,pady=yspace)
        Four = tk.Button(self.window,text="4",command=lambda:self.Input("4"),fg=FGButtonColor,bg=BGButtonColor).grid(row=4,column=1,padx=xspace,pady=yspace)
        Five = tk.Button(self.window,text="5",command=lambda:self.Input("5"),fg=FGButtonColor,bg=BGButtonColor).grid(row=4,column=2,padx=xspace,pady=yspace)
        Six = tk.Button(self.window,text="6",command=lambda:self.Input("6"),fg=FGButtonColor,bg=BGButtonColor).grid(row=4,column=3,padx=xspace,pady=yspace)
        Seven = tk.Button(self.window,text="7",command=lambda:self.Input("7"),fg=FGButtonColor,bg=BGButtonColor).grid(row=5,column=1,padx=xspace,pady=yspace)
        Eight = tk.Button(self.window,text="8",command=lambda:self.Input("8"),fg=FGButtonColor,bg=BGButtonColor).grid(row=5,column=2,padx=xspace,pady=yspace)
        Nine = tk.Button(self.window,text="9",command=lambda:self.Input("9"),fg=FGButtonColor,bg=BGButtonColor).grid(row=5,column=3,padx=xspace,pady=yspace)
        Zero = tk.Button(self.window,text="0",command=lambda:self.Input("0"),fg=FGButtonColor,bg=BGButtonColor).grid(row=6,column=1,padx=xspace,pady=yspace)
        Decimal = tk.Button(self.window,text=".",command=lambda:self.Input("."),fg=FGButtonColor,bg=BGButtonColor).grid(row=6,column=2,padx=xspace,pady=yspace)
        Negative = tk.Button(self.window,text="-",command=lambda:self.Input("-"),fg=FGButtonColor,bg=BGButtonColor).grid(row=6,column=3,padx=xspace,pady=yspace)
        Submit = tk.Button(self.window, text="Submit", command=lambda:self.SubmitButton(),fg=FGButtonColor,bg=BGButtonColor).grid(row=7,column=1,columnspan=1)
        Submit = tk.Button(self.window, text="Delete", command=lambda:self.DeleteButton(),fg=FGButtonColor,bg=BGButtonColor).grid(row=7,column=3,columnspan=1)

    def DeleteButton(self):
        if self.labelText == "":
            return

        self.labelText = self.labelText[0 : len(self.labelText) - 1 : ] + self.labelText[len(self.labelText) : :]
        self.label.config(text = self.labelText)
        

    def SubmitButton(self):
        if self.labelText == "":
            return
        elif self.labelText == "   ":
            return

        currentValue = int(self.labelText)
        self.Inputs.append(currentValue)
        self.labelText = ""
        self.label.config(text = "")

        self.currentInput += 1

        print(self.Inputs)

        if self.currentInput == 1:
            self.labelHelp.config(text = "Enter Right Bound")
        else:
            if self.numOfInputs == 4:
                if(self.currentInput == 2):
                    self.labelHelp.config(text = "Enter the m: y = mx + b")
                elif(self.currentInput == 3):
                    self.labelHelp.config(text = "Enter the b: y = mx + b")
            elif self.numOfInputs == 5:
                if self.currentInput == 2:
                    self.labelHelp.config(text = "Enter the a: y = ax^2 + bx + c")
                elif self.currentInput == 3:
                    self.labelHelp.config(text = "Enter the b: y = ax^2 + bx + c")
                elif self.currentInput == 4:
                    self.labelHelp.config(text = "Enter the c: y = ax^2 + bx + c")
            elif self.numOfInputs == 6:
                if self.currentInput == 2:
                    self.labelHelp.config(text = "Enter the a: y = ax^3 + bx^2 + cx + d")
                elif self.currentInput == 3:
                    self.labelHelp.config(text = "Enter the b: y = ax^3 + bx^2 + cx + d")
                elif self.currentInput == 4:
                    self.labelHelp.config(text = "Enter the c: y = ax^3 + bx^2 + cx + d")
                elif self.currentInput == 5:
                    self.labelHelp.config(text = "Enter the d: y = ax^3 + bx^2 + cx + d")

        if self.currentInput >= self.numOfInputs:
            self.window.destroy()

            self.canvas.destroy()      

            LeftBound = self.Inputs[0]
            RightBound = self.Inputs[1]

            x = np.arange(LeftBound, RightBound, 1)

            if self.numOfInputs == 4:
                m = self.Inputs[2]
                b = self.Inputs[3]
                y = (m * x) + b
            elif self.numOfInputs == 5:
                a = self.Inputs[2]
                b = self.Inputs[3]
                c = self.Inputs[4]
                y = (a * (x ** 2)) + (b * x) + c
            elif self.numOfInputs == 6:
                a = self.Inputs[2]
                b = self.Inputs[3]
                c = self.Inputs[4]
                d = self.Inputs[5]
                y = ((a * (x ** 3)) + (b * x ** 2) + (c * x) + d)
            
            self.page.graph(self.frame, x, y)

    def Input(self, number):
        if self.labelText == "   ":
            self.labelText = ""
        self.labelText = self.labelText + str(number)
        self.label.config(text = self.labelText)



    
