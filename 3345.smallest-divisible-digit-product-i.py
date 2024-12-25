#
# @lc app=leetcode.cn id=3345 lang=python3
# @lcpr version=30204
#
# [3345] 最小可整除数位乘积 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if n%10==0:
            return n
     
        x,y=divmod(n,10)
        xx=1 if x==0 else x
        for i in range(y,10):
            if xx*i % t==0:
                return x*10+i
        return (x+1)*10



# @lc code=end
assert Solution().smallestNumber(3,2)==4
assert Solution().smallestNumber(1,2)==2
assert Solution().smallestNumber(2,1)==2
#
# @lcpr case=start
# 10\n2\n
# @lcpr case=end

# @lcpr case=start
# 15\n3\n
# @lcpr case=end

#

