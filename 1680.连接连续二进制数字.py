#
# @lc app=leetcode.cn id=1680 lang=python3
#
# [1680] 连接连续二进制数字
#

# @lc code=start
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        shift=0
        ret=0
        Mod=10**9+7
        for i in range(1,n+1):
            if i & (i-1)==0:
                shift+=1
            ret=(ret<<shift)+i
            ret%=Mod
        return ret
# @lc code=end
assert Solution().concatenatedBinary(12)==505379714
