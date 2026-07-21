import numpy as np
#1.定义两个二维向量（对应刚才视频中的箭头）
v = np.array([2,1])   #指向右上方
w = np.array([-1,2])   #指向左上方

print("向量 v = ",v)
print("向量 w = ",w)


#2.标量乘法（拉伸/压缩箭头）
print("\n把v拉长3倍:",3*v)


#3.向量加法（注意收尾相连）
print("v+w",v+w)


#4.线性组合
#随便取两个系数c1=3,c2=2,看看合起来的向量指向哪里
c1,c2 = 3,2
combo = c1*v +c2*w
print(f"\n{c1}*v + {c2}*w的线性组合结果 =",combo)

 
#5.[验证基向量] 尝试用标准基 e1=(1,0),e2=(0,1)拼出（5,3）
e1 = np.array([1,0])
e2 = np.array([0,1])
result = 5*e1 + 3*e2
print(f"\n用基向量拼出（5,3）:{result}")   


#03矩阵与线性变换部分
import numpy as np
#1.定义一个剪切矩阵（竖线变斜）
shear = np.array([[1,1],[0,1]])
#2.定义标准基向量
e1 = np.array([1,0])
e2 = np.array([0,1])
#3.运行看基向量被拉到哪里去了
print("e2被拉到了:",shear @ e2)




#复习练习
import numpy as np
v = np.array([1,2])
w = np.array([-3,5])   #定义两个二维向量
print("向量 v = ",v)
print("向量 w = ",w)   #输出两个向量的表示形式
print("\n把向量w拉长5倍:",5*w)   #向量的拉伸、向量数乘
print("\n v+w :",v+w)   #向量加法

#线性组合后的练习复习
c1,c2 = 2,7
combo = c1*v+c2*w
print(f"\n{c1}*v +{c2}*w的线性组合结果 = ",combo)   #f是格式化字符串，可以在字符串的花括号里直接写变量名或表达式而无影响
#验证基向量
e1 = np.array([1,0])
e2 = np.array([0,1])
result = 3*e1+7*e2
print(f"\n用基向量拼出(3,7):",result)
#矩阵与线性变换
shear = np.array([[1,1],[0,1]])
e1 = np.array([1,0])
e2 = np.array([0,1])
print("e2被拉到了：",shear@e2)
