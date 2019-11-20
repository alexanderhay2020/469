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

# t, training_input, y, theta, v, w
training_input = np.random.randint(9,size=(10,6)) # data simulating 11 instances of 6-dim input
# training_input = np.loadtxt('10_input.tsv')

training_output= np.zeros([len(training_input),3])

for i in range(len(training_input)):
    """
    Motion Model
    """

    time = training_input[i,0]                # time
    v = training_input[i,4]                   # linear velocity
    w = training_input[i,5]                   # angular velocity

    theta = w*time                   			  # dtheta = w*t
    delta_training_input = (v*np.cos(theta)*time) # dtraining_input = vt*cos(theta)
    delta_y = (v*np.sin(theta)*time)              # dy = vt*sin(theta)

    training_output[i,0] = delta_training_input
    training_output[i,1] = delta_y
    training_output[i,2] = theta

# randomly initialize our weights with mean 0
w0 = 2*np.random.random((6,6)) - 1
w1 = 2*np.random.random((6,3)) - 1

print "Training Output: "
print training_output
print

print "Layer 1 Weights: "
print w0
print

print "Layer 2 Weights: "
print w1
print

for j in range(20000):

	# Feed forward through layers 0, 1, and 2
    l0 = training_input
    l1 = sigmoid(np.dot(l0,w0))
    l2 = sigmoid(np.dot(l1,w1))

    l2_error = training_output - l2

    l2_adjustment = l2_error*sigmoid_derivative(l2)

    l1_error = np.dot(l2_adjustment,w1.T)

    l1_adjustment = l1_error * sigmoid_derivative(l1)

    w1 += l1.T.dot(l2_adjustment)
    w0 += l0.T.dot(l1_adjustment)

print "Output: "
print l2
print

print "Layer 1 Weights: "
print w0
print

print "Layer 2 Weights: "
print w1
print
