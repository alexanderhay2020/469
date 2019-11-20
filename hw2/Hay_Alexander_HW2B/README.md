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
  + 10_input.tsv was moved to assignment home directory for code to function
+ test input.ts - 10% of the total data, used to test nn model
+ training_input - 45% of the total data, used to build network with
  + training_input.tsv was moved to assignment home directory for code to function
+ validation_data - 45% of the total data, held to verify model with

#### programs
+ perceptron.py - proof of concept
+ run_single.py - perceptron concept applied to training data
+ run.py - two layers of perceptrons applied to random data

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
