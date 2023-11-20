#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k-=1
        ret=0
        while k>0:
            k&=k-1
            ret^=1
        return ret
# @lc code=end

assert Solution().kthGrammar(1,1)==0
assert Solution().kthGrammar(2,1)==0
assert Solution().kthGrammar(2,2)==1