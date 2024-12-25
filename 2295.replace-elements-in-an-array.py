#
# @lc app=leetcode.cn id=2295 lang=python3
# @lcpr version=30204
#
# [2295] 替换数组中的元素
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        maps={}
        for x,y in reversed(operations):
            maps[x]=maps.get(y,y)
        for i in range(len(nums)):
            nums[i]=maps.get(nums[i],nums[i])
        return nums
# @lc code=end
assert Solution().arrayChange([1,2],[[1,3],[2,1],[3,2]])==[2,1]
assert Solution().arrayChange(nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]])==[3,2,7,1]


#
# @lcpr case=start
# [1,2,4,6]\n[[1,3],[4,7],[6,1]]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[[1,3],[2,1],[3,2]]\n
# @lcpr case=end

#

