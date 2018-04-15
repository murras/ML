## lab 01 TensorFlow 설치 및 기본적 Operations

### TensorFlow
- data flow graph를 이용한 numerical computation을 하기 위한 라이브러리.


##
- tf.constant
- tf.Session
- sess.run()
```py
import tensorflow as tf
node1 = tf.constant(3.0, tf.float32)
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

![Image](https://i.imgur.com/1psnmmX.png)
- y값 : 실제 데이터값

- Variable: TensorFlow가 사용하는 variable, trainable한 변수.
- W와 b의 값을 몰라서 random한 값을 준다.
- tf.random_normal([1]) 
    - [1]: 값이 하나인 1차원 Node.
