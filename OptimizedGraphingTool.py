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



# testing

c = Circle((3,6),3)

l = Line((34,8),2)

print("circle origin = ",c.origin)

print("circle radius = ",c.radius)

print("slope of line = ",l.slope)




################################################################################