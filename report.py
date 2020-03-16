from random import choice
"""Return random weather, just like the pros"""

def get_description():
    posibilities = ['rain','snow','sleet','fog','sun','who knows']
    return choice(posibilities)

