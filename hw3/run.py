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
import matplotlib.pyplot as plt

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

# t, input, y, theta, v, w
# input = np.random.randint(9,size=(10,6)) # data simulating 11 instances of 6-dim input
input = np.loadtxt('input2.dat')

output= np.zeros([len(input),3])

# t_0 = 1288971842.041
t_0 = 1288971925.782

for i in range(len(input)):
    """
    Motion Model
    """

    duration = input[i,0]                # time
    v = input[i,1]                   # linear velocity
    w = input[i,2]                   # angular velocity

    theta = w*duration                   			  # dtheta = w*t
    delta_input = (v*np.cos(theta)*duration) # dinput = vt*cos(theta)
    delta_y = (v*np.sin(theta)*duration)              # dy = vt*sin(theta)

    output[i,0] = delta_input
    output[i,1] = delta_y
    output[i,2] = theta

actual_output = output
error = output

# randomly initialize our weights with mean 0
w0 = 2*np.random.random([3,6]) - 1
w1 = 2*np.random.random([6,3]) - 1

print "Training Output: "
print actual_output
print
#
# print "Layer 1 Weights: "
# print w0
# print
#
# print "Layer 2 Weights: "
# print w1
# print

for j in range(20000):

	# Feed forward through layers 0, 1, and 2
    l0 = input
    l1 = sigmoid(np.dot(l0,w0))
    l2 = sigmoid(np.dot(l1,w1))

    l2_error = output - l2

    l2_adjustment = l2_error*sigmoid_derivative(l2)

    l1_error = np.dot(l2_adjustment,w1.T)

    l1_adjustment = l1_error * sigmoid_derivative(l1)

    w1 += l1.T.dot(l2_adjustment)
    w0 += l0.T.dot(l1_adjustment)

fig1 = plt.figure()
plt.title("Layer 0 Weights")
# plt.xlabel()
xticks = ['t','v','w']

plt.ylabel("magnitude")
# plt.bar(w0,label="w0")
for i in range(len(w0)):
    # x=w0[i][0]
    plt.plot(w0[i],label="weight " + str(i))
    plt.xticks(w0[i],xticks)
plt.legend()

fig2 = plt.figure()
plt.title("Layer 1 Weights")
plt.xlabel("d_x, d_y, d_theta")
plt.ylabel("magnitude")
# p(lt.bar(xlabel,w1,label="w1")
for i in range(len(w1)):
    plt.plot(w1[i],label="weight " + str(i))
plt.legend()
plt.show()

print "Learned Output: "
print l2
print

# print "Layer 1 Weights: "
# print w0
# print
#
# print "Layer 2 Weights: "
# print w1[0]
# print

for i in range(len(l2)):
    error[i] = actual_output[i] - l2[i]

print error

fig3 = plt.figure()
# plt.title("Layer 1 Weights")
# plt.xlabel("d_x, d_y, d_theta")
# plt.ylabel("magnitude")
# p(lt.bar(xlabel,w1,label="w1")
# for i in range(len(w1)):
#     plt.plot(w1[i],label="weight " + str(i))
# plt.legend()
plt.plot(error)
plt.show()
