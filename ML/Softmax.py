import tensorflow as tf
from pcap_manipulation import load_pcap_data_hot
import numpy
import matplotlib.pyplot as plt

SAMPLE_SIZE = 30
# Parameters
learning_rate = 0.01
training_epochs = 5000
batch_size = 512
display_step = 50

# Network Parameters
n_hidden_1 = 256
n_hidden_2 = 256
n_input = SAMPLE_SIZE
n_classes = 6

train_x, train_y, test_x, test_y = load_pcap_data_hot(SAMPLE_SIZE)
# tf Graph input
X = tf.placeholder("float", [None, n_input])
Y = tf.placeholder("float", [None, n_classes])
cost_history = numpy.empty(shape=[1], dtype=float)

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
    layer_1 = tf.nn.relu(tf.matmul(x, weights['h1']) + biases['b1'])
    # Hidden fully connected layer with 256 neurons
    layer_2 = tf.nn.relu(tf.matmul(layer_1, weights['h2']) + biases['b2'])
    # Output fully connected layer with a neuron for each class
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Construct model
logits = multilayer_perceptron(X)

# Define loss and optimizer
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
    logits=logits, labels=Y))
regularizer = tf.nn.l2_loss(weights['h1']) + tf.nn.l2_loss(weights['h2'] + tf.nn.l2_loss(weights['out'] ))
loss_op = tf.reduce_mean(loss_op + regularizer*0.05)
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)


init = tf.global_variables_initializer()
total_batch = len(train_x)
size = len(test_x)
train_x = numpy.reshape(train_x, (total_batch, SAMPLE_SIZE))
test_x = numpy.reshape(test_x, (size, SAMPLE_SIZE))
with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        offset = (epoch * batch_size) % (train_y.shape[0] - batch_size)
        batch_data = train_x[offset:(offset + batch_size), :]
        batch_labels = train_y[offset:(offset + batch_size), :]

        # Run optimization op (backprop) and cost op (to get loss value)
        _, c = sess.run([train_op, loss_op], feed_dict={X: batch_data,
                                                           Y: batch_labels})
        # Compute average loss
        avg_cost += c / batch_size
        # Display logs per epoch step
        if epoch % display_step == 0:
            # Calculate accuracy
            print("Epoch:", '%04d' % (epoch+1), "cost={:.9f}".format(avg_cost))
        cost_history = numpy.append(cost_history, sess.run(loss_op, feed_dict={X: train_x,
                                                           Y: train_y}))

    print("Optimization Finished!")
    # Test model
    pred = tf.nn.softmax(logits)  # Apply softmax to logits
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(Y, 1))
    print(correct_prediction)
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print("Accuracy:", accuracy.eval({X: test_x, Y: test_y}))
    plt.plot(range(len(cost_history)), cost_history)
    plt.axis([0, training_epochs, 0, numpy.max(cost_history)])
    plt.show()
