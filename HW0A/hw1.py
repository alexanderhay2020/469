# Alexander Hay
# ME_469, HW0, Part A2
# Dataset 1, Particle Filter

# import necessities
import numpy as np
import pylab as p
import math

# global variables
barcodes=np.loadtxt('ds1_Barcodes.dat') #
groundtruth=np.loadtxt('ds1_Groundtruth.dat') # position data from motion capture (may be taken as known information for filtering)
landmark=np.loadtxt('ds1_Landmark_Groundtruth.dat') # landmark data
measurement=np.loadtxt('ds1_Measurement.dat') # position data measureed from robot
odometry=np.loadtxt('ds1_Odometry.dat') # time, forward v, angular v, measured from robot

initialx=0.98038490
initialy=-4.99232180
initialrad=1.44849633

# motion Model
def pt2():

    # timestamp, velocity, angular velocity
    odo=[(0,0.5,0),
    (1,0,(-1/(2*math.pi))),
    (2,0.5,0),
    (3,0,(1/(2*math.pi))),
    (4,0.5,0)]

    odo=np.array(odo)

    # array of x, y, theta values
    xytheta=np.zeros((len(odo),3))

    for i in range(len(odo)):
        time=1 # delta t is always 1 second
        vel=odo[i,1] # velocity data

        xytheta[i,2]=(odo[i,2]*time)+xytheta[i-1,2] # calculates theta value and adds to previous value
        xytheta[i,0]=xytheta[i-1,0]+(vel*np.cos(xytheta[i,2])*time) # calculates x and adds to previous value
        xytheta[i,1]=xytheta[i-1,1]+(vel*np.sin(xytheta[i,2])*time) # calculates y and adds to previous value

    xytheta[0,0]=0
    xytheta[0,1]=0
    # this reset origin values since they were overwritten
    # This is not the ideal solution, but it works and displays the line correctly

    # A E S T H E T I C
    p.title("Position over Time")
    p.xlabel("x position (m)")
    p.ylabel("y position (m)")
    p.xlim(-0.25,1.75)
    p.plot(xytheta[:,0],xytheta[:,1])

    p.show()

# applied motion model
def pt3():

    def odo():

        # 2D array to hold calculated x, y, and theta values
        delta=np.zeros((len(odometry),3))

        delta[0,0]=initialx
        delta[0,1]=initialy
        delta[0,2]=initialrad

        for i in range(1,len(odometry)-1):

            # ************************************
            # This section calculates robot's position
            # from odometry data

            time=odometry[i+1,0]-odometry[i,0] # executes command from timestamp until next command is issued
            vel=odometry[i,1]

            delta[i,2]=delta[i-1,2]+(odometry[i,2]*time) # theta value in rad
            delta[i,0]=delta[i-1,0]+vel*np.cos(delta[i,2])*time # finds x displacement (m) x=v*cos(theta)*t
            delta[i,1]=delta[i-1,1]+vel*np.sin(delta[i,2])*time # finds y displacement (m) x=v*sin(theta)*t

        return [delta]

    #def filter():

    def plotbarriers():

        # plots graph axes
        p.xlabel("x position (m)")
        p.ylabel("y position (m)")
        p.xlim(-8,10)
        p.ylim(-7,7)
        p.autoscale=True

        # plots landmark positions
        p.plot(landmark[:,1],landmark[:,2],'ro')

        # plots barriers
        p.plot([landmark[1,1],landmark[4,1]],[landmark[1,2],landmark[4,2]],'k-') # connects landmarks 7 and 10
        p.plot([landmark[4,1],landmark[3,1]],[landmark[4,2],landmark[3,2]],'k-') # connects landmarks 10 and 9
        p.plot([landmark[3,1],landmark[0,1]],[landmark[3,2],landmark[0,2]],'k-') # connects landmarks 9 and 6
        p.plot([landmark[0,1],landmark[2,1]],[landmark[0,2],landmark[2,2]],'k-') # connects landmarks 6 and 8
        p.plot([landmark[2,1],landmark[5,1]],[landmark[2,2],landmark[5,2]],'k-') # connects landmarks 8 and 11
        p.plot([landmark[5,1],landmark[6,1]],[landmark[5,2],landmark[6,2]],'k-') # connects landmarks 11 and 12
        p.plot([landmark[6,1],landmark[14,1]],[landmark[6,2],landmark[14,2]],'k-') # connects landmarks 12 and 20
        p.plot([landmark[14,1],landmark[13,1]],[landmark[14,2],landmark[13,2]],'k-') # connects landmarks 20 and 19
        p.plot([landmark[13,1],landmark[12,1]],[landmark[13,2],landmark[12,2]],'k-') # connects landmarks 19 and 18
        p.plot([landmark[12,1],landmark[11,1]],[landmark[12,2],landmark[11,2]],'k-') # connects landmarks 18 and 17
        p.plot([landmark[11,1],landmark[9,1]],[landmark[11,2],landmark[9,2]],'k-') # connects landmarks 17 and 15
        p.plot([landmark[9,1],landmark[4,1]],[landmark[9,2],landmark[4,2]],'k-') # connects landmarks 15 and 10

        # plots island barriers
        p.plot([landmark[10,1],landmark[8,1]],[landmark[10,2],landmark[8,2]],'k-') # connects landmarks 16 and 14
        p.plot([landmark[8,1],landmark[7,1]],[landmark[8,2],landmark[7,2]],'k-') # connects landmarks 14 and 13

        # plots landmark annotations
        for i in range(len(landmark)):
            p.annotate(str(landmark[i,0])[:-2], # landmark # label
            (landmark[i,1],landmark[i,2]), # landmark coordinates for label
            textcoords="offset points", # how to position text
            xytext=(7,10), # distance from text to points (x,y)
            ha='center') # horizontal adjustment; left, right, or center

    def main():

        [delta]=odo()
        plotbarriers()
        p.title("Robot Odometry vs Ground Truth")
        p.plot(delta[:,0],delta[:,1],'b-',label='Robot Odometry') # plots position data derived from odometry readings
        p.plot(groundtruth[:,1],groundtruth[:,2],'g-',label='Ground Truth') # plots position data from motion capture
        p.legend(loc='best')

        p.show()

    main()

# measurement model
def pt6():

    # robot
    xytheta=np.array([
    (2,3,0),
    (0,3,0),
    (1,-2,0)])

    # landmark
    xyland=np.array([
    (1.88032539,-5.57229508,6),
    (3.07964257,0.24942861,13),
    (-1.04151642,2.80020985,17)])

    rangebearing=np.zeros((3,2)) # range, bearing

    for i in range(len(xytheta)):
        rangebearing[i,0]=(pow(pow(xytheta[i,0]-xyland[i,0],2)+pow(xytheta[i,1]-xyland[i,1],2),0.5))
        rangebearing[i,1]=math.atan2((xyland[i,1]-xytheta[i,1]),(xyland[i,0]-xytheta[i,0]))-xytheta[i,2]

    # A E S T H E T I C
    p.title("Global x,y Position")
    p.xlabel("x position (m)")
    p.ylabel("y position (m)")

    p.plot(xyland[:,0],xyland[:,1],'rx',label='landmark position')
    p.plot(xytheta[:,0],xytheta[:,1],'go',label='robot position')
    #p.plot(xy[:,0],xy[:,1],'bo',label='calculated position')

    for i in range(len(xyland)):
        p.annotate(str(i),#[:-2], # coordinate label
        (xyland[i,0],xyland[i,1]), # coordinates for label
        textcoords="offset points", # how to position text
        xytext=(-4,-10), # distance from text to points (x,y)
        ha='center') # horizontal adjustment; left, right, or center

        p.annotate(str(i),#[:-2], # coordinate label
        (xytheta[i,0],xytheta[i,1]), # coordinates for label
        textcoords="offset points", # how to position text
        xytext=(-4,-10), # distance from text to points (x,y)
        ha='center') # horizontal adjustment; left, right, or center

    p.legend(loc='best')

    for i in range(len(xyland)):
        print 'point '+str(i)
        print 'range: '+str(rangebearing[i,0])+' (m)'
        print 'bearing: '+str(rangebearing[i,1])+' (rad)'

    p.show()

# main funciton
def main():

    print 'Enter exercise to be graded'
    print '2, 3, or 6'

    while True:
        input=raw_input()
        try:
            input=int(input)
            if int(input) == 2:
                pt2()
                break
            elif int(input) == 3:
                pt3()
                break
            elif int(input) == 6:
                pt6()
                break
            elif int(input) != 2 or int(input) != 3 or int(input) != 6:
                print 'Not a valid entry, re-enter exercise to be graded'
        except ValueError:
            print 'Not a valid entry, re-enter exercise to be graded'

main()
