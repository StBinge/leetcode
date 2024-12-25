#
# @lc app=leetcode.cn id=2870 lang=python3
# @lcpr version=30204
#
# [2870] 使数组为空的最少操作次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        ret=0
        for v in cnt.values():
            if v<2:
                return -1
            ret+=(v-1)//3+1
        return ret
# @lc code=end



#
# @lcpr case=start
# [2,3,3,2,2,4,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,2,2,3,3]\n
# @lcpr case=end

#

