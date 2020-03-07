# 题目描述 

```

请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```

# 解题思路
* 使用双端队列deque操作队列，双端队列的pop popleft 和索引操作时间复杂度都是1
* 使用max_queue 存储最大值,最大值存储于index=0的位置
* push操作 的时候，对比max_queue的最后一位数据，如果小于当前值，执行pop操作
* pop操作 对比当前pop值，是否是max_queue[0],如果是,执行popleft

# 解题代码

[队列最大值](offer-59.1.py)
