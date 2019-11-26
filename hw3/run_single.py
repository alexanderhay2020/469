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
input = np.loadtxt('input.dat')
# input = np.random.randint(9,size=(10,6)) # data simulating 10 instances of 6-dim input

output = np.zeros([len(input),3])
# x, y, theta

t_0 = 1288971842.041

for i in range(len(input)):
    """
    Motion Model
    """

    time = input[i,0]                # time
    v = input[i,1]                   # linear velocity
    w = input[i,2]                   # angular velocity

    duration = time - t_0
    t_0 = time

    theta = w*duration                   			  # dtheta = w*t
    delta_input = (v*np.cos(theta)*duration) # dinput = vt*cos(theta)
    delta_y = (v*np.sin(theta)*duration)              # dy = vt*sin(theta)

    output[i,0] = delta_input
    output[i,1] = delta_y
    output[i,2] = theta

weights = np.random.random([3,3]) # starting weight for each column (synapse)

# print "Starting Weights: "
# print weights
# print

print "Training output: "
print output
print

for i in range(20000):
    """
    neuron
    """
    xw = np.dot(input,weights) # [4x3]*[3*1]=[4x1]

    output = sigmoid(xw)

    error = output - output

    adjustments = error * sigmoid_derivative(output)

    weights = weights + np.dot(input.T,adjustments)

# print "Weights after training: "
# print weights
# print

print "Learned output: "
print output
print
