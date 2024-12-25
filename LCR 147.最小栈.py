#
# @lc app=leetcode.cn id=LCR 147 lang=python3
# @lcpr version=30204
#
# [LCR 147] 最小栈
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.counter=defaultdict(int)
        self.stack=[]
        self.small=[float('inf')]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.small.append(min(x,self.small[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.small.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.small[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
obj=MinStack()
ops=["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
args=[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
ret='[null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]'
test_obj(obj,ops,args,ret)


obj=MinStack()
ops=["MinStack","push","push","push","getMin","pop","top","getMin"]
args=[[],[-2],[0],[-3],[],[],[],[]]
ret='[null,null,null,null,-3,null,0,-2]'
test_obj(obj,ops,args,ret)

#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#

