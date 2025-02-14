#
# @lc app=leetcode.cn id=3201 lang=python3
# @lcpr version=30204
#
# [3201] 找出有效子序列的最大长度 I
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # f0 = f1 = 0
        t=odd = even = 0
        pre=nums[0]+1
        for n in nums:
            t+=(pre+n)&1
            if n & 1 == 0:
                odd += 1
            else:
                even += 1
            pre=n
        return max(t, odd, even)


# @lc code=end
assert Solution().maximumLength([1, 2, 1, 1, 2, 1, 2]) == 6
assert Solution().maximumLength([4, 2, 6]) == 3
assert Solution().maximumLength([1, 3]) == 2
assert Solution().maximumLength([1, 2, 3, 4]) == 4


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#
