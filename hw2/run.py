import numpy as np

def sigmoid(x):
    """
    args: x - some number

    retrun: some value between 0 and 1 based on sigmoid function

    Activation Function:
    + Allows the neuron to react in a non-binary fashion (ie. not 0/1, true/false)
    + Somewhat computationally expensive
    + This is a parameter that can be changed to improve performance, though
      sigmoid function seems to be the most common
      + Sigmoid function is preferred because "the nonlinear properties of this
        function means that the rate of change is slower at the extremes and
        faster in the center.""
    """

    return 1/(1+np.exp(-x))


training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

training_outputs = np.array([[0],
                             [1],
                             [1],
                             [0]])

test_input = np.array([[1, 0, 0],
                       [1, 1, 0],
                       [0, 1, 0]])

# expected output [[1],
#                  [1],
#                  [0]]
# first index is from training video (https://www.youtube.com/watch?v=kft1AJ9WVDk)
# second and third is verification
# neuron should value first column and disregard second/third columns
# an input of 0/1 in the first column should output a 0/1

np.random.seed(1) # for troubleshooting, can reproduce
weights = np.random.random((3,1))

print "Starting Weights: "
print weights
print

for i in range(1):

    input = training_inputs

    output = sigmoid(np.dot(input,weights))

print "Output after sigmoid function: "
print output
print
