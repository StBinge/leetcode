#
# @lc app=leetcode.cn id=2348 lang=python3
# @lcpr version=30204
#
# [2348] 全 0 子数组的数目
#
from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ret=0
        cnt=0
        for x in nums:
            if x==0:
                cnt+=1
                ret+=cnt
            else:
                cnt=0
        return ret


# @lc code=end
assert Solution().zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6


#
# @lcpr case=start
# [1,3,0,0,2,0,0,4]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,2,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,10,2019]\n
# @lcpr case=end

#
