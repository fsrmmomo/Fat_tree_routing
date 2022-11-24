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
使用最短路计算每对节点的路由方案，以及每个方案对应的源和目的ip组  
运行gen_topo.py生成对应的topo文件  
然后运行sp.py得到计算结果输出到data/sp_result  
### ecmp 方案
使用k最短路计算每对节点的所有最短路由方案，以及每个方案对应的源和目的ip组  
该拓扑比较特殊，同组的有两条等效路径，不同组有四条等效路径，并且都是平分的关系，因此直接使用该结论对流进行拆分  

运行gen_topo.py生成对应的topo文件  
然后运行ecmp.py得到计算结果输出到data/ecmp_result  