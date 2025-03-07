#
# @lc app=leetcode.cn id=3296 lang=python3
# @lcpr version=30204
#
# [3296] 移山所需的最少秒数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        mx=max(workerTimes)
        right=(mountainHeight+1)*mountainHeight//2*mx
        def check(x):
            ret=0
            for t in workerTimes:
                h=math.floor(math.sqrt(0.25+2*x/t)-0.5)
                ret+=h
            return ret>=mountainHeight
        
        return bisect_left(range(right),True,1,key=check)


# @lc code=end
assert Solution().minNumberOfSeconds(mountainHeight = 5, workerTimes = [1])==15
assert Solution().minNumberOfSeconds( mountainHeight = 10, workerTimes = [3,2,2,4])==12
assert Solution().minNumberOfSeconds(4,(2,1,1))==3


#
# @lcpr case=start
# 4\n[2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[3,2,2,4]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[1]\n
# @lcpr case=end

#

