"""
Alexander Hay
HW2 - Machine Learning

Learning aim: Motion model
Learning algorithm: Neural Network
Dataset: DS1
 + Training Data: (t, v, w) - odometry
                  (x, y, theta) - groundtruth

 + Test Data: (t, v, w) - odometry

Part A
1. build training set

2. code learning algorithm

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

    return: derivative of sigmid given x
    """
    x_prime = x*(1-x)
    return x_prime

# t, v, w, x, y, dtheta
input = np.loadtxt('training_input.tsv')

output = np.zeros([len(input),3])
# x, y, theta
for i in range(len(input)):
    """
    Motion Model
    """

    time = input[i,0]                # time
    v = input[i,4]                   # linear velocity
    w = input[i,5]                   # angular velocity

    theta = w*time                   # dtheta = w*t
    delta_x = (v*np.cos(theta)*time) # dx = vt*cos(theta)
    delta_y = (v*np.sin(theta)*time) # dy = vt*sin(theta)

    output[i,0] = delta_x
    output[i,1] = delta_y
    output[i,2] = theta

weights = np.random.random([6,3]) # starting weight for each column (synapse)

print "Starting Weights: "
print weights
print

for i in range(2000):
    """
    neuron
    """
    xw = np.dot(input,weights) # [4x3]*[3*1]=[4x1]

    output = sigmoid(xw)

    error = output - output

    adjustments = error * sigmoid_derivative(output)

    weights = weights + np.dot(input.T,adjustments)

print "Weights after training: "
print weights
print
