#
# @lc app=leetcode.cn id=3371 lang=python3
# @lcpr version=30204
#
# [3371] 识别数组中的最大异常值
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s=sum(nums)
        cnt=Counter(nums)
        ret=float('-inf')
        # x+2y=s
        for y in nums:
            x=s-2*y
            if x in cnt and (x!=y or cnt[x]>1):
                ret=max(ret,x)
        return ret


# @lc code=end
assert Solution().getLargestOutlier([6,-31,50,-35,41,37,-42,13]) == -35
assert Solution().getLargestOutlier([1,1,1,1,1,5,5]) == 5
assert Solution().getLargestOutlier([-2, -1, -3, -6, 4]) == 4
assert Solution().getLargestOutlier([2, 3, 5, 10]) == 10


#
# @lcpr case=start
# [2,3,5,10]\n
# @lcpr case=end

# @lcpr case=start
# [-2,-1,-3,-6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1,5,5]\n
# @lcpr case=end

#
