#标量广播
import numpy as np
#1.创建一个2×3矩阵
arr = np.array([[1,2,3],
                [4,5,6]])

#2.标量乘法：例如将数字10广播到每一个元素
result = arr * 10
print("数组每个元素乘以10:\n",result)

#3.标量加法：将数字100广播到每一个元素
result_add = arr + 100
print("\n数组中的每个元素加上100:\n",result_add)




#行/列广播（应用于数据归一化、去中心化）
#1.创建一个3×3矩阵
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

#场景A：矩阵的每一行都减去“该行的平均值”（行操作）
row_means = matrix.mean(axis=1)   #axis=1 按行求平均，得到形状(3,)      axis=0 是按列求平均值
print("每行的平均值:",row_means)   #应输出【2,5,8】

#广播发生：形状（3,3）减去（3，）——>每一行都减去对应的平均值
centered_rows = matrix - row_means.reshape(3,1)   #把（3，）变成（3,1）
print("\n每行减去自身均值后的结果(中心化):\n",centered_rows)





#经典网格生成
#1.创建一个列向量（3,1）
col = np.array([1,2,3]).reshape(3,1)
#2.创建一个行向量（3，）
row = np.array([10,20,30])

print("列向量形状:",col.shape)   #(3,1)
print("行向量形状:",row.shape)   #(3,)
 
#广播触发：（3,1）+（3，）——>自动扩展为（3,3）+（3,3）
grid = col+row
print("\n列向量+行向量 生成的网格矩阵:\n",grid)





#会报错的（广播失败）
#尝试让（3,2）和（3，）相加
try:
    bad_matrix = np.array([[1,2],[3,4],[5,6]])
    bad_vector = np.array([10,20,30])
    result_bad = bad_matrix+bad_vector
except ValueError as e:
    print("\n广播报错的样子:",e)
    print("原因:尾部维度2和3对不上,且没有1可以拉伸")





#补充不理解的点
#1.情况1：一维数组（3，）
arr_1d = np.array([10,20,30])   
print("一维数组的形状:",arr_1d.shape)   #输出（3，）
print("一维数组的内容:",arr_1d)

#2.情况2：二维数组（3,1）——3行1列
arr_col = np.array([[10],[20],[30]])
print("\n列向量（3行1列）的形状:",arr_col.shape)   #输出（3,1）
print("列向量的内容:\n",arr_col)

#3.情况3：二维数组（1,3）——1行3列
arr_row = np.array([[10,20,30]])
print("\n行向量（1行3列）的形状:",arr_row.shape)   #输出（1,3）
print("行向量的内容:",arr_row)
