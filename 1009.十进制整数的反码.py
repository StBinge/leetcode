#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        high_bit=0
        for i in range(1,31):
            if n>=1<<i:
                high_bit=i
            else:
                break
        mask=1<<(high_bit+1)
        return n^(mask-1)
# @lc code=end
assert Solution().bitwiseComplement(0)==1
assert Solution().bitwiseComplement(5)==2
assert Solution().bitwiseComplement(7)==0
assert Solution().bitwiseComplement(10)==5
