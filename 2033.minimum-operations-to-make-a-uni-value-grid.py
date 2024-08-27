#
# @lc app=leetcode.cn id=2033 lang=python3
# @lcpr version=30204
#
# [2033] 获取单值网格的最小操作数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums=[]
        z=grid[0][0]
        for row in grid:
            for cell in row:
                if (z-cell)%x:
                    return -1
                nums.append(cell)
        nums.sort()
        median=nums[len(nums)//2]
        return sum(abs(n-median)//x for n in nums)

# @lc code=end

assert Solution().minOperations(grid = [[1,2],[3,4]], x = 2)==-1
assert Solution().minOperations(grid = [[1,5],[2,3]], x = 1)==5
assert Solution().minOperations(grid = [[2,4],[6,8]], x = 2)==4

#
# @lcpr case=start
# [[2,4],[6,8]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1,5],[2,3]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4]]\n2\n
# @lcpr case=end

#

