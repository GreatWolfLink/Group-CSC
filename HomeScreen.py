
from tkinter import *
from Plot import *



window = Tk()

window.geometry("500x500")

Grid.rowconfigure(window,0)
Grid.columnconfigure(window,0,weight=1)

Grid.rowconfigure(window,1,weight=1)
Grid.rowconfigure(window,2,weight=1)



def PressingPlotButton():
    print("calling main function in Plot.py")
    

def PressingPracticeProblemsButton():
    print("Open practice problems")

def PressingOptionsButton():
    print("Open options menu")
    

label = Label(window,text="Optimized Graphing Tool")
button1 = Button(window,text="Plot",fg="red",command=PressingPlotButton)
button2 = Button(window,text="Practice Problems",fg="blue",command=PressingPracticeProblemsButton)
button3 = Button(window,text="Options",fg="green",command=PressingOptionsButton)




label.grid(row=0,column=0,sticky=N+S+E+W)
button1.grid(row=1,column=0,sticky=N+S+E+W)
button2.grid(row=2,column=0,sticky=N+S+E+W)
button3.grid(row=3,column=0,sticky=N+S+E+W)


window.mainloop()


