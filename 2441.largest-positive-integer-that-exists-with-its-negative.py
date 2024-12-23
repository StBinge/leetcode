#
# @lc app=leetcode.cn id=2441 lang=python3
# @lcpr version=30204
#
# [2441] 与对应负数同时存在的最大正整数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen=set()
        ret=-1
        for n in nums:
            if -n in seen:
                ret=max(ret,abs(n))
            seen.add(n)
        return ret
# @lc code=end



#
# @lcpr case=start
# [-1,2,-3,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,10,6,7,-7,1]\n
# @lcpr case=end

# @lcpr case=start
# [-10,8,6,7,-2,-3]\n
# @lcpr case=end

#

