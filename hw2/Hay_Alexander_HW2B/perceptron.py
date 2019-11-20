"""
Based on video:
https://www.youtube.com/watch?v=kft1AJ9WVDk)

neuron should value first and second columns, and disregard third
"""

import numpy as np

np.random.seed(1) # for troubleshooting, can reproduce

def sigmoid(x):
    """
    args: x - some number
    return: some value between 0 and 1 based on sigmoid function
    """

    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    """
    args: x - some number
    return: derivative of sigmoid given x
    """
    x_prime = x*(1-x)
    return x_prime

training_input = np.array([[0, 0, 1],
                           [1, 1, 1],
                           [1, 0, 1],
                           [0, 1, 1]])

training_output = np.array([[0],
                            [1],
                            [1],
                            [1]])

weights = np.random.random((3,1)) # starting weight for each column (synapse)

print "Input: "
print training_input
print

print "Starting Weights: "
print weights
print

for i in range(20000):
    """
    neuron
    """
    input = training_input
    xw = np.dot(input,weights) # [4x3]*[3*1]=[4x1]

    output = sigmoid(xw)

    error = training_output - output

    adjustments = error * sigmoid_derivative(output)

    weights = weights + np.dot(input.T,adjustments)

print "Weights after training: "
print weights
print

print "Output: "
print output
print
