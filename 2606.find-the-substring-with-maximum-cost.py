#
# @lc app=leetcode.cn id=2606 lang=python3
# @lcpr version=30204
#
# [2606] 找到最大开销的子字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        score={chr(ord('a')+i):i+1 for i in range(26)}
        score.update({ch:v for ch,v in zip(chars,vals)})
        ss=0
        ret=0
        for ch in s:
            v=score[ch]
            ss=max(ss+v,0)
            ret=max(ss,ret)
        return ret
# @lc code=end



#
# @lcpr case=start
# "adaa"\n"d"\n[-1000]\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n[-1,-1,-1]\n
# @lcpr case=end

#

