import tkinter as tk
import Plot as pl



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

        for F in (StartPage, PageOne, PageTwo):

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

        label = tk.Label(self,text="Optimized Graphing Tool")
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self,text="Plot",fg="red",command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = tk.Button(self,text="Options",fg="green",command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        

class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)

        label = tk.Label(self,text="Plot")
        label.pack()

        button = tk.Button(self,text="back",fg="blue", command=lambda: controller.show_frame(StartPage))
        button.pack()
    


class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame. __init__(self,parent)


        label = tk.Label(self,text="Options")
        label.pack()

        button = tk.Button(self,text="back",fg="blue", command=lambda: controller.show_frame(StartPage))
        button.pack()
   




Menu = GUI()
Menu.mainloop()




