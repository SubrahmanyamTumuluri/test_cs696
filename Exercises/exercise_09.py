"""
Exercise 9
1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowledge of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math


def my_decorator(fn):
    def internal_time_wrapper(*args):
        t0 = time.time()
        tt0= time.process_time()
        result = fn(*args)
        size= sys.getsizeof(result)
        tt1= time.process_time()
        t1 = time.time()
        print("'{}' finished in {} seconds, process time :{}, size is {}".format(fn.__name__,t1-t0, tt0-tt1, size))
        return result
    return internal_time_wrapper

def for_loop():
    newlist = []
    for a in range(1000000):
        newlist.append(a)
for_loop()
my_decorator(for_loop)()


@my_decorator
def list_comp():
    return [x for x in range(1, 1000000)]
list_comp()
# print(list_comp.__name__)


def numpy_list():
   numpy.arange(1,1000000)
numpy_list()
my_decorator(numpy_list)()


def pandas_list():
    pandas.DataFrame(numpy.arange(1,1000000))
pandas_list()
my_decorator(pandas_list)()


def generator_list():
    return (x for x in range(1,1000000))
generator_list()
my_decorator(generator_list)()


def for_loop_log():
    New_list = []
    for i in range(1000000):
        if i != 0:
            New_list.append(math.log10(i))
for_loop_log()
my_decorator(for_loop_log)()

def list_comp_log():
    return [math.log(x) for x in range(1,1000000) if x!=0]
list_comp_log()
my_decorator(list_comp_log)()



def numpy_list_log():
    return [numpy.math.log(x) for x in range(1,1000000)]
numpy_list_log()
my_decorator(numpy_list_log)()




def pandas_list_log():
 return [pandas.DataFrame(numpy.log10(numpy.arange(1, 1000000)))]
pandas_list_log()
my_decorator(pandas_list_log)()




def generator_list_log():
    return (math.log(x) for x in range(1, 1000000) if x!=0)
generator_list_log()
my_decorator(generator_list_log)()

# @my_decorator
# def mon():
#     x = 100
#     y=100
#     return
# mon()


