# What is TensorFlow
"""
Open-source library for graph-based numerical computation
    1. Developed by the Google Brain Team
Low and high level APIs
    1. Addition, multiplication, differentiation
    2. Machine learning models.
"""
import tensorflow as tf

'''
What is a tensor?
1. Generalization of vectors and matrices
2. Collection of numbers
3. Specific shape
'''
# 0D Tensor
d0 = tf.ones((1,))
print(d0)

# 1D Tensor
d1 = tf.ones((2,))
print(d1)

# 2D Tensor
d2 = tf.ones((2,2,))
print(d2)

# 3D Tensor
d3 = tf.ones((2,2,2))
print(d3)
'''
[[1. 1.]
  [1. 1.]]], shape=(2, 2, 2), dtype=float32)
'''
# Print the 3D tensor
print(d3.numpy())
'''
[[[1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]]]
'''


#Defining constants in Tensorflow
'''
A constant is the simplest category of tensor
    - Not trainable
    - Can have any dimension
'''
from tensorflow import constant
#Define a 2X3 constant.
a = constant(3, shape=[2,3])
#Define a 2X2 constant
b = constant([1,2,3,4], shape=[2,2])


#Defining and initialization variable
import tensorflow as tf

#Define a variable
a0 = tf.Variable([1,2,3,4,5,6], dtype=tf.float32)
a1 = tf.Variable([1,2,3,4,5,6], dtype=tf.float16)

#Define a constant
b = tf.constant(2, tf.float32)

# Compute their product
c0 = tf.multiply(a0, b)
c1 = a0*b