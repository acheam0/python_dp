# Implementations of common functions across these privacy notebooks

from random import getrandbits, randint

import numpy as np


def create_neighbour(x, verbose=False):
    """ Creates a neighbouring dataset
    Inputs:
        x: original dataset
        verbose: print detail
    Output:
        neighbouring dataset to x with 1 random value added or removed
    """
    
    x2 = np.copy(x)
    np.random.default_rng().shuffle(x2)

    # Randomly chose whether to add or subtract a value
    if getrandbits(1):
        x2 = x2[1:]
        if verbose: print("Subtracting value")
    else:
        x2 = np.append(x2, randint(min(x), max(x)))
        if verbose: print("Adding value")

    return x2

def print_hline(length):
    """ Prints a horizontal line
    Inputs:
        length: length of the line in characters
        
    Output:
        Unicode horizontal line printed to console
    """
    
    print(u'\u2500' * length)
    
def get_epsilons(max_epsilon, epsilon_step):
    """ Create array of epsilon values to test using given parameters
    Inputs:
        max_epsilon: maximum epsilon value
        epsilon_step: step size between epsilons
        
    Output:
        Array of epsilon values to test
    """
    
    epsilon_div = 1 / epsilon_step
    return [i / epsilon_div for i in range(1, int(max_epsilon * epsilon_div))]
