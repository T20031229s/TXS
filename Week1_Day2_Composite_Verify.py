import numpy as np
#1.定义两个变换
shear = np.array([[1,1],[0,1]])   #剪切（竖线变斜）
rot45 = np.array([[1,-1],[1,0]])   #逆时针旋转45°

#2.计算两种顺序的复合矩阵     矩阵乘法从右往左读
compose_RS = shear @ rot45   #先旋转（R),再剪切（S）
compose_SR = rot45 @ shear   #与上一个相反

print("[先旋转后剪切]的复合矩阵(shear @ rot45):",compose_RS)
print("\n[先剪切后旋转]的复合矩阵(rot45 @ shear)",compose_SR)
