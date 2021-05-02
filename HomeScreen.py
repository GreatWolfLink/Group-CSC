import tkinter as tk
import Plot as pl
import sys 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


Font = ("Times",40)
window = tk.Tk()
frame = tk.Frame(window)


class GUI():
    def __init__(self,frame,window):
        
        frame.pack(side="top", fill="both", expand=True)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        window.state('zoomed')
        window.resizable(0,0)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            LocalFrame = F(frame,self)

            self.frames[F] = LocalFrame

            LocalFrame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self,Page):

        frame = self.frames[Page]
        frame.tkraise()


    def Quit():
        window.destroy()


  

        
class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)

        label = tk.Label(self,text="Optimized Graphing Tool",font=Font)
        label.pack(pady=10,padx=10)


        button1 = tk.Button(self,text="Plot",fg="red",command=lambda: controller.show_frame(PageOne),padx=350,pady=100,font=Font)
        button1.pack()


        button2 = tk.Button(self,text="Insctructions",fg="green",command=lambda: controller.show_frame(PageTwo),padx=350,pady=100,font=("Times",20))
        button2.pack()

        
        button3 = tk.Button(self,text="Creators",fg="orange",command=lambda: controller.show_frame(PageThree),padx=350,pady=100,font=("Times",20))
        button3.pack()


        button4 = tk.Button(self,text="Exit",fg="blue",command=lambda: GUI.Quit(),padx=350,pady=100,font=("Times",20))
        button4.pack()

        

class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)

        label = tk.Label(self,text="Plot",font=Font)
        label.pack()

        button = tk.Button(self,text="back",fg="blue", command=lambda: controller.show_frame(StartPage),padx=100,pady=25)
        button.pack(side = tk.BOTTOM)

        parabolaButton = tk.Button(self, text="Parabola", fg="blue", command=lambda: parabola(),padx=100,pady=25)
        parabolaButton.pack()

        def parabola():
            f = Figure(figsize=(5, 5), dpi=100)
            x = np.arange(-100,100,1)
            y = x**2 + x**2 + 2
            axes = f.add_subplot(111)
            axes.plot(x, y)
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack()


class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)


        label = tk.Label(self,text="Instructions:",font=Font)
        label.pack()

        button = tk.Button(self,text="back",fg="blue", command=lambda: controller.show_frame(StartPage),padx=100,pady=25)
        button.pack(side = tk.BOTTOM)
   

class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)


        label = tk.Label(self,text="Creators:",font=Font)
        label.pack()

        label = tk.Label(self,text="Grant Gremillion \n Connor Broussard \n Ethan Joyce",fg="green",font=Font)
        label.pack()

        button = tk.Button(self,text="back",fg="blue",command=lambda: controller.show_frame(StartPage),padx=100,pady=25)
        button.pack(side = tk.BOTTOM)


Menu = GUI(frame,window)
window.mainloop()




