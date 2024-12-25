#
# @lc app=leetcode.cn id=3101 lang=python3
# @lcpr version=30204
#
# [3101] 交替子数组计数
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        N=len(nums)
        ret=1
        cnt=1
        for i in range(1,N):
            if nums[i]==nums[i-1]:
                cnt=1
            else:
                cnt=cnt+1
            ret+=cnt
        return ret
        
# @lc code=end
assert Solution().countAlternatingSubarrays([1,0,1,0])==10
assert Solution().countAlternatingSubarrays([0,1,1,1])==5


#
# @lcpr case=start
# [0,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,0]\n
# @lcpr case=end

#

