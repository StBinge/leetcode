#
# @lc app=leetcode.cn id=LCR 041 lang=python3
# @lcpr version=30204
#
# [LCR 041] 数据流中的移动平均值
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.mx_size=size
        self.vals=deque(maxlen=self.mx_size)
        self.s=0

    def next(self, val: int) -> float:
        if len(self.vals)==self.mx_size:
            self.s-=self.vals.popleft()
        self.s+=val
        self.vals.append(val)    
        return self.s/len(self.vals)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end



#
# @lcpr case=start
# ["MovingAverage", "next", "next", "next"\n[[3], [1], [10], [3], [5]]\n
# @lcpr case=end

#

