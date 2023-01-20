
import math 

def f(x):
    value = 0.99999999
    if math.sin(x[0]*x[1]) > value:
        return x
