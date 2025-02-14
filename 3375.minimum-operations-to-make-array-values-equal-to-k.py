#
# @lc app=leetcode.cn id=3375 lang=python3
# @lcpr version=30204
#
# [3375] 使数组的值全部为 K 的最少操作次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=set(nums)
        mi=min(s)
        if mi<k:
            return -1
        
        return len(s)-(mi==k)


# @lc code=end



#
# @lcpr case=start
# [5,2,5,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [9,7,5,3]\n1\n
# @lcpr case=end

#

