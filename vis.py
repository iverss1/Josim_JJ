# 导入必要的库
import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
expanded_data_path = 'F:/Superconductor/JJ/expanded_data.xls'
expanded_data = pd.read_excel(expanded_data_path)

# 为数据列重命名，方便访问
expanded_data.columns = ['A', 'B', 'C']

# 创建折线图，使用B列作为横坐标，C列作为纵坐标
plt.figure(figsize=(8, 6))
plt.plot(expanded_data['B'], expanded_data['C'], marker='o')

# 设置坐标轴标签
plt.xlabel("Vbo", fontsize=12)
plt.ylabel("Iin", fontsize=12)

# 设置图表标题（可选）
plt.title("Vbo vs Iin", fontsize=14)

# 显示网格
plt.grid(True)

# 展示图表
plt.show()

