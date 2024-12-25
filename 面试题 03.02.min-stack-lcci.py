#
# @lc app=leetcode.cn id=面试题 03.02 lang=python3
# @lcpr version=30204
#
# [面试题 03.02] 栈的最小值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals=[]
        self.mins=[float('inf')]

    def push(self, x: int) -> None:
        self.vals.append(x)
        self.mins.append(min(x,self.mins[-1]))

    def pop(self) -> None:
        self.mins.pop()
        return self.vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end



