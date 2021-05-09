import tkinter as tk
import tkinter.simpledialog as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import random
from matplotlib.figure import Figure
from PIL import ImageTk, Image
import NumbPad as NP
import sys



#NOTE::This is the path to the background sprite
backgroundSpritePath = "Background.jpg"

Font = ("Bahnschrift SemiCondensed", 30)
Font2 = ("Times", 30)
Font3 = ("Times", 15)


FGLabelColor = "navy"
BGLabelColor = "orchid1"
FGButtonColor = "pink"
BGButtonColor = "navy"
BorderSize = 2
BorderType = "solid"


window = tk.Tk()
window.title("Graphing Tool")
frame = tk.Frame(window)
#window.attributes('-zoomed',True)

WindowWidth = window.winfo_screenwidth()
WindowHeight = window.winfo_screenheight()

ButtonSpacingWeight = .02
ButtonWidthWeight = .2

spacing = int(WindowHeight * ButtonSpacingWeight)
#width = int(WindowWidth * ButtonWidthWeight)
height = 5

ButtonHeightWeight = 2
FontColor = "blue"

class GUI():
    def __init__(self, frame, window):
        
        frame.pack(side="top", fill="both", expand=True)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        #NOTE::have to update window before grabbing width and height
        window.update()
        ScreenWidth = window.winfo_width()
        ScreenHeight = window.winfo_height()

        #NOTE::Adding background image
        self.img = ImageTk.PhotoImage(Image.open(backgroundSpritePath).resize((ScreenWidth, ScreenHeight)))
        self.background_label = tk.Label(window, image=self.img)
        self.background_label.image = self.background_label

        self.background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            LocalFrame = F(frame, self)

            self.frames[F] = LocalFrame

            LocalFrame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        self.background_label.destroy()

    def show_frame(self, Page):
        frame = self.frames[Page]
        frame.tkraise()

    def Quit():
        window.destroy()
        sys.exit(0)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Width = 15

        #NOTE::have to update window before grabbing width and height
        window.update()
        ScreenWidth = window.winfo_width()
        ScreenHeight = window.winfo_height()

        #NOTE::Adding background image
        self.img = ImageTk.PhotoImage(Image.open(backgroundSpritePath).resize((ScreenWidth, ScreenHeight)))
        self.background_label = tk.Label(self, image=self.img)
        self.background_label.image = self.background_label

        self.background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        
        label = tk.Label(self, text="Optimized Graphing Tool",relief=BorderType,borderwidth=BorderSize,fg=FGLabelColor,bg=BGLabelColor, font=Font)
        label.grid(row=0,column=0,columnspan=15)

        for row in range(15):
            tk.Grid.rowconfigure(self,row,weight=1)
        for column in range(15):
            tk.Grid.columnconfigure(self,column,weight=1)

        button1 = tk.Button(self, text="Plot", fg=FGButtonColor,bg=BGButtonColor, command=lambda: controller.show_frame(PageOne), font=Font2, height=ButtonHeightWeight,width=Width)
        button1.grid(row=4,column=6,sticky=tk.N+tk.S+tk.E+tk.W)

        button2 = tk.Button(self, text="Instructions", fg=FGButtonColor,bg=BGButtonColor, command=lambda: controller.show_frame(PageTwo), font=Font2, height=ButtonHeightWeight,width=Width)
        button2.grid(row=4,column=8,sticky=tk.N+tk.S+tk.E+tk.W)

        button3 = tk.Button(self, text="Creators", fg=FGButtonColor,bg=BGButtonColor, command=lambda: controller.show_frame(PageThree), font=Font2, height=ButtonHeightWeight,width=Width)
        button3.grid(row=6,column=6,sticky=tk.N+tk.S+tk.E+tk.W)

        button4 = tk.Button(self, text="Exit", fg=FGButtonColor,bg=BGButtonColor, command=lambda: GUI.Quit(), font=Font2,height=ButtonHeightWeight,width=Width)
        button4.grid(row=6,column=8,sticky=tk.N+tk.S+tk.E+tk.W)


class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.CurrentProblem = 0

        width = 5
        self.can = None
        x = np.arange(-100, 100, 1)

        #NOTE::have to update window before grabbing width and height
        window.update()
        ScreenWidth = window.winfo_width()
        ScreenHeight = window.winfo_height()

        #NOTE::Adding background image
        self.img = ImageTk.PhotoImage(Image.open(backgroundSpritePath).resize((ScreenWidth, ScreenHeight)))
        self.background_label = tk.Label(self, image=self.img)
        self.background_label.image = self.background_label

        self.background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        label = tk.Label(self, text="Plot",fg=FGLabelColor,bg=BGLabelColor,relief=BorderType,borderwidth=BorderSize, font=Font)
        label.grid(row=0,column=0,columnspan=15)
        
        for row in range(15):
            tk.Grid.rowconfigure(self,row,weight=1)
        for column in range(15):
            tk.Grid.columnconfigure(self,column,weight=1)


        ProblemText = tk.StringVar()
        ProblemText.set("Problems will appear here")
        ProblemLabel = tk.Label(self, textvariable=ProblemText,fg=FGLabelColor,bg=BGLabelColor,relief=BorderType,borderwidth=BorderSize)
        GenerateProblemButton = tk.Button(self, text="Generate Problem",command=lambda: self.ChangeText(ProblemText),fg=FGButtonColor,bg=BGButtonColor,font=Font3)

        GenerateProblemButton.grid(row=0,column=12,columnspan=2)
        ProblemLabel.grid(row=1,column=12,columnspan=2)

        
        ParabolaButton = tk.Button(self, text="Quadratic", fg=FGButtonColor,bg=BGButtonColor,command=lambda: PageOne.ParabolaInput(self,canvas1),height=height,width=width)
        ParabolaButton.grid(row=1,column=0,sticky=tk.N+tk.W+tk.E)

        LinearButton = tk.Button(self, text="Linear", fg=FGButtonColor,bg=BGButtonColor,command=lambda: PageOne.LinearInput(self,canvas1),height=height,width=width)
        LinearButton.grid(row=1,column=1,sticky=tk.N+tk.W+tk.E)


        CubicButton = tk.Button(self, text="Cubic", fg=FGButtonColor,bg=BGButtonColor, command=lambda: PageOne.CubicInput(self,canvas1),height=height,width=width)
        CubicButton.grid(row=1,column=2,sticky=tk.N+tk.W+tk.E)

    

        ############ shows blank graph
        canvas1 = tk.Canvas(self)
        canvas1.grid(row=1,column=4,rowspan=3,columnspan=3)
        fig = Figure(figsize=(3,3), dpi = 100)
        plot1 = fig.add_subplot(111)
        plot1.plot()
        plot1.grid()
        plot1.margins(1000,1000)
        canvas2 = FigureCanvasTkAgg(fig, master = canvas1)
        canvas2.draw
        canvas2.get_tk_widget().grid()
        #############

        button = tk.Button(self, text="Back", fg=FGButtonColor,bg=BGButtonColor,command=lambda: controller.show_frame(StartPage),height=height)
        button.grid(row=10,column=0,rowspan=8,sticky=tk.N+tk.W+tk.E)

        
    # Graphs based on an x value and a y value
    # y value is the equation with whatever inputs are received entered in beforehand
    # destroys previous graph when it runs
    def graph(self, x, y):
        if self.can:
            self.can.destroy()
        f = plt.figure(figsize=(3,3))
        canvas = FigureCanvasTkAgg(f, self)
        axes = f.add_subplot(111)
        axes.plot(x, y)

        # Sets the origin to be clearly displayed
        axes.spines['left'].set_position('zero')
        axes.spines['right'].set_color('none')
        axes.spines['bottom'].set_position('zero')
        axes.spines['top'].set_color('none')
        axes.xaxis.set_ticks_position('bottom')
        axes.yaxis.set_ticks_position('left')
        axes.grid()
       
        self.can = canvas.get_tk_widget()
        self.can.grid(row=1,column=4,rowspan=3,columnspan=3)

##        ValuesLabel = tk.Label(self, text="x and y values")
##        ValuesLabel.grid(row=10,column=12)
##    

##        List = tk.Listbox(self)
##        j = 1
##        for i in x:
##            List.insert(j,i)
##            j+=1
##        List.grid(row=11,column=12)
##
##        ScrollBar = tk.Scrollbar(self,command=List.yview)
##        ScrollBar.grid(row=13,column=13)
##

        

        

        
        

    # Takes user input for the necessary integers and uses them in an equation
    def ParabolaInput(self,canvas1):
        InputPad = NP.NumberPad(5, canvas1, self, PageOne)

    def LinearInput(self,canvas1):
        InputPad = NP.NumberPad(4, canvas1, self, PageOne)

    def CubicInput(self,canvas1):
        InputPad = NP.NumberPad(6, canvas1, self, PageOne)
    
    def ChangeText(self,ProblemText):

        

        QuestionList = ["Graph a cubic \nequation with a B \nvalue of 34",
                        "Graph a linear \nfunction with a \nslope of 4.6 and y \nintercept of 8",
                        "Graph a cubic \nfunction with a\n y intercept \nof 3",
                        "Graph a quadratic \nfunction with an A \nvalue of -3",
                        "Graph a linear \nfunction with a \nslope of 0 and y \nintercept of 3"]

        ProblemText.set(QuestionList[self.CurrentProblem])
        
        self.CurrentProblem +=1

        if self.CurrentProblem > 4:
            self.CurrentProblem = 0

        
        

        


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #NOTE::have to update window before grabbing width and height
        window.update()
        ScreenWidth = window.winfo_width()
        ScreenHeight = window.winfo_height()

        #NOTE::Adding background image
        self.img = ImageTk.PhotoImage(Image.open(backgroundSpritePath).resize((ScreenWidth, ScreenHeight)))
        self.background_label = tk.Label(self, image=self.img)
        self.background_label.image = self.background_label

        self.background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        label = tk.Label(self, text="Instructions",fg=FGLabelColor,bg=BGLabelColor,relief=BorderType,borderwidth=BorderSize, font=Font)
        label.grid(row=0,column=0,columnspan=15)

        for row in range(15):
            tk.Grid.rowconfigure(self,row,weight=1)
        for column in range(15):
            tk.Grid.columnconfigure(self,column,weight=1)


        label = tk.Label(self, relief=BorderType,borderwidth=BorderSize,text=" \n 1. Generate a random problem \n\n 2. Select function button appropriate for question \n\n 3. Input parameters asked in question \n\n 4. Use visual to help solve problem ",fg=FGLabelColor,bg=BGLabelColor, font=Font3)
        label.grid(row=4,column=0,columnspan=15)

        button = tk.Button(self, text="back",fg=FGButtonColor,bg=BGButtonColor, command=lambda: controller.show_frame(StartPage),height = height)
        button.grid(row=15,column=0,sticky=tk.N+tk.W+tk.E)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #NOTE::have to update window before grabbing width and height
        window.update()
        ScreenWidth = window.winfo_width()
        ScreenHeight = window.winfo_height()

        #NOTE::Adding background image
        self.img = ImageTk.PhotoImage(Image.open(backgroundSpritePath).resize((ScreenWidth, ScreenHeight)))
        self.background_label = tk.Label(self, image=self.img)
        self.background_label.image = self.background_label

        self.background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        label = tk.Label(self, text="Creators",fg=FGLabelColor,bg=BGLabelColor,relief=BorderType,borderwidth=BorderSize, font=Font)
        label.grid(row=0,column=0,columnspan=15)

        for row in range(15):
            tk.Grid.rowconfigure(self,row,weight=1)
        for column in range(15):
            tk.Grid.columnconfigure(self,column,weight=1)

        label = tk.Label(self, text="\n----Grant Gremillion----\n\n\n----Connor Broussard----\n\n\n----Ethan Joyce----",fg=FGLabelColor,bg=BGLabelColor,font=Font3,relief=BorderType,borderwidth=BorderSize)
        label.grid(row=5,column=0,columnspan=15)

        button = tk.Button(self, text="back",fg=FGButtonColor,bg=BGButtonColor, command=lambda: controller.show_frame(StartPage),height=height)
        button.grid(row=15,column=0,sticky=tk.N+tk.W+tk.E)


Menu = GUI(frame, window)
window.mainloop()
