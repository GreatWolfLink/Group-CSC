from tkinter import *
from matplotlib import *



#############################################################################

# main class
class Graph:

    # initiate every graph with origin of 0 by default
    def __init__(self,origin=(0,0)):
        self.origin = origin
        


    # getter and setter for origin
    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self,origin):
        self._origin = origin
        

  
#############################################################################



# Line and Circle classes inherit from Graph class
class Line(Graph):

    def __init__(self,origin,slope):
        self.slope = slope
        Graph.__init__(self,origin)


   
class Circle(Graph):

    def __init__(self,origin,radius):
        self.radius = radius
        Graph.__init__(self,origin)


################################################################################




def Main():

    PlotWindow = Tk()
    PlotWindow.geometry("500x500")

    


    Line = Button(PlotWindow,text="Line",pady=8)
    Line.pack(side=BOTTOM)


    Circle = Button(PlotWindow,text="Circle",pady=8)
    Circle.pack(side=BOTTOM)


    Parabola = Button(PlotWindow,text="Parabola",pady=8)
    Parabola.pack(side=BOTTOM)
 
 




    

    PlotWindow.mainloop()
    
    
    
