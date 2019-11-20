import numpy as np

def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))

# t, x, y, theta, v, w
input = np.random.randint(9,size=(10,6)) # data simulating 11 instances of 6-dim input
# input = np.loadtxt('Hay_Alexander_HW2B/data/training_input.tsv')

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

print "Training Output: "
print output
print

np.random.seed(1)

# randomly initialize our weights with mean 0
w0 = 2*np.random.random((6,6)) - 1
w1 = 2*np.random.random((6,3)) - 1

print "Layer 1 Weights: "
print w0
print

print "Layer 2 Weights: "
print w1
print

for j in xrange(2000):

	# Feed forward through layers 0, 1, and 2
    l0 = input
    #
    # xw0 = np.dot(l0,w0)
    # xw1 = np.dot(l1,w1)
    #
    # o0 = sigmoid(xw0)
    # o1 = sigmoid(xw1)

    l1 = nonlin(np.dot(l0,w0))
    l2 = nonlin(np.dot(l1,w1))

    # how much did we miss the target value?
    l2_error = output - l2

    # if (j% 10000) == 0:
    #     print "Error:" + str(np.mean(np.abs(l2_error)))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*nonlin(l2,deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(w1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1,deriv=True)

    w1 += l1.T.dot(l2_delta)
    w0 += l0.T.dot(l1_delta)

print "Layer 1 Weights: "
print w0
print

print "Layer 2 Weights: "
print w1
print

print "Final Output: "
print l2
print
