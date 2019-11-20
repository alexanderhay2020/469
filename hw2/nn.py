import numpy as np

def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))

# t, training_input, y, theta, v, w
# training_input = np.random.randint(9,size=(10,6)) # data simulating 11 instances of 6-dim input
training_input = np.loadtxt('Hay_Alexander_HW2B/data/training_input.tsv')

# training_output= np.loadttraining_inputt('y.tsv')
training_output= np.zeros([len(training_input),3])

for i in range(len(training_input)):
    """
    Motion Model
    """

    time = training_input[i,0]                # time
    v = training_input[i,4]                   # linear velocity
    w = training_input[i,5]                   # angular velocity

    theta = w*time                   # dtheta = w*t
    delta_training_input = (v*np.cos(theta)*time) # dtraining_input = vt*cos(theta)
    delta_y = (v*np.sin(theta)*time) # dy = vt*sin(theta)

    training_output[i,0] = delta_training_input
    training_output[i,1] = delta_y
    training_output[i,2] = theta

print "training output: "
print training_output
print

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2*np.random.random((6,6)) - 1
syn1 = 2*np.random.random((6,3)) - 1

for j in xrange(10):

	# Feed forward through layers 0, 1, and 2
    l0 = training_input
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    # how much did we miss the target value?
    l2_error = training_output - l2

    if (j% 10000) == 0:
        print "Error:" + str(np.mean(np.abs(l2_error)))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*nonlin(l2,deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1,deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print "output: "
print l2
print
