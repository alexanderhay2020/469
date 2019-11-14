"""
Alexander Hay
HW2 - Machine Learning

Learning aim: Motion model
Learning algorithm: Neural Network
Dataset: DS0
 + Training Data: (v, w) - odometry
                  (x, y, theta) - groundtruth

 + Test Data: (v, w) - odometry

Part A
1. build training set

2. code learning algorithm

"""

import numpy as np

def sigmoid(x):
    """
    args: x - some number

    return: some value between 0 and 1 based on sigmoid function
    """

    return 1/(1+np.exp(-x))


def sigmoid_derivative(x):
    """
    args: x - some number

    return: derivative of sigmid given x
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
                            [0]])

test_input = np.array([[1, 0, 0],
                       [1, 1, 0],
                       [0, 1, 0]])

test_output = np.array([[1],
                        [1],
                        [0]])
# first index is from training video (https://www.youtube.com/watch?v=kft1AJ9WVDk)
# second and third is verification
# neuron should value first column and disregard second/third columns
# an input of 0/1 in the first column should output a 0/1

np.random.seed(1) # for troubleshooting, can reproduce
weights = np.random.random((len(test_input),1)) # starting weight for each column (synapse)

print "Starting Weights: "
print weights
print

for i in range(20000):
    """
    neuron
    """
    input = test_input
    xw = np.dot(input,weights) # [4x3]*[3*1]=[4x1]
    # print "x*w: "
    # print xw
    # print
    output = sigmoid(xw)

    error = test_output - output

    adjustments = error * sigmoid_derivative(output)

    weights = weights + np.dot(input.T,adjustments)

print "Weights after training: "
print weights
print

print "Output after sigmoid function: "
print output
print
