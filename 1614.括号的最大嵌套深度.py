#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        ret=0
        cur=0
        for c in s:
            if c=='(':
                cur+=1
            elif c==')':
                ret=max(ret,cur)
                cur-=1
        return ret
# @lc code=end

