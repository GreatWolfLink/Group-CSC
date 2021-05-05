import tkinter as tk
import tkinter.simpledialog as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import random

Font = ("Bahnschrift SemiCondensed", 60)
Font2 = ("Times", 30)
window = tk.Tk()
frame = tk.Frame(window)
window.state('zoomed')
window.resizable(0, 0)
WindowWidth = window.winfo_screenwidth()
WindowHeight = window.winfo_screenheight()


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

        ButtonSpacingWeight = .02
        ButtonWidthWeight = .2

        spacing = int(WindowHeight * ButtonSpacingWeight)
        width = int(WindowWidth * ButtonWidthWeight)

        ButtonHeightWeight = 2
        FontColor = "blue"

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

        self.can = None
        x = np.arange(-100, 100, 1)
        label = tk.Label(self, text="Plot", font=Font)
        label.pack()

        ProblemText = tk.StringVar()
        ProblemText.set(" ")
        ProblemLabel = tk.Label(self, textvariable=ProblemText)
        GenerateProblemButton = tk.Button(self, text="Generate Problem",command=lambda: self.ChangeText(ProblemText))

        GenerateProblemButton.pack()
        ProblemLabel.pack()

        button = tk.Button(self, text="Back", fg="blue",
                           command=lambda: controller.show_frame(StartPage), padx=100, pady=25)
        button.pack(side=tk.BOTTOM)

        parabolaButton = tk.Button(self, text="Quadratic", fg="blue",
                                   command=lambda: PageOne.ParabolaInput(self), padx=100, pady=25)
        parabolaButton.pack()

        LinearButton = tk.Button(self, text="Linear", fg="blue",
                                 command=lambda: [PageOne.LinearInput(self)], padx=100, pady=25)
        LinearButton.pack()

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
        self.can.pack()
        

    # Takes user input for the necessary integers and uses them in an equation
    def ParabolaInput(self):
        x = np.arange(-100, 100, 1)
        a = sd.askfloat('User Input', "Input an A value")
        b = sd.askfloat('User Input', "Input a B value")
        c = sd.askfloat('User Input', "Input a C value")
        y = (a * (x ** 2)) + (b * x) + c
        PageOne.graph(self, x, y)

    def LinearInput(self):
        x = np.arange(-100, 100, 1)
        m = sd.askfloat('User Input', "Input a slope")
        b = sd.askfloat('User Input', "Input a y-intercept")
        y = (m * x) + b
        PageOne.graph(self, x, y)


    def ChangeText(self,ProblemText):
        QuestionList = ["Graph the equation 4x^2 + 3x + 28 and write the range and domain of the function.","q2","q3","q4","q5"]
        ProblemText.set(random.choice(QuestionList))

        


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Instructions:", font=Font)
        label.pack()

        label = tk.Label(self, text=" \n 1. Generate a random problem \n\n 2. Select function button appropriate for question \n\n 3. Input parameters asked in question \n\n 4. Use visual to help solve problem ", fg="green", font=Font2)
        label.pack()

        button = tk.Button(self, text="back", fg="blue", command=lambda: controller.show_frame(StartPage), padx=100,
                           pady=25)
        button.pack(side=tk.BOTTOM)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Creators:", font=Font)
        label.pack()

        label = tk.Label(self, text="\nGrant Gremillion \n \n \nConnor Broussard \n \n \nEthan Joyce", fg="green",
                         font=Font2)
        label.pack()

        button = tk.Button(self, text="back", fg="blue", command=lambda: controller.show_frame(StartPage), padx=100,
                           pady=25)
        button.pack(side=tk.BOTTOM)


Menu = GUI(frame, window)
window.mainloop()
