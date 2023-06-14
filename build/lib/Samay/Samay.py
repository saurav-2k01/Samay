# Importing requried Modules and packages
import time


# Samay is a Module to compare execution time of two functions.


# Creating class Samay
class samay:
    """
        Creating a Samay class constructor having following attributes.
        func = func is an attribute to parse a function.
        args = args is a tuple containing all parameters of the function that has been parsed.

    """

    def __init__(self, func, args=()):
        self._func = func
        self._args = args
        self._loop = 1  # _loop holds the number of loops to increase execution time of a function, _loop is equal to 1 by default.
        self._object_name = None  # _object_name is hold the Temporary name for the initialized objects.

    # Defining object_name as a property of a function.
    @property
    def object_name(self):
        return self._object_name

    # Setting object_name
    @object_name.setter
    def object_name(self, object=str):
        if object == None:
            return f'Objects are set to None'
        else:
            self._object_name = object

    # Defining Loop as a property.
    @property
    def loop(self):
        return self._loop

    # Setting loop as a property.
    @loop.setter
    def loop(self, loops):
        if loops == 1:
            return None
        else:
            self._loop = loops

    # Creating a  function that calculates the execution time of a function.
    def get_exe_time(self):
        if self._func != None:
            start = time.time()
            for i in range(self._loop):
                self._func(*self._args)
            end = time.time()
            return end - start
        else:
            return None

    # Creating a function that compares two different function.
    def compare_function(self, other):
        function_1 = self.get_exe_time()
        function_2 = other.get_exe_time()
        difference = function_1 - function_2

        """ 
            if object_name are not set, then it only returns the difference.
            else if Object_name are set, then it returns execution time of both 
            the functions as well as differnce between them. 

        """

        if self.object_name == None or other._object_name == None:
            return f'Difference  : {difference}'
        else:
            return {
                self._object_name: function_1,
                other._object_name: function_2,
                'Difference': difference
            }


