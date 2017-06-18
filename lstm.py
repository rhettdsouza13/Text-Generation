import tensorflow as tf
import numpy
from initializer import *
n_input=5
x = tf.placeholder(tf.float32,[n_input,28])
y = tf.placeholder(tf.float32,[1,28])
data = numpy.load("/home/rhett/Documents/TextGen/Lyrics/parse.npy")
maps = numpy.load("/home/rhett/Documents/TextGen/Lyrics/maps.npy")

x_ = tf.split(x,n_input,0)
cell = tf.contrib.rnn.MultiRNNCell([tf.contrib.rnn.BasicLSTMCell(750),tf.contrib.rnn.BasicLSTMCell(512)])

outputs, states = tf.contrib.rnn.static_rnn(cell, x_, dtype=tf.float32)

W = weight_initializer([512,28])
b = bias_initializer([28])

h = tf.matmul(outputs[-1],W)+b

sess = tf.Session()

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=h))

train_step = tf.train.RMSPropOptimizer(1e-3).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(h,1), tf.argmax(y,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess.run(tf.global_variables_initializer())
print len(data[0])
for i in xrange(len(data[0])-3):
    xs=data[0][i]
    ys=[data[1][i]]
    if i%50==0:
        acc, error = sess.run([accuracy, cross_entropy], feed_dict = {x:xs, y:ys})
        print "Step: " + str(i) + ", Accuracy: " + str(acc) + ", Loss: " + str(error)
    sess.run(train_step, feed_dict = {x:xs, y:ys} )
nextcall = data[0][len(data[0])-1]

gen=[]
for val in nextcall:
    gen.append(val)
print gen
for i in xrange(200):
    print "pass"
    index = sess.run(tf.argmax(h,1), feed_dict = {x:nextcall})
    newvec = numpy.zeros(28)
    newvec[index]=1
    gen.append(newvec)
    nextcall = nextcall[1:n_input]
    nextcall.append(newvec)
numpy.save("/home/rhett/Documents/TextGen/Lyrics/generated.npy", gen)
