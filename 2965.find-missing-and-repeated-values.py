#
# @lc app=leetcode.cn id=2965 lang=python3
# @lcpr version=30204
#
# [2965] 找出缺失和重复的数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N2=len(grid)**2
        d1=sum(sum(row) for row in grid)-(1+N2)*N2//2 # repeat-miss
        d2=sum(x*x for row in grid for x in row)- N2*(N2+1)*(2*N2+1)//6 # r*r-m*m
        d3=d2//d1 # repeat+miss
        return [(d1+d3)//2,(d3-d1)//2]

# @lc code=end
assert Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]])==[9,5]
assert Solution().findMissingAndRepeatedValues([[1,3],[2,2]])==[2,4]


#
# @lcpr case=start
# [[1,3],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[9,1,7],[8,9,2],[3,4,6]]\n
# @lcpr case=end

#

