#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left=0
        ret=0
        for c in s:
            if c=='(':
                left+=1
            else:
                if left==0:
                    ret+=1
                else:
                    left-=1
        return ret+left
# @lc code=end

assert Solution().minAddToMakeValid('(((')==3
assert Solution().minAddToMakeValid('())')==1