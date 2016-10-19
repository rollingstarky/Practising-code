import tensorflow as tf

#Create a Variable initialized with scalar 0.
state=tf.Variable(0,name="counter")
one=tf.constant(1)
new_value=tf.add(state,one)

update=tf.assign(state,new_value)

#First have to add the `init` Op to the graph.
init_op=tf.initialize_all_variables()

#launch the graph and run the ops.
with tf.Session() as sess:
    #run the init op
    sess.run(init_op)
    #print the state's initial value
    print(sess.run(state))
    #Run the op that updates 'state',loop 3 times.
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))

#output

#0
#1
#2
#3
