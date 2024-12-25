#
# @lc app=leetcode.cn id=2149 lang=python3
# @lcpr version=30204
#
# [2149] 按符号重排数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N=len(nums)
        ret=[0]*N
        p_idx=0
        n_idx=1
        for n in nums:
            if n>0:
                ret[p_idx]=n
                p_idx+=2
            else:
                ret[n_idx]=n
                n_idx+=2
        return ret
# @lc code=end



#
# @lcpr case=start
# [3,1,-2,-5,2,-4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1]\n
# @lcpr case=end

#

