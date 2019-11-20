import numpy as np

def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))

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

# t, x, y, theta, v, w
training_input = np.random.randint(9,size=(10,6)) # data simulating 11 instances of 6-dim input
# input = np.loadtxt('Hay_Alexander_HW2B/data/training_input.tsv')

# training_output = np.loadtxt('training_output.tsv')
training_output = np.zeros([len(training_input),3])

for i in range(len(training_input)):
    """
    Motion Model
    """

    time = training_input[i,0]                # time
    v = training_input[i,4]                   # linear velocity
    w = training_input[i,5]                   # angular velocity

    theta = w*time                   # dtheta = w*t
    delta_x = (v*np.cos(theta)*time) # dx = vt*cos(theta)
    delta_y = (v*np.sin(theta)*time) # dy = vt*sin(theta)

    training_output[i,0] = delta_x
    training_output[i,1] = delta_y
    training_output[i,2] = theta


np.random.seed(1)

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

for j in xrange(2000):

	# Feed forward through layers 0, 1, and 2
    l0 = training_input

    xw0 = np.dot(l0,w0)
    l1 = sigmoid(xw0)

    xw1 = np.dot(l1,w1)
    l2 = sigmoid(xw1)
    # l1 = nonlin(np.dot(l0,w0))
    # l2 = nonlin(np.dot(l1,w1))

    # how much did we miss the target value?
    print training_output.shape
    print l1.shape
    l1_error = training_output - l1

    # if (j% 10000) == 0:
    #     print "Error:" + str(np.mean(np.abs(l2_error)))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error*sigmoid_derivative(o1)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l0_error = l1_delta.dot(w1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l0_delta = l0_error * sigmoid_derivative(l0)

    w1 += l1.T.dot(l1_delta)
    w0 += l0.T.dot(l0_delta)

print "Layer 1 Weights: "
print w0
print

print "Layer 2 Weights: "
print w1
print

print "Final Output: "
print
print
