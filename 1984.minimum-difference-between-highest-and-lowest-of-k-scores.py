#
# @lc app=leetcode.cn id=1984 lang=python3
# @lcpr version=30204
#
# [1984] 学生分数的最小差值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        k-=1
        nums.sort()
        return min(nums[i]-nums[i-k] for i in range(k,len(nums)))
    
# @lc code=end
assert Solution().minimumDifference(nums = [9,4,1,7], k = 2)==2
assert Solution().minimumDifference(nums = [90], k = 1)==0


#
# @lcpr case=start
# [90]\n1\n
# @lcpr case=end

# @lcpr case=start
# [9,4,1,7]\n2\n
# @lcpr case=end

#

