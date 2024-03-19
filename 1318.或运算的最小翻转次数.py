#
# @lc app=leetcode.cn id=1318 lang=python3
#
# [1318] 或运算的最小翻转次数
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ret=0
        while a or b or c:
            a1=a&1
            b1=b&1
            c1=c&1
            if c1==0:
                ret+=a1+b1
            else:
                ret+=1-(a1|b1)
            a>>=1
            b>>=1
            c>>=1
        return ret
# @lc code=end
assert Solution().minFlips(1,2,3)==0
assert Solution().minFlips(2,6,5)==3
assert Solution().minFlips(4,2,7)==1
