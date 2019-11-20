"""
Alexander Hay
HW2 - Machine Learning

Learning aim: Motion model
Learning algorithm: Neural Network
Dataset: DS1
 + Training Data: (v, w) - odometry
                  (x, y, theta) - groundtruth

 + Test Data: (v, w) - odometry

Part A
1. build training set

2. code learning algorithm

"""

import numpy as np

# global variables
barcodes = np.loadtxt('ds1_Barcodes.dat')
groundtruth = np.loadtxt('ds1_Groundtruth.dat') # position data from motion capture (may be taken as known information for filtering)
landmark = np.loadtxt('ds1_Landmark_Groundtruth.dat')  # landmark data
measurement = np.loadtxt('ds1_Measurement.dat') # measurement data from robot
odometry = np.loadtxt('ds1_Odometry.dat') # time, forward v, angular v, measured from robot

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
input = np.loadtxt('input.tsv')
# input = np.random.randint(9,size=(11,3)) # data simulating 11 instances of 6-dim input

# x, y, theta
output = np.loadtxt('output.tsv')
# output = np.zeros([11,3]) # building output data

# output data is the difference between time steps
for i in range(len(input)):
    """
    Motion Model
    """

    time = input[i,0]       # time
    v = input[i,1]          # velocity
    theta = input[i,2]*time # dtheta = w*t

    delta_x = (v*np.cos(theta)*time) # dx = vt*cos(theta)
    delta_y = (v*np.sin(theta)*time) # dy = vt*sin(theta)
    delta_theta = theta              # dtheta

    output[i,0] = delta_x
    output[i,1] = delta_y
    output[i,2] = delta_theta

# first index is from training video (https://www.youtube.com/watch?v=kft1AJ9WVDk)
# second and third is verification
# neuron should value first column and disregard second/third columns
# an input of 0/1 in the first column should output a 0/1

weights = np.random.random((input.shape[1],3)) # starting weight for each column (synapse)

print "input: "
print input.shape
print


print "Starting Weights: "
print weights.shape
print weights
print

print "output "
print output.shape
print

# print "Input Shape: "
# print input.shape
# print

for i in range(2000):
    """
    neuron
    """
    # print "iteration: " + str(i)
    # print "training_intput shape" + str(input.shape)

    xw = np.dot(input,weights) # [4x3]*[3*1]=[4x1]
    # print "xw shape: " + str(xw.shape)
    # print xw.shape
    # print "x*w: "
    # print xw
    # print
    output = sigmoid(xw)
    # print "output: " + str(output.shape)

    error = output - output
    # print "error shape: " + str(error.shape)
    # print

    adjustments = error * sigmoid_derivative(output)

    weights = weights + np.dot(input.T,adjustments)

print "Weights after training: "
print weights.shape
print weights
print

print "Output after sigmoid function: "
print output
print

print "Training output: "
print output
print
