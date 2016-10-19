#enter an interactive TensorFlow Session.
import tensorflow as tf
sess=tf.InteractiveSession()

x=tf.Variable([1.0,2.0])
a=tf.constant([3.0,3.0])

#intialize 'x' using the run() method of its initializer op.
x.initializer.run()

#add an op to subtract 'a' from 'x'
sub=tf.sub(x,a)
print(sub.eval())
# ==> [-2.-1.]

#close session
