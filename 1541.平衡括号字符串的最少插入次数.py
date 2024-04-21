#
# @lc app=leetcode.cn id=1541 lang=python3
#
# [1541] 平衡括号字符串的最少插入次数
#


# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        left=idx=ret=0
        N=len(s)
        while idx<N:
            if s[idx]=='(':
                left+=1
                idx+=1
                continue
            if left>0:
                left-=1
            else:
                ret+=1
            if idx+1<N and s[idx+1]==')':
                idx+=2
            else:
                ret+=1
                idx+=1
        return ret+left*2


# @lc code=end
assert Solution().minInsertions(")))()))))))((()))())))()))))()))()())((()()))()(())()())()()))))))()()((()))(") == 28
assert Solution().minInsertions(")))))))") == 5
assert Solution().minInsertions("))())(") == 3
assert Solution().minInsertions("())") == 0
assert Solution().minInsertions("(()))") == 1
