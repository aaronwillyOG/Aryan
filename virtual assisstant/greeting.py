import random as r
from datetime import *

def greet():
    list = ['yes','how can i help','hello','you called']
    return r.choice(list)



def gtt():
    time = datetime.now()
    hour = time.hour

    if hour < 12:
        g = 'good morning, how can i help.'
        return g
    
    elif hour < 18:
        g = 'good afternoon, how can i help.'
        return g
    
    else:
        g = 'good evening, how can i help.'
        return g

def mation():
    list = ['here is what i found', 'here you go', "is this what you're looking for?", ]

def rg():
    list = [greet,gtt]
    rf = r.choice(list)
    return(rf())

# print(rg())
