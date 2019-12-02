"""
Alexander Hay
HW2 - Machine Learning

Learning aim: Motion model
Learning algorithm: Neural Network
Dataset: DS0
 + Training Data:        (v, w) - odometry
                  (x, y, theta) - groundtruth

 + Test Data: (v, w) - odometry

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

def sigmoid_derivative(x):
    """
    args: x - some number

    return: derivative of sigmid given x
    """
    x_prime = x*(1-x)
    return x_prime


data = np.loadtxt('lwr_validation_input.tsv')

input = data[:,:2]
output = data [:,-2:]

actual_output = output
error = output

w0 = np.loadtxt('lwr_w0.tsv')
w1 = np.loadtxt('lwr_w1.tsv')

l0 = input
l1 = sigmoid(np.dot(l0,w0))
l2 = sigmoid(np.dot(l1,w1))

l2_error = output - l2

for i in range(len(l2)):
    error[i] = actual_output[i] - l2[i]

np.savetxt('lwr_validation_error.tsv', error)
print "lwr_validation_error.tsv saved"

np.savetxt('lwr_validation_predicted.tsv', l2)
print "lwr_validation_predicted.tsv saved"

np.savetxt('lwr_validation_output.tsv', l2)
print "lwr_validation_output.tsv saved"
