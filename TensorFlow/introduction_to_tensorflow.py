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


#Exerise 
# Import constant from TensorFlow
from tensorflow import constant

# Convert the credit_numpy array into a tensorflow constant
credit_constant = constant(credit_numpy)

# Print constant datatype
print('\n The datatype is:', credit_constant.dtype)

# Print constant shape
print('\n The shape is:', credit_constant.shape)


#2
# Define the 1-dimensional variable A1
A1 = Variable([1, 2, 3, 4])

# Print the variable A1
print('\n A1: ', A1)

# Convert A1 to a numpy array and assign it to B1
B1 = A1.numpy()

# Print B1
print('\n B1: ', B1)