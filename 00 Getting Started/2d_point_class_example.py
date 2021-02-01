# A class that models two-dimensional points.
# -----------------------------------------------------------------------------------------

# The Point class has public member data consisting of 2 variables,
# representing the x and y coordinates of a 2D point.
# When we create a Point object,
# we want to be able to supply the values for x and y.

class Point:  # use PascalCase for classes

    # In order to have the behavior Point(1,2) we use constructors.
    # Constructors are a special method that get called when a new Point object is created.

    def __init__(self, x, y):
        """
        __init__ is a magic method that gets executed when an instance of a class is created
        """
        self.x = x
        self.y = y

    def draw(self):
        """
        Draw is a function that belongs to the Point class, a method
        """
        print(f"Point ({self.x}, {self.y})")


# What is self?? Self is a reference to the current Point object,
# For example, when we call the Point object, Python will create the Point object in memory,
# and set self to reference that Point object

# Self is referencing that object, and that object has a bunch of attributes and methods,
# using the "dot" operator you can see the methods, __draw__, __class__, with little square
# symbols, and attributes, __doc__, __annotations__,...
# variables that hold data about that object.
point = Point(1, 2)

# point.x and point.y would be attributes that can be printed on the terminal,
# they tell us where the point is...
print(point.x)

# We can set the self.x value to the argument or set it to 0,
# and call those methods from within the object
point.draw()

# Notice, when calling the draw method, we didn't have to supply the "self" method;

# To summarise, a Class bundles data and methods into 1 unit.
# As a metaphor, think of a human, a human can have eye-color, weight etc.,
# as well as functions, like walk, talk, and eat
