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