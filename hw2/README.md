# ME 469 - Homework 1B

Alexander Hay<br/>
ME 469, HW2, Part A<br/>
Machine Learning

## Preface

I constructed the neuron first, to understand how it worked before really committing to manipulating the datasets. I followed a video and a few articles, cited below. The code is very similar as I used the video to learn how a neural net works conceptually. The next step is incorporating the data, whether its disseminating the data into a neuron or figuring out how to make more than one neuron. Layers will be after.

Data was split into 3 partitions (45/45/10):

1) input_data - this will be used while constructing the neural net

2) validation_data - this will be used to verify whether the algorithm is over fitting the input_data and to tune parameters

3) test_data - a small sample in which to run the algorithm on

ds1 was chosen because it has more data
---------------------------------
## Perceptron Brekadown

### Imports and Global Variables:

##### Imports:
+ numpy

##### Global Variables:

+ input_data - ds1_Groundtruth.dat and ds1_Odometry.dat data, sorted by timestamp

+ Data has only gone through minor combing for reason stated above.

### Functions

#### sigmoid(x)
Activation Function:
+ Allows the neuron to react in a non-binary fashion (ie. not 0/1, true/false)
+ Somewhat computationally expensive
+ This is a parameter that can be changed to improve performance, though
  sigmoid function seems to be the most common
  + Sigmoid function is preferred because "the nonlinear properties of this
    function means that the rate of change is slower at the extremes and
    faster in the center.""

#### sigmoid_derivative(x):
Gradient calculation for back propogation

### How It Works

The perceptron in this exercise works as follows; first, the loop starts by taking in an input array. It then assigns each column a weight. The dot-product of the input column and its weight are calculated and passed through the sigmoid function. The sigmoid function output is then compared to the expected output and an error is derived. An adjustment to the error is needed to determine a proper weight to each column. This is back-propogation. The adjustment is calculated by multiplying the error by the gradient along the sigmoid, or rather, its derivative. This process repeated ad infinitum would produce a proper weight for the input column. In this case the loop is repeated 20,000 times.

## References
+ Arnx, Arthur. “First Neural Network for Beginners Explained (with Code).” Medium, Towards Data Science, 11 Aug. 2019, towardsdatascience.com/first-neural-network-for-beginners-explained-with-code-4cfd37e06eaf.

+ Fried, Charles. “Let's Code a Neural Network From Scratch.” Medium, TypeMe, 6 Apr. 2017, medium.com/typeme/lets-code-a-neural-network-from-scratch-part-1-24f0a30d7d62.

+ Spencer-Harper, Milo, director. Create a Simple Neural Network in Python from Scratch. YouTube, PolyCode, 31 Mar. 2018, www.youtube.com/watch?v=kft1AJ9WVDk.

+ Spencer-Harper, Milo. “How to Build a Simple Neural Network in 9 Lines of Python Code.” Medium, 8 Apr. 2019, medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1.
