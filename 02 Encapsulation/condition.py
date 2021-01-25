from enum import Enum, auto


class ConditionType(Enum):
    """ 
    Enum class for listing the types of boundary conditions 

    """
    lower = auto()
    upper = auto()


class Condition:
    """ 
    [Boundary] Condition class for storing boundary-condition information

    """

    def __init__(self, __boundary, __the_condition_type):
        """ 
        The constructor for the Condition class. 

        Parameters:
            boundary (private): The level the boundary is set at.
            the_condition_type (private): the boundary condition, e.g., upper or lower

        """

        # declare private attributes
        self.__the_condition_type = __the_condition_type
        self.__boundary = __boundary

    # the main method is public, we give it the boundary value,
    # it returns the simulated level at the boundary
    def condition(self, level):
        """ 
        Given the condition type, switches boundary value method. 

        Parameters: 
            level: The current level of the measurement. 

        Returns: 
            The level given the boundary condition
        """
        if self.__the_condition_type is ConditionType.lower:
            return max(level - self.__boundary, 0)
        elif self.__the_condition_type is ConditionType.upper:
            return max(self.__boundary - level, 0)
        else:
            print("unknown condition type")
