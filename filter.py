import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def sliding_filter(data, window_size):
    """
    Perform a simple moving average (sliding window) filter on the data.
    
    :param data: Input data (1D array)
    :param window_size: The size of the window to use for the moving average
    :return: Filtered data as a numpy array
    """
    filtered_data = np.zeros(len(data))  # Initialize the array for filtered data
    half_window = window_size // 2  # Calculate half window size
    
    for i in range(len(data)):
        # Define the start and end indices for the window
        start_index = max(0, i - half_window)
        end_index = min(len(data), i + half_window + 1)
        # Calculate the mean within the window and assign to the filtered data
        filtered_data[i] = np.mean(data[start_index:end_index])
    
    return filtered_data

# 读取展开的Excel文件
file_path = 'F:/Superconductor/JJ/expanded_data.xls'  # 将路径替换为您的实际文件路径
data = pd.read_excel(file_path, engine='xlrd')

# 假设数据已经展开为三列，命名为A, B, C
data.columns = ['A', 'B', 'C']

# 移动平均滤波器
window_size = 10  # 设置窗口大小，决定滤波器的平滑程度
data['B_filtered_custom'] = sliding_filter(data['B'], window_size)

# 创建图像：原始数据和滤波后的数据
plt.figure(figsize=(8, 6))

# 原始数据绘制
plt.plot(data['B'], data['C'], color='blue', label='Original Data')

# 滤波后的数据绘制
plt.plot(data['B_filtered_custom'],  data['C'], color='red', label='Filtered Data')

# 设置坐标轴标签
plt.xlabel("Voltage (V)", fontsize=12)
plt.ylabel("Current (I)", fontsize=12)

# 添加标题和图例
plt.title(f"Voltage vs Current (Original vs Filtered, Window Size = {window_size})", fontsize=14)
plt.legend()

# 显示网格
plt.grid(True)

# 添加图像标题
plt.suptitle('After applying Moving Average Filter', fontsize=16)

# 显示图像
plt.show()