#
# @lc app=leetcode.cn id=2419 lang=python3
# @lcpr version=30204
#
# [2419] 按位与最大的最长子数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx=0
        cnt=0
        ret=0
        for n in nums:
            if n==mx:
                cnt+=1
            elif n>mx:
                mx=n
                cnt=1
                ret=0
            else:
                ret=max(ret,cnt)
                cnt=0
        return max(ret,cnt)
# @lc code=end
assert Solution().longestSubarray([323376, 323376, 323376, 323376, 323376, 323376, 323376, 75940, 323376, 323377, 323377])==2


#
# @lcpr case=start
# [1,2,3,3,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

#

