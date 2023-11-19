#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        xor=(n^(n>>1))
        return (xor+1 & xor)==0
# @lc code=end

assert Solution().hasAlternatingBits(1)
assert Solution().hasAlternatingBits(0)
assert Solution().hasAlternatingBits(5)
assert Solution().hasAlternatingBits(7)==False
assert Solution().hasAlternatingBits(11)==False
assert Solution().hasAlternatingBits(4)==False