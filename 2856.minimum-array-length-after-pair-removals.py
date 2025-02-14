#
# @lc app=leetcode.cn id=2856 lang=python3
# @lcpr version=30204
#
# [2856] 删除数对后的最小数组长度
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        N=len(nums)
        mid=nums[N//2]
        mx_cnt=bisect_right(nums,mid,lo=N//2)- bisect_left(nums,mid,hi=N//2)
        if mx_cnt*2>N:
            return mx_cnt*2-N
        else:
            return N&1



# @lc code=end
assert Solution().minLengthAfterRemovals([2, 3, 4, 4, 4]) == 1
assert Solution().minLengthAfterRemovals([1000000000, 1000000000]) == 2
assert Solution().minLengthAfterRemovals([1, 1, 2, 2, 3, 3]) == 0
assert Solution().minLengthAfterRemovals([1, 2, 3, 4]) == 0


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,2,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [1000000000,1000000000]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,4,4]\n
# @lcpr case=end

#
