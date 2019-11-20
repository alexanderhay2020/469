# ME 469 - Homework 1B

Alexander Hay<br/>
ME 469, HW2, Part B<br/>
Machine Learning
Algorithm: Neural Network
Learning Aim: Motion Model
Input: t, x, y, theta, v, w
Output: dx, dy, dtheta
---------------------------------
## File Content Breakdown

#### data
+ 10_input.tsv - a snapshot of first 10 training data samples
+ test input.ts - 10% of the total data, used to test nn model
+ training_input - 45% of the total data, used to build network with
+ validation_data - 45% of the total data, held to verify model with

#### programs
+ nn.py - broken, but shows framework of layered network
+ perceptron.py - proof of concept
+ run.py - perceptron concept applied to training data

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
