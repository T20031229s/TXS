import numpy as np
#1.定义一个变换矩阵（剪切矩阵）
A = np.array([[1,1],[0,1]])
#2.目标向量（就是想让那个点落在【3，1】上？）
v = np.array([3,1])
#3.求解 Ax = v
x = np.linalg.solve(A,v)

print("方程Ax = v的解是",x)
print("验证A@x=",A@x)

#4.用逆矩阵再算一遍，结果应一样
A_inv = np.linalg.inv(A)
x_via_inv = A_inv @ v
print("用逆矩阵算的解：",x_via_inv)