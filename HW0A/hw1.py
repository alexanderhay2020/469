# Alexander Hay
# ME_469, HW0, Part A2
# Dataset 1, Particle Filter

# import necessities
import numpy as np
import pylab as p
import math

# global variables
barcodes = np.loadtxt('ds1_Barcodes.dat')
groundtruth = np.loadtxt('ds1_Groundtruth.dat') # position data from motion capture (may be taken as known information for filtering)
landmark = np.loadtxt('ds1_Landmark_Groundtruth.dat')  # landmark data
measurement = np.loadtxt('ds1_Measurement.dat') # measurement data from robot
odometry = np.loadtxt('ds1_Odometry.dat') # time, forward v, angular v, measured from robot

# since the datasets for the assignments have been truncated and don't start at time t0, it needed to be 'calibrated'
# if we assumed t0=0 and that the frequency of sampling is even, the time steps of t0-t1 nad t1-t2 would be significantly different
# so all initial values given are gathered from the complete dataset, using the index of where our datasets start minus one.
# the origin is assumed to be known, again used the previous time frame's location data
t = 1288971842.041
initial_theta = 1.44849633
initial_x = 0.98038490
initial_y = -4.99232180
mu = [initial_theta, initial_x, initial_y] # initializes mu for particle generation

xt = np.zeros([1,3])
xt2 = np.zeros([1,3])
xt[0,0] = initial_theta
xt[0,1] = initial_x
xt[0,2] = initial_y

# -------------- motion model--------------------
# --------- part 2 of the homework---------------


def pt2():

    # timestamp, velocity, angular velocity
    odo = [(0, 0.5, 0),
           (1, 0, (-1 / (2 * math.pi))),
           (2, 0.5, 0),
           (3, 0, (1 / (2 * math.pi))),
           (4, 0.5, 0)]

    odo = np.array(odo)

    # array of x, y, theta values
    xytheta = np.zeros((len(odo), 3))

    for i in range(len(odo)):
        time = 1  # delta t is always 1 second
        vel = odo[i, 1]  # velocity data

        # calculates theta value and adds to previous value
        xytheta[i, 2] = (odo[i, 2] * time) + xytheta[i - 1, 2]
        # calculates x and adds to previous value
        xytheta[i, 0] = xytheta[i - 1, 0] + \
            (vel * np.cos(xytheta[i, 2]) * time)
        # calculates y and adds to previous value
        xytheta[i, 1] = xytheta[i - 1, 1] + \
            (vel * np.sin(xytheta[i, 2]) * time)

    xytheta[0, 0] = 0
    xytheta[0, 1] = 0
    # this reset origin values since they were overwritten
    # This is not the ideal solution, but it works and displays the line correctly

    # A E S T H E T I C
    p.title("Position over Time")
    p.xlabel("x position (m)")
    p.ylabel("y position (m)")
    p.xlim(-0.25, 1.75)
    p.plot(xytheta[:, 0], xytheta[:, 1])

    p.show()

# ------------ applied motion model--------------
# ----------- part 3 of the homework-------------


def pt3():

    # def odo():
    #
    #     # 2D array to hold calculated state x, y, and theta values
    #     xt = np.zeros((len(odometry), 3))
    #
    #     xt[0, 0] = initial_x
    #     xt[0, 1] = initial_y
    #     xt[0, 2] = initial_theta
    #
    #     for i in range(1, len(odometry)-1):
    #
    #         # ************************************
    #         # This section calculates robot's position
    #         # from odometry data
    #
    #         # executes command from timestamp until next command is issued
    #         time = odometry[i + 1, 0]-odometry[i, 0]
    #         vel = odometry[i, 1]
    #         xt[i, 2] = xt[i-1, 2]+(odometry[i, 2]*time)  # theta value in rad
    #         xt[i, 0] = xt[i - 1, 0]+vel*np.cos(xt[i, 2])*time # finds x displacement (m) x=v*cos(theta)*t
    #         xt[i, 1] = xt[i - 1, 1]+vel*np.sin(xt[i, 2])*time # finds y displacement (m) x=v*sin(theta)*t
    #
    #     return [xt]

    def particles(mu,m): # asks for mu [list of means], m (number of particles); returns mx3 array [theta, x, y] of randomly distributed numbers

        # creates  random points of data around the mean and std dev
        # for this exercise, mu is the state at t0, sigma is 1 but is tunable
        # m was set to 1000, but decided to make it variable in case resampling needs to occur

        # sig is defined
        # an mx3 array is created with random numbers for theta, x, y  *
        # fill each column with a random distribution with a given mu and sigma
        #
        # returns [mx3] particle array
        #
        # * I want to see if I can change the way random numbers generated, by using a gaussian distribution

        sig = 1
        xp = np.empty([m, 3], dtype=float)
        for i in range(3):
            xp[:, i] = np.random.normal(mu[i], sig, 1000)

        return xp

    # this function should be looped
    def motion_model(xt,ut): # asks for xt [theta, x, y], control vectors [t, v ,w]; returns state vector [theta, x ,y]
        # state vector is 1x3 array vector [theta, x, y]
        # control vector is the 1x3 odometry data [time, velocity, angular velocity]

        # calls global t, time in the world at previous step
        # ti is defined as previous step's time`

        # control vector is parsed as current time
        # control vector is parsed as current velocity
        # control vector is parsed as current angular velocity

        # delta t defined as difference between previous time and current time
        # theta at previous state
        # x at previous state
        # creates array vector [theta, x, y]

        # calculates robot's orientation
        # calculates robot's x position
        # calculates robot's y position

        # saves theta for next state
        # saves x for next state
        # saves y for next state

        # returns 1x3 state model [theta, x, y]

        global t # this is how I get around t0 not being 0
        ti=t # ti is the timestamp of the previous step

        t = ut[0]
        v = ut[1]
        w = ut[2]

        delta_t = t-ti # time passed is previous time minus current time
        xt_theta = xt[0,0]
        xt_x = xt[0,1]
        xt_y = xt[0,2]

        xti = np.zeros((1, 3))

        xti[0,0] = xt_theta + (w * delta_t) # theta = previous theta + new theta (angular velocity * time)
        xti[0,1] = xt_x + (v * np.cos(xti[0,0]) * delta_t) # finds x location x=v*cos(theta)*t
        xti[0,2] = xt_y + (v * np.sin(xti[0,0]) * delta_t) # finds y location x=v*sin(theta)*t

        # theta_step = xti[0,0]
        # x_step = xti[0,1]
        # y_step = xti[0,2]

        # print xt
        # print ut
        return xti # returns 1x3 vector array [theta, x, y]

    # this function should be looped
    def sensor_model(xt, id): # asks for xt [theta, x, y], id of landmark; returns new state vector zt [theta, x, y]

        # robot state vector is parsed into theta
        # robot state vector is parsed into x position
        # robot state vector is parsed into y position
        # landmark_Groundtruth index is the landmark ID minus 5
        # landmark x data
        # landmark y data
        # landmark x standard dev
        # landmark y standard dev

        # creates 1x2 array vector [range, bearing]

        # returns 1x3 state model [theta, x, y]
        # calculates range - sqrt((xt-xi)^2 + (yt-yi)^2)
        # calculates bearing - arctan((yi-yt)/(xi-xt)) - theta

        # calculates new x; x = xi + r*cos(phi+theta)
        # calculates new y; y = yi + r*sin(phi+theta)

        # returns 1x3 state model [theta, x, y]

        xi_theta = xt[0,0]
        xi_x = xt[0,1]
        xi_y = xt[0,2]
        id=id-6
        landmark_x = landmark[id,1]
        landmark_y = landmark[id,2]
        landmark_xdev = landmark[id,3]
        landmark_ydev = landmark[id,4]

        zt = np.zeros((1,3))

        zt_r = pow(pow(xi_x - landmark_x, 2) + pow(xi_y - landmark_y, 2), 0.5)
        zt_phi = math.atan2((landmark_y - xi_y), (landmark_x - xi_x)) - xi_theta

        zt[0,0] = xi_theta
        zt[0,1] = xi_x + (zt_r * np.cos(zt_phi + xi_theta))
        zt[0,2] = xi_y + (zt_r * np.sin(zt_phi + xi_theta))

        return zt # returns state model [theta, x, y]

    #def error(mu, covar):

    def plotbarriers():

        # plots graph axes
        p.xlabel("x position (m)")
        p.ylabel("y position (m)")
        p.xlim(-8, 10)
        p.ylim(-7, 7)
        p.autoscale = True

        # plots landmark positions
        p.plot(landmark[:, 1], landmark[:, 2], 'ro')

        # plots barriers
        p.plot([landmark[1, 1], landmark[4, 1]], [landmark[1, 2],
                                                  landmark[4, 2]], 'k-')  # connects landmarks 7 and 10
        p.plot([landmark[4, 1], landmark[3, 1]], [landmark[4, 2],
                                                  landmark[3, 2]], 'k-')  # connects landmarks 10 and 9
        p.plot([landmark[3, 1], landmark[0, 1]], [landmark[3, 2],
                                                  landmark[0, 2]], 'k-')  # connects landmarks 9 and 6
        p.plot([landmark[0, 1], landmark[2, 1]], [landmark[0, 2],
                                                  landmark[2, 2]], 'k-')  # connects landmarks 6 and 8
        p.plot([landmark[2, 1], landmark[5, 1]], [landmark[2, 2],
                                                  landmark[5, 2]], 'k-')  # connects landmarks 8 and 11
        p.plot([landmark[5, 1], landmark[6, 1]], [landmark[5, 2],
                                                  landmark[6, 2]], 'k-')  # connects landmarks 11 and 12
        p.plot([landmark[6, 1], landmark[14, 1]], [landmark[6, 2],
                                                   landmark[14, 2]], 'k-')  # connects landmarks 12 and 20
        p.plot([landmark[14, 1], landmark[13, 1]], [landmark[14, 2],
                                                    landmark[13, 2]], 'k-')  # connects landmarks 20 and 19
        p.plot([landmark[13, 1], landmark[12, 1]], [landmark[13, 2],
                                                    landmark[12, 2]], 'k-')  # connects landmarks 19 and 18
        p.plot([landmark[12, 1], landmark[11, 1]], [landmark[12, 2],
                                                    landmark[11, 2]], 'k-')  # connects landmarks 18 and 17
        p.plot([landmark[11, 1], landmark[9, 1]], [landmark[11, 2],
                                                   landmark[9, 2]], 'k-')  # connects landmarks 17 and 15
        p.plot([landmark[9, 1], landmark[4, 1]], [landmark[9, 2],
                                                  landmark[4, 2]], 'k-')  # connects landmarks 15 and 10

        # plots island barriers
        p.plot([landmark[10, 1], landmark[8, 1]], [landmark[10, 2],
                                                   landmark[8, 2]], 'k-')  # connects landmarks 16 and 14
        p.plot([landmark[8, 1], landmark[7, 1]], [landmark[8, 2],
                                                  landmark[7, 2]], 'k-')  # connects landmarks 14 and 13

        # plots landmark annotations
        for i in range(len(landmark)):
            p.annotate(str(landmark[i, 0])[:-2],  # landmark # label
                       # landmark coordinates for label
                       (landmark[i, 1], landmark[i, 2]),
                       textcoords="offset points",  # how to position text
                       xytext=(7, 10),  # distance from text to points (x,y)
                       ha='center')  # horizontal adjustment; left, right, or center

    #def weights(xtm): # asks for state of particle m, returns set of weights


    #return w

    def filter():

        global t
        global xt # calls current state vector
        global xt2
        global mu # calls mu

        #xp=particles(mu,1000) # sampling
        #w=()

        # for i in range(len(mu)):
        #     ut=odometry[i,:]
        #     xti=motion_model(xt[i,:],ut) # xpi is a 3vector
        #     zti=sensor_model(xt[i,:],measurement[i,1])
        #     # calculcate weights

        plotbarriers()
        p.title("Particle Initialization")
        # plots position data derived from odometry readings
        # p.scatter(xp[:, 1], xp[:, 2])

        # measurement step
        for i in range(1,len(odometry)):
            ut=odometry[i,:] # gets current odometry reading [t, v, w]
            t=ut[0]
            if ut[1] != odometry[i-1,1] and ut[2] != odometry[i-1,2]: # checks if robot moved at all
                xti=motion_model(xt,ut) # passes xt, ut, to the motion model. motion model returns 1x3 array
                xt=np.append(xt,xti,axis=0)
            if t =
            # check for measurement

            # print 'this is xti type: ' + str(type(xti))
            # print 'this is xti shape: ' + str(xti.shape)
            # print
            #xt=np.append(xt,xti,axis=0)
        for i in range(len(measurement)):
            #print i
            id=int(measurement[i,1])
            #print 'barcode #: ' + str(id)
            id=np.where(barcodes==id)
            #print 'barcode index retrun: {0}'.format(id)
            id=id[0]
            #print 'tuple index: ' + str(id)
            id=int(id[0])
            #print 'final index: ' + str(id)
            id=int(barcodes[id,0])
            #print 'index value: ' + str(id)
            #xti=sensor_model(xti,id)

            #xp=np.append(xp,xpi,axis=0)
            # print 'this is xti type: ' + str(type(xti))
            # print 'this is xti shape: ' + str(xti.shape)
            # print 'this is xt2 type: ' + str(type(xt2))
            # print 'this is xt2 shape: ' + str(xt2.shape)
            #xt2=np.append(xt2,xti,axis=0)

        plotbarriers()
        p.title("Robot Odometry vs Ground Truth")
        # plots position data derived from odometry readings
        p.plot(xt[:, 1], xt[:, 2], 'b-', label='Robot Odometry')
        #p.plot(xt[:, 1], xt[:, 2], 'r-', label='Sensor Added')
        # plots position data from motion capture
        #p.plot(groundtruth[:, 1], groundtruth[:, 2],'g-', label='Ground Truth')
        p.legend(loc='best')

        p.show()

    filter()

# ------------- measurement model----------------
# ---------- part 6 of the homework--------------


def pt6():

    # robot
    xytheta = np.array([
        (2, 3, 0),
        (0, 3, 0),
        (1, -2, 0)])

    # landmark
    xyland = np.array([
        (1.88032539, -5.57229508, 6), # landmark x, landmark y, landmark id
        (3.07964257, 0.24942861, 13),
        (-1.04151642, 2.80020985, 17)])

    rangebearing = np.zeros((3, 2))  # range, bearing

    for i in range(len(xytheta)):
        rangebearing[i, 0] = (pow(pow(xytheta[i, 0] - xyland[i, 0], 2) + pow(xytheta[i, 1] - xyland[i, 1], 2), 0.5))
        rangebearing[i, 1] = math.atan2((xyland[i, 1] - xytheta[i, 1]), (xyland[i, 0] - xytheta[i, 0])) - xytheta[i, 2]

    # A E S T H E T I C
    p.title("Global x,y Position")
    p.xlabel("x position (m)")
    p.ylabel("y position (m)")

    p.plot(xyland[:, 0], xyland[:, 1], 'rx', label='landmark position')
    p.plot(xytheta[:, 0], xytheta[:, 1], 'go', label='robot position')
    #p.plot(xy[:,0],xy[:,1],'bo',label='calculated position')

    for i in range(len(xyland)):
        p.annotate(str(i),  # [:-2], # coordinate label
                   (xyland[i, 0], xyland[i, 1]),  # coordinates for label
                   textcoords="offset points",  # how to position text
                   xytext=(-4, -10),  # distance from text to points (x,y)
                   ha='center')  # horizontal adjustment; left, right, or center

        p.annotate(str(i),  # [:-2], # coordinate label
                   (xytheta[i, 0], xytheta[i, 1]),  # coordinates for label
                   textcoords="offset points",  # how to position text
                   xytext=(-4, -10),  # distance from text to points (x,y)
                   ha='center')  # horizontal adjustment; left, right, or center

    p.legend(loc='best')

    for i in range(len(xyland)):
        print 'point ' + str(i)
        print 'range: ' + str(rangebearing[i, 0]) + ' (m)'
        print 'bearing: ' + str(rangebearing[i, 1]) + ' (rad)'

    p.show()

# main funciton


def main():
    pt3()
    # print 'Enter exercise to be graded'
    # print '2, 3, or 6'
    #
    # while True:
    #     input = raw_input()
    #     try:
    #         input = int(input)
    #         if int(input) == 2:
    #             pt2()
    #             break
    #         elif int(input) == 3:
    #             pt3()
    #             break
    #         elif int(input) == 6:
    #             pt6()
    #             break
    #         elif int(input) != 2 or int(input) != 3 or int(input) != 6:
    #             print 'Not a valid entry, re-enter exercise to be graded'
    #     except ValueError:
    #         print 'Not a valid entry, re-enter exercise to be graded'


main()
