import numpy as np

#1.创建向量和矩阵 （对应数学里的箭头和方阵）
v = np.array([2,3])   #二维向量
A = np.array([[1,2],[3,4]])   #2*2矩阵

#2.矩阵乘法（对应线性变换的“复合”）
B = np.array([[2,0],[1,3]])
print("A@B的结果（先A后B的复合效果):\n",A@B)     #@是python中矩阵乘法运算符   \n表示换行

#3.核心验证：证明矩阵乘法不满足交换律(对比B@A)
print("\nB@A的结果（交换顺序）:\n",B@A)

#4.转置（把网络翻转)
print("\nA的转置 A.T:\n",A.T)





#练习复习
import numpy as np
v = np.array([2,3])   #创建的二维向量
A = np.array([1,2],[3,4])   #创建的2*2的矩阵A
B = np.array([2,3],[6,7])   #创建的2*2的矩阵B
print("A@B的结果（先A后B的复合效果）:\n",A@B)
print("\nB@A的结果（交换顺序，即先B后A的复合效果）:\n",B@A)
print("\nA的转置 A.T:\n",A.T)
