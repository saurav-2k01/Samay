import time
import matplotlib.pyplot as plt

class Samay:

    """
            Samay class is used to find the execution time of function and compare execution time of those function.
            func: func is an attribute to parse a function.
            function_name: function_name holds the Temporary name for the initialized objects.
            args: args is a tuple containing all parameters of the function that has been parsed.
            id: unique id is generated everytime for a new instance.
    """

    object_count = 0
    def __init__(self, func, function_name:str=None, args=()):
        Samay.object_count += 1
        self.id = Samay.object_count
        self.func = func
        self.function_name = function_name
        if self.function_name:
            pass
        else:
            self.function_name = f"function {self.id}"
        self.args = args


    def get_exe_time(self, loops:int=10):

        """
            loops holds the number of loops to increase execution time of a function,
            loops is equal to 1 by default.
        """

        if self.func != None:
            start = time.time()
            for i in range(loops):
                self.func(*self.args)
            end = time.time()
            return end - start
        else:
            return None

    # Creating a function that compares two different function.
    def compare_function(self, other):

        """
            compare_function is used to compare two different function by the difference between
            the execution time of those two function.
        """

        function_1 = self.get_exe_time()
        function_2 = other.get_exe_time()
        difference = function_1 - function_2

        if self.function_name == None or other.function_name == None:
            return f'Difference  : {difference}'
        else:
            return {
                self.function_name: function_1,
                other.function_name: function_2,
                'Difference': difference
            }


class Samay_Bulk:

    """ Samay_Bulk class is used to test and compare function in bulk at once.
        functions: functions parameters takes a list of tuples containg function, function_name and args
        example:
            data = [
                (func1, "function1", (x, y)),
                (func2, (x, y)),
                (func3,)
            ]
        result: result holds the execution time as output with their function
        example:
            {"function1":0.0, "function2":0.0, "function3":0.0 }
    """

    def __init__(self, functions:list=[]):
        self.functions = functions
        self.function_count = len(self.functions)
        self.result = {}


    def filter(self,data):
        types = [type(x) for x in data]
        if str in types and tuple in types:
            return str, tuple
        elif str in types:
            return str
        elif tuple in types:
            return tuple


    def test_bulk(self, loops:int=10):

        """ test_bulk function is used to find the exection time of function in bulk,
            more than 2 function could be tested, and the result is stored in dictionary called
            result.
            example:
                temp = Samay_Bulk(data)
                temp.test_bulk()
                result = temp.result
        """

        for function in self.functions:
            if self.filter(function) == (str, tuple):
                process = Samay(func=function[0], function_name=function[1], args=function[2])
                self.result[process.function_name] = process.get_exe_time(loops)
            elif self.filter(function) == tuple:
                process = Samay(func=function[0], args=function[1])
                self.result[process.function_name] = process.get_exe_time(loops)
            elif self.filter(function) == str:
                process = Samay(func=function[0], function_name=function[1])
                self.result[process.function_name] = process.get_exe_time(loops)
            else:
                process = Samay(func=function[0])
                self.result[process.function_name] = process.get_exe_time(loops)


    def bar_chart(self):
        """ bar_chart function is used to visualize the result for easy comparison. """
        plt.bar(self.result.keys(), self.result.values())
        plt.title("Bar Chart")
        plt.xlabel("Function")
        plt.ylabel("Time")
        plt.show()
