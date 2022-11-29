#This code written for solving https://quera.ir/problemset/33473/
from cmath import pi

def get_func(shape, *args):
    if shape == 'square':
        return pow(args[0],2)
    elif shape == 'circle':
        return pi*pow(args[0], 2)
    elif shape == 'rectangle':
        return args[0]*args[1]
    elif shape == 'triangle':
        return args[0]*args[1]/2

if __name__ == "__main__":
    ls = get_func(['square', 'circle', 'rectangle', 'triangle'])

    print(ls[0](1))
    print(ls[1](2))
    print(ls[2](2, 4))
    print(ls[3](4, 5))