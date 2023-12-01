#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 重新排序得到 2 的幂
#

# @lc code=start
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s=sorted(str(n))
        l=len(s)
        Min=10**(l-1)
        Max=10**l
        x=1
        while x<Min:
            x<<=1
        while x<Max:
            if sorted(str(x))==s:
                return True
            x<<=1
        return False
# @lc code=end
assert Solution().reorderedPowerOf2(1)
assert Solution().reorderedPowerOf2(10)==False
