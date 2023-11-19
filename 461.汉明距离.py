#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret=0
        z=x^y
        while z>0:
            z=z&(z-1)
            ret+=1
        return ret
# @lc code=end
assert Solution().hammingDistance(1,4)==2
assert Solution().hammingDistance(3,1)==1
