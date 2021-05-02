import tkinter as tk
import Plot as pl
import sys 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


Font = ("Bahnschrift SemiCondensed",80)
Font2 = ("Times",30)
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

        height =30
        width = 500
        ButtonHeight = 2
        FontColor = "blue"
        BackgroundImg = tk.PhotoImage(file="Background.gif")


        label = tk.Label(self,text="Optimized Graphing Tool",font=Font)
        label.pack(fill=tk.BOTH,pady=50)


      
        button1 = tk.Button(self,text="Plot",fg=FontColor,command=lambda: controller.show_frame(PageOne),font=Font2,height=ButtonHeight)
        button1.pack(fill=tk.BOTH,pady=height,padx=width)


        button2 = tk.Button(self,text="Instructions",fg=FontColor,command=lambda: controller.show_frame(PageTwo),font=Font2,height=ButtonHeight)
        button2.pack(fill=tk.BOTH,pady=height,padx=width)


        
        
        button3 = tk.Button(self,text="Creators",fg=FontColor,command=lambda: controller.show_frame(PageThree),font=Font2,height=ButtonHeight)
        button3.pack(fill=tk.BOTH,pady=height,padx=width)


        button4 = tk.Button(self,text="Exit",fg=FontColor,command=lambda: GUI.Quit(),font=Font2,height=ButtonHeight)
        button4.pack(fill=tk.BOTH,pady=height,padx=width)

        

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

        label = tk.Label(self,text="  ",fg="green",font=Font2)
        label.pack()

        button = tk.Button(self,text="back",fg="blue", command=lambda: controller.show_frame(StartPage),padx=100,pady=25)
        button.pack(side = tk.BOTTOM)
   

class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)


        label = tk.Label(self,text="Creators:",font=Font)
        label.pack()

        label = tk.Label(self,text="\n\n\nGrant Gremillion \n \n \nConnor Broussard \n \n \nEthan Joyce",fg="green",font=Font2)
        label.pack()

        button = tk.Button(self,text="back",fg="blue",command=lambda: controller.show_frame(StartPage),padx=100,pady=25)
        button.pack(side = tk.BOTTOM)


Menu = GUI(frame,window)
window.mainloop()




