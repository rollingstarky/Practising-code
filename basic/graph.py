import tensorflow as tf

#create a Constant op that produces a 1x2 matrix.
matrix1=tf.constant([[3.,3.]])

#another matrix(2x1).
matrix2=tf.constant([[2.],[2.]])

#create a Matmul op.
product=tf.matmul(matrix1,matrix2)

#Launch the default graph.
sess=tf.Session()

#The cal 'run' causes the execution of three ops in the graph.

result=sess.run(product)
print(result)
# ==> [[12.]] : a numpy `ndarray` object.

#close the Session
sess.close()


