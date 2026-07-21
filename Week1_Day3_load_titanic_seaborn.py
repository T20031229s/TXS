import seaborn as sns
import pandas as pd

# 从Seaborn加载内置的泰坦尼克号数据集
titanic = sns.load_dataset('titanic')

# 查看数据前几行
print(titanic.head())

# 保存为本地CSV文件
titanic.to_csv('train.csv', index=False)
print("数据已保存到本地 train.csv")