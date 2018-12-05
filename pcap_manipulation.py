import numpy
import pandas as pd
import os
from sklearn import preprocessing
rootdir = os.getcwd()
video_samples = []
class video_sample:
    def __init__(self, data, labels):
        self.data = preprocessing.normalize(data)
        self.labels = [0,0,0,0,0,1]
        if labels == 'tiny':
            self.labels = [0,0,0,0,0,1]
        if labels == 'small':
            self.labels = [0,0,0,0,1,0]
        if labels == 'medium':
            self.labels = [0,0,0,1,0,0]
        if labels == 'large':
            self.labels = [0,0,1,0,0,0]
        if labels == 'hd720':
            self.labels = [0,1,0,0,0,0]
        if labels == 'hd1080':
            self.labels = [1,0,0,0,0,0]


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".csv"):
            df=pd.read_csv(subdir + '/' + file,usecols = [1],skiprows = [0],header=None)
            data = df.values
            x = len(data) / 5
            if(x >= 1):
                data = numpy.array_split(data,x)
                for sample in data:
                    if(len(sample) > 5):
                        sample = sample[:5, :]
                    video_samples.append(video_sample(sample,subdir.split('/')[-1]))
X = numpy.array([sample.data for sample in video_samples])
Y = numpy.array([sample.labels for sample in video_samples])
rnd_indices = numpy.random.rand(len(X)) < 0.70
train_x = X[rnd_indices]
train_y = Y[rnd_indices]
test_x = X[~rnd_indices]
test_y = Y[~rnd_indices]

import tensorflow as tf

# Parameters
learning_rate = 0.001
training_epochs = 1000
batch_size = 10
display_step = 1

# Network Parameters
n_hidden_1 = 256 # 1st layer number of neurons
n_hidden_2 = 256 # 2nd layer number of neurons
n_input = 5 # MNIST data input (img shape: 28*28)
n_classes = 6 # MNIST total classes (0-9 digits)

# tf Graph input
X = tf.placeholder("float", [None, n_input])
Y = tf.placeholder("float", [None, n_classes])

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}


# Create model
def multilayer_perceptron(x):
    # Hidden fully connected layer with 256 neurons
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    # Hidden fully connected layer with 256 neurons
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    # Output fully connected layer with a neuron for each class
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Construct model
logits = multilayer_perceptron(X)

# Define loss and optimizer
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
    logits=logits, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)
# Initializing the variables
init = tf.global_variables_initializer()
total_batch = len(train_x)
size = len(test_x)
train_x = numpy.reshape(train_x, (total_batch, 5))
test_x = numpy.reshape(test_x, (size, 5))
print(train_x,train_y)
# with tf.Session() as sess:
#     sess.run(init)
#
#     # Training cycle
#     for epoch in range(training_epochs):
#         avg_cost = 0.
#         # Loop over all batches
#         # Run optimization op (backprop) and cost op (to get loss value)
#         _, c = sess.run([train_op, loss_op], feed_dict={X: train_x,
#                                                         Y: train_y})
#         # Compute average loss
#         avg_cost += c / total_batch
#         # Display logs per epoch step
#         if epoch % display_step == 0:
#             print("Epoch:", '%04d' % (epoch+1), "cost={:.9f}".format(avg_cost))
#     print("Optimization Finished!")
#
#     # Test model
#     pred = tf.nn.softmax(logits)  # Apply softmax to logits
#     correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(Y, 1))
#     # Calculate accuracy
#     accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
#     print("Accuracy:", accuracy.eval({X: test_x, Y: test_y}))
