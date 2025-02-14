#
# @lc app=leetcode.cn id=2560 lang=python3
# @lcpr version=30204
#
# [2560] 打家劫舍 IV
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N=len(nums)
        def check(x):
            cnt=0
            idx=0
            while idx<N:
                if nums[idx]>x:
                    idx+=1
                else:
                    cnt+=1
                    idx+=2
            return cnt>=k

        return bisect_left(range(max(nums)),True,key=check)
# @lc code=end
assert Solution().minCapability(nums = [2,7,9,3,1], k = 2)==2
assert Solution().minCapability(nums = [2,3,5,9], k = 2)==5


#
# @lcpr case=start
# [2,3,5,9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n2\n
# @lcpr case=end

#

