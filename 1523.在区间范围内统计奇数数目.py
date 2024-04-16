#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        between=(high-low+1)
        if low%2:
            between+=1
        return between//2


# @lc code=end
assert Solution().countOdds(8,10)==1
assert Solution().countOdds(3,7)==3
