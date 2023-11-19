#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#
from typing import List
# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ret=0
        NG=len(g)
        NS=len(s)
        gi=NG-1
        si=NS-1
        while gi>=0 and si >=0:
            if s[si]>=g[gi]:
                si-=1
                gi-=1
                ret+=1
            elif s[si]<g[gi]:
                gi-=1
        return ret
# @lc code=end
g = [1,2,3]
s = [1,1]
assert Solution().findContentChildren(g,s)==1

g = [1,2]
s = [1,2,3]
assert Solution().findContentChildren(g,s)==2
