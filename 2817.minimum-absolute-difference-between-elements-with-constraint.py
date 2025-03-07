#
# @lc app=leetcode.cn id=2817 lang=python3
# @lcpr version=30204
#
# [2817] 限制条件下元素之间的最小绝对差
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sl=SortedList([float('-inf'),float('inf')])
        ret=float('inf')
        for n1,n2 in zip(nums,nums[x:]):
            sl.add(n1)
            j=sl.bisect_left(n2)
            ret=min(ret,sl[j]-n2,n2-sl[j-1])
        return ret
# @lc code=end
assert Solution().minAbsoluteDifference(nums = [1,2,3,4], x = 3)==3
assert Solution().minAbsoluteDifference(nums = [5,3,2,10,15], x = 1)==1
assert Solution().minAbsoluteDifference(nums = [4,3,2,4], x = 2)==0


#
# @lcpr case=start
# [4,3,2,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,3,2,10,15]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n3\n
# @lcpr case=end

#

