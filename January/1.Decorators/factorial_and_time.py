import time
import math
print("To find factorial and calculate its time") 

def calculate_time(func):
    def inner1(*non_key_args, **key_args):
        begin = time.time()
        val=func(*non_key_args, **key_args)
        end = time.time()
        print("Total time taken in : ", func.__name__, "is ", end - begin)
        return val
 
    return inner1

@calculate_time
def factorial(val):
    val = math.factorial(val)
    return val
 
factorial(10)



