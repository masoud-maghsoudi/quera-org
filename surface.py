#This code written for solving https://quera.ir/problemset/33473/
from cmath import pi

def get_func(shape, args*):
    if shape == 'square':
        return pow(args[0],2)
    elif shape == 'circle':
        return pi*pow(args[0], 2)
    elif shape == 'rectangle':
        return args[0]*args[1]
    elif shape == 'triangle':
        return args[0]*args[1]/2