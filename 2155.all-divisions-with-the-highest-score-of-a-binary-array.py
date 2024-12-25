#
# @lc app=leetcode.cn id=2155 lang=python3
# @lcpr version=30204
#
# [2155] 分组得分最高的所有下标
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ret=[0]
        mx=0
        cur=0
        for i,n in enumerate(nums):
            if n==1:
                cur-=1
                continue
            cur+=1
            if cur>mx:
                ret=[i+1]
                mx=cur
            elif cur==mx:
                ret.append(i+1)
        return ret

# @lc code=end



#
# @lcpr case=start
# [0,0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

