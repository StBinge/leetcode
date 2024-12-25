#
# @lc app=leetcode.cn id=2587 lang=python3
# @lcpr version=30204
#
# [2587] 重排数组以得到最大前缀分数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ret=0
        s=0
        for n in nums:
            s+=n
            if s>0:
                ret+=1
            else:
                break
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,-1,0,1,-3,3,-3]\n
# @lcpr case=end

# @lcpr case=start
# [-2,-3,0]\n
# @lcpr case=end

#

