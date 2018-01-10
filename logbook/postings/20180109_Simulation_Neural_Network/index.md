# Using a neural network to extract the cosmo field

## 1. Neural network concepts

A **neural network** consists of an **input layer**, some **hidden layers** and an **output layer**. The layer number of a neural network doesn't count in the input layer, because the input layer doesn't modify the data.

A **fully connected layer** is an affine transformation of the input followed with a **ReLU** function. The definition is ![fc_def](http://latex.codecogs.com/svg.latex?Y%3DReLU%28XW%2Bb%29).

 - Y is the output of the layer.
 - X is the output of the previous layer.
 - W (weight) and b (bias) are the parameters that are waiting for training.
 - W has the shape of (len(X), len(Y)).
 - b has the shape of (len(Y)).

The **input layer** has the same size with the input data.

The **output layer** is a fully connected layer without a ReLU function. The size of the output layer is the same with the output data.

The **ReLU** function is an activation function which adds some nonlinear factor to the network, so that the network can solve nonlinear problem. There are some other kind of activation functions. ReLU is proved to be the most efficient one in most case.

ReLU function definition

![relu_def](http://latex.codecogs.com/svg.latex?f%28x%29%3D%7B%5Cbegin%7Bcases%7Dx%26%7B%5Cmbox%7Bif%20%7Dx%3E0%5C%5C0%26%7B%5Cmbox%7Botherwise%7D%7D%5Cend%7Bcases%7D%7D)

**Dropout** is an optimization method to prevent the network to be overfitting. It masks out by default 50% output of a layer. It does not have any training parameter.

![dropout](https://cdn-images-1.medium.com/max/1200/1*iWQzxhVlvadk6VAJjsgXgg.png)

**Loss function** is a measurement function of how bad the network does. In most case the lower, the better. We calculate the partial derivative of the loss function with respective to each training parameter.

The loss function I use is Mean Square Error (MSE) function, also called L2 function:

![loss_func](http://latex.codecogs.com/svg.latex?MSE%3D%7B%5Cfrac%7B1%7D%7Bn%7D%7D%5Csum%20_%7Bi%3D1%7D%5E%7Bn%7D%28Y_%7Bi%7D-%7B%5Chat%20%7BY_%7Bi%7D%7D%7D%29%5E%7B2%7D)

 - ![y](http://latex.codecogs.com/svg.latex?Y_i) is the known result.
 - ![y](http://latex.codecogs.com/svg.latex?%5Chat%7BY%7D_i) is the output of the network.

There are several optimization algorithms to update the training parameters. The one I use is **Adam**, which is introduced in [arXiv:1412.6980](https://arxiv.org/abs/1412.6980).

## 2. The neural network structure

The neural network is a 4-layer fully connected network. The function is to do a regression task to guess the real cosmo field signal.

![structure](structure.png)

## 3. Training and result

Since one cycle of the simulation output is 24 hours, the network takes 23-hour all-field data subtracted with polyfit as the input, 23-hour cosmo data as the known result to do the training. The rest 1-hour data is used to test the network.

I tried several network structure. These are the result for the network with and without dropout.

Network with dropout:

![cosmo_nn_1](cosmo50_1.png)

Network without dropout:

![cosmo_nn](cosmo50.png)
