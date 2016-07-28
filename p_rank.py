# coding: utf-8
'''
PageRank
1.核心思想： 权重越高(受到普遍的承认和信赖)，它的排名久越高
2.网页y的排名应该来自于所有指向这个网页的其他网页x1,x2,x3,x4,...xk的权重之和。
3.由于其他网页的权重也是未知的，需要破解这个怪圈： 假定所有的网页排名是相同的，根据
假设的初始值，算出每个网页的第一次迭代排名，迭代数次后即可收敛到排名的真实值。

问题：
1. 各个数据没有相互指向的关系。
2. 项目的目的主要是矩阵 的学习，矩阵需要大型的多对多关系。

思路：
每个网页都有权重值－不用根据搜索关键词 区分，假设有100k网页，分别编号为p1-p100000，
指向网页pi的网页有Ni个，0<N<20000［随机生成的N个数，范围是1-100000］
初始排名 都是 1/100000， 假定向量 B = (b1,b2,...bp)^T 为p个网页的排名／权重
	a11 ... a1n ... a1p
	... 		    ...
A = am1 ... amn ... amp  amn代表第m个网页所指向第n个网页的链接数，
	...   			...
	ap1 ... apn ... app
矩阵A中有p＊p个数字，B*A 得到收敛排名，迭代多次，使两次临近结果接近即视为收敛后的真实值

涉及的运算只有向量和矩阵的乘法而已。

'''
import numpy as np
a = [[2,4,7,7,6,6,9,5,6,3],  # 所有网页指向第一个网页的链接数，而不是第一个网页指向其他网页的链接数
	[2,4,7,7,6,6,9,5,6,53],
	[2,4,7,7,6,56,9,55,6,3],
	[2,4,7,57,56,6,9,55,6,3],
	[2,4,7,7,106,6,9,105,6,3],
	[2,4,7,57,216,6,9,5,6,3],
	[2,4,7,317,6,6,9,5,6,3],
	[2,4,7,317,56,6,9,5,6,3],
	[2,4,7,7,6,6,419,5,6,3],
	[2,4,57,7,416,6,9,5,6,3],
]
a1 = [[1,2,3,2],[2,4,3,3],[3,4,5,4],[5,6,5,4]]  # 依次是四网站指向1，2，3，4个网站的数
b = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1] 
b1 = [0.25,0.25,0.25,0.25]

A = np.array(a)
B = np.array(b)
c = A.dot(B)
d = A.dot(c)
e = A.dot(d)

print c 
print d 
print e








