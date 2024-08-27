#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vows='aeiouAEIOU'
        N=len(s)
        return sum(s[i] in vows for i in range(N//2))==sum(s[i] in vows for i in range(N//2,N))
# @lc code=end
assert Solution().halvesAreAlike('book')
