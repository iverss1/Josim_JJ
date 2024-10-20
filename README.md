# Josim_JJ
Simulation the characteristics of Josephsen Junction using Josim. Chinese version is uploaded on [【从零开始学习VLSI设计（三）】超导器件特性仿真——约瑟夫森结（Josephsen Junction）与Josim使用](https://blog.csdn.net/iverss/article/details/143048300?spm=1001.2014.3001.5501)  

## 1.How to use
### Generate the I/V data with netlist file
Commmand `josim-cli -o jj_iv.csv jj_iv.inp -V 1`, and a `.csv` file will be generated.
### Insure the format
Commmand `python extend.py` to extend the data of first column in the `.csv` file to three columns.
### Visualize the I/V curve
Command `python vis.py`
### Fiter the voltage shock
Command `python filter.py`

**Please ensure the corresponding file direction is set before simulation and visualization.**

## 2.Results presentation
![R_35_f](https://github.com/user-attachments/assets/e92f2a87-dfe8-4d9c-b1c9-66d931fb0bd2)
![jj](https://github.com/user-attachments/assets/0d458a1d-1e5a-4f58-a41a-efaaec2df8a2)

## 3. Reference
[1][Josephson Effect](https://www.sciencedirect.com/topics/materials-science/josephson-effect)

[2][JoSIM—Superconductor SPICE Simulator](https://ieeexplore.ieee.org/document/8633946)

[3][SuperSIM: a comprehensive benchmarking framework for neural networks using superconductor Josephson devices](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=snJXnIkAAAAJ&cstart=20&pagesize=80&citation_for_view=snJXnIkAAAAJ:4OULZ7Gr8RgC)

