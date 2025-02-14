#
# @lc app=leetcode.cn id=2779 lang=python3
# @lcpr version=30204
#
# [2779] 数组的最大美丽值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        bucks=defaultdict(int)
        for n in nums:
            bucks[n//k]+=1
        

# @lc code=end
assert Solution().maximumBeauty([12,71],10)==1


#
# @lcpr case=start
# [4,6,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n10\n
# @lcpr case=end

#

