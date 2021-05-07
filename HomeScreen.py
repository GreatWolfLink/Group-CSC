import tkinter as tk
import tkinter.simpledialog as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import random
from matplotlib.figure import Figure

Font = ("Bahnschrift SemiCondensed", 60)
Font2 = ("Times", 30)
window = tk.Tk()
frame = tk.Frame(window)
window.state('zoomed')
window.resizable(0, 0)
WindowWidth = window.winfo_screenwidth()
WindowHeight = window.winfo_screenheight()

ButtonSpacingWeight = .02
ButtonWidthWeight = .2

spacing = int(WindowHeight * ButtonSpacingWeight)
width = int(WindowWidth * ButtonWidthWeight)
height = 5

ButtonHeightWeight = 2
FontColor = "blue"


class GUI():
    def __init__(self, frame, window):
        
        frame.pack(side="top", fill="both", expand=True)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            LocalFrame = F(frame, self)

            self.frames[F] = LocalFrame

            LocalFrame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, Page):
        frame = self.frames[Page]
        frame.tkraise()

    def Quit():
        window.destroy()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Optimized Graphing Tool", font=Font)
        label.pack(fill=tk.BOTH, pady=10)

        button1 = tk.Button(self, text="Plot", fg=FontColor, command=lambda: controller.show_frame(PageOne), font=Font2,
                            height=ButtonHeightWeight)
        button1.pack(fill=tk.BOTH, pady=spacing, padx=width)

        button2 = tk.Button(self, text="Instructions", fg=FontColor, command=lambda: controller.show_frame(PageTwo),
                            font=Font2, height=ButtonHeightWeight)
        button2.pack(fill=tk.BOTH, pady=spacing, padx=width)

        button3 = tk.Button(self, text="Creators", fg=FontColor, command=lambda: controller.show_frame(PageThree),
                            font=Font2, height=ButtonHeightWeight)
        button3.pack(fill=tk.BOTH, pady=spacing, padx=width)

        button4 = tk.Button(self, text="Exit", fg=FontColor, command=lambda: GUI.Quit(), font=Font2,
                            height=ButtonHeightWeight)
        button4.pack(fill=tk.BOTH, pady=spacing, padx=width)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        width = 5
        self.can = None
        x = np.arange(-100, 100, 1)

        label = tk.Label(self, text="Plot", font=Font)
        label.grid(row=0,column=0,columnspan=15)
        
        for row in range(15):
            tk.Grid.rowconfigure(self,row,weight=1)
        for column in range(15):
            tk.Grid.columnconfigure(self,column,weight=1)


        ProblemText = tk.StringVar()
        ProblemText.set(" ")
        ProblemLabel = tk.Label(self, textvariable=ProblemText)
        GenerateProblemButton = tk.Button(self, text="Generate Problem",command=lambda: self.ChangeText(ProblemText))

        GenerateProblemButton.grid(row=0,column=12,columnspan=2)
        ProblemLabel.grid(row=1,column=12,columnspan=2)

        
        ParabolaButton = tk.Button(self, text="Quadratic", fg="blue",command=lambda: PageOne.ParabolaInput(self,canvas1),height=height,width=width)
        ParabolaButton.grid(row=1,column=0,sticky=tk.N+tk.W+tk.E)

        LinearButton = tk.Button(self, text="Linear", fg="blue",command=lambda: PageOne.LinearInput(self,canvas1),height=height,width=width)
        LinearButton.grid(row=1,column=1,sticky=tk.N+tk.W+tk.E)

        ############ shows blank graph
        canvas1 = tk.Canvas(self)
        canvas1.grid(row=5,column=7)
        fig = Figure(figsize=(5,5), dpi = 100)
        plot1 = fig.add_subplot(111)
        plot1.plot()
        plot1.grid()
        plot1.margins(1000,1000)
        canvas2 = FigureCanvasTkAgg(fig, master = canvas1)
        canvas2.draw
        canvas2.get_tk_widget().grid(row=5,column=7)
        #############

        button = tk.Button(self, text="Back", fg="blue",command=lambda: controller.show_frame(StartPage),height=height)
        button.grid(row=15,column=0,sticky=tk.N+tk.W+tk.E)




    # Graphs based on an x value and a y value
    # y value is the equation with whatever inputs are received entered in beforehand
    # destroys previous graph when it runs
    def graph(self, x, y):
        if self.can:
            self.can.destroy()
        f = plt.figure()
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
        self.can.grid(row=5,column=7)
        

    # Takes user input for the necessary integers and uses them in an equation
    def ParabolaInput(self,canvas1):
        x = np.arange(-100, 100, 1)
        a = sd.askfloat('User Input', "Input an A value")
        b = sd.askfloat('User Input', "Input a B value")
        c = sd.askfloat('User Input', "Input a C value")
        canvas1.destroy()
        y = (a * (x ** 2)) + (b * x) + c
        PageOne.graph(self, x, y)

    def LinearInput(self,canvas1):
        x = np.arange(-100, 100, 1)
        m = sd.askfloat('User Input', "Input a slope")
        b = sd.askfloat('User Input', "Input a y-intercept")
        canvas1.destroy()
        y = (m * x) + b
        PageOne.graph(self, x, y)


    def ChangeText(self,ProblemText):
        QuestionList = ["Graph the equation 4x^2 + 3x + 28 \n and compute the range and domain \n of the function.","q2","q3","q4","q5"]
        ProblemText.set(random.choice(QuestionList))

        


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Instructions:", font=Font)
        label.grid(row=0,column=0,columnspan=15)

        for row in range(15):
            tk.Grid.rowconfigure(self,row,weight=1)
        for column in range(15):
            tk.Grid.columnconfigure(self,column,weight=1)


        label = tk.Label(self, text=" \n 1. Generate a random problem \n\n 2. Select function button appropriate for question \n\n 3. Input parameters asked in question \n\n 4. Use visual to help solve problem ", fg="green", font=Font2)
        label.grid(row=4,column=7)

        button = tk.Button(self, text="back", fg="blue", command=lambda: controller.show_frame(StartPage),height = height)
        button.grid(row=15,column=0,sticky=tk.N+tk.W+tk.E)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Creators:", font=Font)
        label.grid(row=0,column=0,columnspan=15)

        for row in range(15):
            tk.Grid.rowconfigure(self,row,weight=1)
        for column in range(15):
            tk.Grid.columnconfigure(self,column,weight=1)

        label = tk.Label(self, text="\nGrant Gremillion \n \n \nConnor Broussard \n \n \nEthan Joyce", fg="green",font=Font2)
        label.grid(row=5,column=7)

        button = tk.Button(self, text="back", fg="blue", command=lambda: controller.show_frame(StartPage),height=height)
        button.grid(row=15,column=0,sticky=tk.N+tk.W+tk.E)


Menu = GUI(frame, window)
window.mainloop()
