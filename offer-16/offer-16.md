# 题目描述 

```
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

```

# 解题思路
* 考虑n为偶数 val = pow(x\*x, n //2)
* 考虑n为奇数 val = pow(x\*x, (n-1) //2) * x
* 每次迭代,n // 2 数据减少一半，考虑使用递归解决问题



## 解题代码

[数值的整数次方](offer-16.py)

 
