# 导入必要的库
import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件，使用openpyxl引擎来读取.xlsx文件
file_path = 'F:/Superconductor/JJ/jj_iv.xlsx'  # 将路径替换为您的实际文件路径
data = pd.read_excel(file_path, engine='openpyxl')

# 展开数据，将一列中的数据分割为三列
# 假设数据最初全部在一列中，且数据之间以空格分隔
expanded_data = data.iloc[:, 0].str.split(expand=True)

# 为展开后的三列命名
expanded_data.columns = ['A', 'B', 'C']

# 保存展开后的数据为新的Excel文件
expanded_data.to_excel('expanded_data.xls', index=False)