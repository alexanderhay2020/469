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

# global variables
np.random.seed(1) # for troubleshooting, can reproduce

class NeuralNet(object):
    """
    text
    """
    def __init__(self, training_input, training_output, iterations, layers):

        self.train(training_input, training_output, iterations, layers)

    def sigmoid(self,x):
        """
        args: x - some number

        return: some value between 0 and 1 based on sigmoid function

        Activation Function:
        + Allows the neuron to react in a non-binary fashion (ie. not 0/1, true/false)
        + Somewhat computationally expensive
        + This is a parameter that can be changed to improve performance, though
          sigmoid function seems to be the most common
          + Sigmoid function is preferred because "the nonlinear properties of this
            function means that the rate of change is slower at the extremes and
            faster in the center.""
        """

        return float(1/(1+np.exp(-x)))


    def sigmoid_derivative(self, x):
        """
        args: x - some number

        return: derivative of sigmoid at x

        Defines derivative
        """
        # x_prime = float(x*(1-x))
        return float(x*(1-x))

    def train(self, training_input, training_output, iterations, layers):
        """
        text
        """

        weights = np.random.random((training_input.shape[1],3)) # starting weight for each column (synapse)
        w0 = 2*np.random.random((training_input.shape[1],6)) - 1
        w1 = 2*np.random.random((w0.shape[0],3)) - 1

        print "w0: "
        print w0.shape
        print
        print "w1: "
        print w1.shape
        print
        for i in range(iterations):
            """
            neuron
            """
            l0 = training_input
            print "l0: "
            print l0.shape
            print

            print "dot product: "
            print np.dot(l0,w0).shape

            l1 = self.sigmoid(np.dot(l0,w0))
            l2 = self.sigmoid(np.dot(l1,w1))

            # print "layer shape: "
            # print l0.shape
            # print l1.shape
            # print l2.shape
            # print
            # input = test_input
            # xw = np.dot(l0,weights) # [4x3]*[3*1]=[4x1]
            # print "x*w: "
            # print xw
            # print
            # output = self.sigmoid(xw)

            l2_error = training_output - l2

            if (i% iterations) == 0:
                print "Error:" + str(np.mean(np.abs(l2_error)))

            l2_delta = l2_error*self.sigmoid_derivative(l2)

            l1_error = l2_delta.dot(w1.T)

            l1_delta = l1_error * self.sigmoid_derivative(l1)

            # print "delta shape: "
            # print l1_delta.shape
            # print l2_delta.shape
            # print
            # print
            w1 += w1 + np.dot(l1.T,l2_delta)
            w0 += w0 + np.dot(l0.T,l1_delta)

            # print "weights: "
            # print w0
            # print w1

            # error = training_output - output
            #
            # adjustments = error * self.sigmoid_derivative(output)
            #
            # weights = weights + np.dot(input.T,adjustments)

def main():
    """
    text
    """
    # training_input = np.loadtxt('training_input.tsv')
    input = np.random.randint(9,size=(11,6)) # data simulating 11 instances of 6-dim input

    # training_output = np.loadtxt('training_output.tsv')
    output = np.zeros([len(input),3])

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

    NeuralNet(input, output, 2000, 2)

if __name__ == '__main__':
    main()
# first index is from training video (https://www.youtube.com/watch?v=kft1AJ9WVDk)
# second and third is verification
# neuron should value first column and disregard second/third columns
# an input of 0/1 in the first column should output a 0/1

# np.random.seed(1) # for troubleshooting, can reproduce
# weights = np.random.random((len(test_input),1)) # starting weight for each column (synapse)
#
# print "Starting Weights: "
# print weights
# print
#
# for i in range(20000):
#     """
#     neuron
#     """
#     input = test_input
#     xw = np.dot(input,weights) # [4x3]*[3*1]=[4x1]
#     # print "x*w: "
#     # print xw
#     # print
#     output = sigmoid(xw)
#
#     error = test_output - output
#
#     adjustments = error * sigmoid_derivative(output)
#
#     weights = weights + np.dot(input.T,adjustments)
#
# print "Weights after training: "
# print weights
# print
#
# print "Output after sigmoid function: "
# print output
# print
