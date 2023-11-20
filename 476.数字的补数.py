#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        t=num
        for i in range(5):
            t|=t>>(2**i)
        return num^t
# @lc code=end
assert Solution().findComplement(5)==2
assert Solution().findComplement(1)==0
