

import random

def get():
    return random.randint(0,100)

def square(*args):
    print(args)
    a = args
    return a*a
 
if __name__ == '__main__':
    print(get())