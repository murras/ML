## lab 01 TensorFlow 설치 및 기본적 Operations

### TensorFlow
- data flow graph를 이용한 numerical computation을 하기 위한 라이브러리.

- tf.constant
- tf.Session
- sess.run()
```py
node1 = ts.constant(3.0, tf.float32)
sess = tf.Session()
print(sess.run(node1))
```
- placeholder
- feed_back
```py
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b
print(sess.run(adder_node, feed_dict={a: 3, b: 4.5}))
print(sess.run(adder_node, feed_dict={a: [1,3], b:[2,4]}))
```
- Rank : 배열의 차원
- Shape : 배열의 모양 ([2,3])
- Type : float32, int32

---
## lab 02 