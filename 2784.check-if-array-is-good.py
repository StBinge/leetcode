#
# @lc app=leetcode.cn id=2784 lang=python3
# @lcpr version=30204
#
# [2784] 检查数组是否是好的
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        N=len(nums)
        cnt=[0]*N
        for n in nums:
            if n>(N-1):
                return False
            cnt[n]+=1
        if cnt[-1]!=2:
            return False
        return all(cnt[i]==1 for i in range(1,N-1))
# @lc code=end
assert Solution().isGood([1, 3, 3, 2])


#
# @lcpr case=start
# [2, 1, 3]\n
# @lcpr case=end

# @lcpr case=start
# [1, 3, 3, 2]\n
# @lcpr case=end

# @lcpr case=start
# [1, 1]\n
# @lcpr case=end

# @lcpr case=start
# [3, 4, 4, 1, 2, 1]\n
# @lcpr case=end

#

