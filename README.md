# Fat_tree_routing

该项目用于生成Fat Tree网络拓扑的相关路由
## 拓扑概况
该Fat Tree共有20个节点，32条边  
core节点4个  
merge节点8个  
access节点8个  

## 算法使用
主要有如下几个步骤：

1. 使用gen_topo.py生成对应的topo文件
2. base.py使用该topo文件生成对应的图结构
3. 计算路由方案
> sp方案
> emcp方案

### sp 方案
使用最短路计算每对节点的路由方案

