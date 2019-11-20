# Alexander Hay
# ME_469, HW0, Part A2
# Dataset 1, Particle Filter
# Motion Model

import numpy as np

# timestamp, velocity, angular velocity
odo = np.random.randint(9,size=(11,3)) # data simulating 11 instances of 6-dim input

# array of x, y, theta values
xytheta=np.random.randint(9,size=(11,3))


# t, x, y, theta, v, w
training_input = np.random.randint(9,size=(11,6))

# dx, dy, dtheta
training_output = np.zeros([11,3])

for i in range(len(training_input)):

    time = training_input[i,0] # delta t is always 1 second
    v = training_input[i,4] # velocity data
    theta = training_input[i,5]*time

    training_output[i,0] = (v*np.cos(theta)*time)
    training_output[i,1] = (v*np.sin(theta)*time)
    training_output[i,2] = theta

print training_output
