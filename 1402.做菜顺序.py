#
# @lc app=leetcode.cn id=1402 lang=python3
#
# [1402] 做菜顺序
#
from sbw import *
# @lc code=start
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        if satisfaction[0]<=0:
            return 0
        if satisfaction[-1]>=0:
            return sum(i*s for i,s in enumerate(reversed(satisfaction),1))
        presum=0
        ret=0
        for s in satisfaction:
            if s+presum<0:
                break
            presum+=s
            ret+=presum
        return ret
# @lc code=end
assert Solution().maxSatisfaction([-2,5,-1,0,3,-3])==35
assert Solution().maxSatisfaction([-5,-7,8,-2,1,3,9,5,-10,4,-5,-2,-1,-6])==260
assert Solution().maxSatisfaction([-1,-4,-5])==0
assert Solution().maxSatisfaction([4,3,2])==20
assert Solution().maxSatisfaction( [-1,-8,0,5,-9])==14
