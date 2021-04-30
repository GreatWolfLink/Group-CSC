import tkinter as tk
import Plot as pl
import sys 



Font = ("Times",40)


class GUI(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)
        
        window = tk.Frame(self)
        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        self.state('zoomed')
        self.resizable(0,0)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(window,self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self,Page):

        frame = self.frames[Page]
        frame.tkraise()


  

        
class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)

        label = tk.Label(self,text="Optimized Graphing Tool",font=Font)
        label.pack(pady=10,padx=10)


        button1 = tk.Button(self,text="Plot",fg="red",command=lambda: controller.show_frame(PageOne),padx=350,pady=100)
        button1.pack()


        button2 = tk.Button(self,text="Insctructions",fg="green",command=lambda: controller.show_frame(PageTwo),padx=350,pady=100)
        button2.pack()

        
        button3 = tk.Button(self,text="Creators",fg="orange",command=lambda: controller.show_frame(PageThree),padx=350,pady=100)
        button3.pack()


        button4 = tk.Button(self,text="Exit",fg="pink",padx=350,pady=100)
        button4.pack()

        

class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)

        label = tk.Label(self,text="Plot",font=Font)
        label.pack()

        button = tk.Button(self,text="back",fg="blue", command=lambda: controller.show_frame(StartPage),padx=100,pady=25)
        button.pack(side = tk.BOTTOM)
    

class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)


        label = tk.Label(self,text="Instructions",font=Font)
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






Menu = GUI()
Menu.mainloop()




