# Encapsulation
## Identifying Classes
In the first implementation, wanting to add more features naturally led to classes that encapsulate the concept of a boundary condition. 
What other concepts arise naturally from the information we want to get from the model?

The Model estimates an _Expectation_, 
there are probably other statistics that could be of interest
- We could therefore abstract the notion of a statistic by creating a statistics gatherer class
- There are different ways to terminate a Monte Carlo Simulation
  - terminate on time, 
  - on standard error,
  - or simply after a fixed number of paths. 
- We could abstract this by writing a terminator class.

There were many different issues with the method of random number generation. 
At the moment, the script relies on the base method `random` which we don't know much about. 
It would be beneficial then to have our own methods for random number generation. 
Another natural abstraction then is a random-number generator class.

Specifying the boundary value(s) of our boundary condition(s) _through_ the condition itself is fairly natural and easy. 
As long as the boundary condition is always applied at the end of the process, 
at time T, 
a class that contains the condition and its boundary level will be neater.

More generally, 
when we pass from one problem to another problem, 
from one Monte Carlo Simulation to another, 
it will be useful if all the information about that problem were stored in one place. 
A generic `Condition` class would know the type of boundary condition, 
the duration in time of the simulation, 
but wouldn't know anything about the other parameters,
the drift, 
the standard deviation, 
or the current level of the measured process. 
These pieces of information should be stored in a booking-keeping class for example.  

The point is that by choosing a real-world concept to encapsulate, 
it is easy to decide what to include or what not to include. 

## What do Classes Buy us?
Suppose that having identified all the classes, 
we implement them. 
What do we gain? 

The first gain is that the ideas that encapsulate natural concepts in Computational Science,
can be easily used in other pieces of code. 
For example, 
suppose we have a class that performs an optimization procedure, 
used time and time again.
Not only will we save time on writing code, 
we will save time on debugging, 
since a class that has been thoroughly tested once, 
has been tested forever. 
In addition, 
any quirks that evade the testing regime will be found through repeated reuse. 
The more times and ways something has been reused, 
the fewer bugs that are left. 

The second major gain is that the code becomes clearer. 
Having written the code in terms of natural concepts, 
another coder can identify those natural concepts, 
and pick up our code much more easily.

Finally, 
classes allow us to separate interface from implementation. 
All the user needs to know about a `Condition` class is its boundary value. 
The user doesn't need to know how that condition is programmed.
This has multiple advantages. 
The first is that the class can be reused without the programmer having to study its internal workings. 
The second advantage is that because the defining characteristic of the class is what it does but not how it does it, 
we can change how it does it at will. 
And crucially, 
we can do this without rewriting the rest of our program. 
One aspect of this is that we can first quickly write a suboptimal implementation and improve it later at no cost. 
This allows us to provide enough functionality to test the rest of the code before devoting a lot of time to the class.
A third advantage of separating interface from implementation is that we can write multiple classes that implement the same interface and use them without rewriting all the interface routines. 

## The Condition Class
Recall that we want to add another boundary condition to the simulation. 
The boundary condition is implemented on line 37

```python
# boundary condition
this_condition = max(this_level - boundary, 0)
```

of the file [simple_mc.py](../00%20First%20Implementation/simple_mc.py) in the first implementation of the Monte Carlo Simulation.

Adding another boundary condition might look like this 
- Copy the code and add "_another" to the end of the [simple_mc.py](simple_mc.py) function, 
- or pass an extra parameter and evaluate a series of if-else statements.

Instead, 
we've identified that a `Condition` class will be useful, 
that encapsulates the notion of a boundary condition. 
The file [condition.py](condition.py) contains the `Condition` class. 

```python
class Condition:

    def __init__(self, __boundary, __the_condition_type):

        # declare private attributes
        self.__the_condition_type = __the_condition_type
        self.__boundary = __boundary

    # the main method is public, we give it the boundary value,
    # it returns the simulated level at the boundary
    def condition(self, level):

        if self.__the_condition_type is ConditionType.lower:
            return max(level - self.__boundary, 0)
        elif self.__the_condition_type is ConditionType.upper:
            return max(self.__boundary - level, 0)
        else:
            print("unknown condition type")

```

### Privacy
We have declared the data in the class to be private. 
This means that the data cannot be accessed by code outside the class. 
The only code that can see, 
let alone change their values, 
are the constructor `__init__` and the method `condition`. 
Trying to access the boundary value from outside of the class will return the following exception

```python
print(lower_condition.boundary)

# Traceback (most recent call last):
#   File "...>
#     print(lower_condition.boundary)
# AttributeError: 'Condition' object has no attribute 'boundary'
```

What does this buy us? 
After all, 
for some reason the user might want to know the boundary value of a simulation, 
and we have denied them the possibility of finding out that value.

The reason is that as soon we let the user access the data directly, 
it is much harder for us to change how the class works. 
We can think of the class as a contract between coder and user. 
We, 
the coder, 
have provided the user with an interface:
_if he/she gives us a measured value we will tell her/him if that value has hit the boundary_. 
This is all we have contracted to provide. 
The user therefore expects and receives precisely that and no more.

For example, 
if the user could see the boundary value directly and access it, 
and if we changed the class so that the boundary value was no longer stored directly, 
then we would get compile errors from everywhere the boundary value was accessed. 

If the class had been used in many files, 
in many different projects (which is after all the objective of code reuse), 
to find every place where the boundary value had been accessed would be a daunting task. 
In fact, 
if this were the case we would probably consider finding them all a considerable waste of time, 
and we would probably give up reforming the internal workings. 

In other words, 
it means I can change whatever I want in the class that is private, 
without worry of breaking the rest of the code.

### Implementing The Condition Class
The main change from the original Monte Carlo routine is that the function [simple_mc.py](simple_mc.py) takes a condition object as an input instead of boundary value. 
The boundary value is of course now hidden inside the object. 

The only line of the algorithm that is new is 

```python
this_condition = the_condition(this_level)
```

The condition object needs to be initialized with a boundary value and condition type, 
and passed a measured level like a function.
Objects that appear more like a function than an object are often called function objects or functors. 

We illustrate how the routine might be called in [app.py](app.py). 

```python
# Create the lower and upper boundary condition objects
lower_condition = Condition(boundary, ConditionType.lower)
upper_condition = Condition(boundary, ConditionType.upper)

result_lower = simple_mc(lower_condition.condition,
                         time, level, vol, drift, n_paths)
result_upper = simple_mc(upper_condition.condition,
                         time, level, vol, drift, n_paths)
```

### Accessing Methods / Attributes in VSCode
In practice, 
the contract between code users is enforced through access to the methods and attributes of the class. 
Python uses dot-notation to access the attributes and methods of a class. 
VSCode's [Autocomplete and intelliSense](https://code.visualstudio.com/docs/languages/python) feature provides a list of the available attributes and methods.

![Class attributes and methods](../Images/02%20Encapsulation/method_lower.png)

An `enum` class is used to create a list of boundary condition types. 
Using the dot-notation, 
we see that only 2 types, upper and lower, are visible.

A boundary condition object is created given the boundary condition type, 
and level of the boundary. 
Using the dot-notation on the condition object, 
only the condition method is visible. 
The private methods are also visible but cannot be accessed. 
In Python, 
even private methods aren't truly private. 
This is discussed in detail in the Appendix.

![Object attributes and methods](../Images/02%20Encapsulation/method_upper.png)

We have thus partially achieved our goal. 
Both upper and lower boundary conditions are called without the need to change much code. 
Adding another condition requires updating the list of types, 
and adding the boundary condition code to the Condition class. 
The amount of code that needs to be changed is minimal, 
but we can still do better. 
At the next checkpoint we introduce polymorphism as a more robust approach to class-based switching.

## Open-Closed Principle
The previous section’s discussion leads naturally to a programming idea known as the open-closed principle. 
Open refers to the idea that code should always be open for extension. 
So in this particular case, 
we should always be able to add extra boundary conditions. 

Closed means that the file is _closed for modification_. 
This refers to the idea that we should be able to do the extension without modifying any existing
code, 
and we should be able to do so without even changing anything in any of the existing files. 
How can one possibly add new features without changing the `Condition` class? 
To illustrate the idea before presenting a class-based solution, 
consider how we might do this using functions or procedural techniques. 

Suppose instead of making the class contain an enum that defines the condition type, 
we instead use a method that points to a specific function. 
The constructor for the condition would then take in the boundary value and the name of the function. 

This code achieves a lot of our objectives. 
We can put the function we point to in a new file, 
so the existing file for the condition does not change each time we add a new boundary condition. 
This means that neither the condition nor the Monte Carlo file needs to be changed. 

However, what do we do when the structure of the boundary condition changes, 
for example, suppose we want an upper _and_ lower absorbing boundary. 
This boundary condition requires 2 boundary levels, 
but we only have one parameter slot in the function chooser. 

One solution would be to use an array to specify and store parameters. 
However, the code is now starting to lose the properties of clarity and elegance which were a large part of our original objectives.
Fortunately, classes were introduced to solve just this sort of problem.

## Key Points
We looked at one way of using a class to encapsulate the notion of a boundary condition. 
We then saw some of the advantages of using such a class. 
We also saw that the class had not achieved all of our requirements:
- Using a `Condition` class allows us to add extra forms of boundary-conditions without modifying our Monte Carlo routine.
- By overloading we can make an object look like a function.
- The open-closed principle says that code should be open for extension but closed for modification
- Private data helps us separate interface from implementation.