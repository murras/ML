import tensorflow as tf

# X와 Y값 입력
x_train = [1, 2, 3]
y_train = [3, 5, 7]

W=tf.Variable(tf.random_normal([1]),name='weight')
b=tf.Variable(tf.random_normal([1]),name='bias')

# hypothesis 
hypothesis=x_train*W+b

# cost function
cost = tf.reduce_mean(tf.square(hypothesis-y_train))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train=optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    sess.run(train)
    if step % 40 == 0:
        print("step: ", step, "cost: ", sess.run(cost), "W: ", sess.run(W), "b: ", sess.run(b))

    
