###RNN mnist example###

import input_data
import tensorflow as tf

# number 1 to 10 data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#parameters
lr = 0.001
training_iters = 100000
batch_size = 128


n_inputs = 28 #MNIST data input(img shape: 28*28)
n_steps = 28 #time steps
n_hidden_unis = 128 #neurons in hidden layer
n_classes = 10

#tf Graph input

