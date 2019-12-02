"""
Alexander Hay
HW2 - Machine Learning

Learning aim: Motion model
Learning algorithm: Neural Network
Dataset: DS1
 + Training Data:        (v, w) - odometry

Part A
1. build training set

2. code learning algorithm

"""

import numpy as np

np.random.seed(1)

def sigmoid(x):
    """
    args: x - some number

    return: some value between 0 and 1 based on sigmoid function
    """

    return 1/(1+np.exp(-x))

input = np.loadtxt('validation_input.tsv')

output = np.loadtxt('validation_output.tsv')

actual_output = output
error = output

w0 = np.loadtxt('nn_w0.tsv')
w1 = np.loadtxt('nn_w1.tsv')


# Feed forward through layers 0, 1, and 2
l0 = input
l1 = sigmoid(np.dot(l0,w0))
output = sigmoid(np.dot(l1,w1))

error = actual_output - output

np.savetxt('nn_validation_predicted.tsv', output)
print "nn_validation_predicted.tsv saved"

np.savetxt('nn_validation_error.tsv', error)
print "nn_validation_error.tsv saved"
