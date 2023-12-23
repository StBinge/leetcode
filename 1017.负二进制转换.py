#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n==0:
            return '0'
        Max=0x55555555
        diff=Max-n
        N=Max^diff
        bits=bin(N)[2:]
        for i in range(len(bits)):
            if bits[i]=='0':
                continue
            return bits[i:]
# @lc code=end
assert Solution().baseNeg2(6)=='11010'
assert Solution().baseNeg2(4)=='100'
assert Solution().baseNeg2(3)=='111'
assert Solution().baseNeg2(2)=='110'
