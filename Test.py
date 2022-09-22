import sys
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}' .format(who_to_greet)
    return greeting


print(greet('World'))
print(greet('Subin'))
