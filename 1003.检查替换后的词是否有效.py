#
# @lc app=leetcode.cn id=1003 lang=python3
#
# [1003] 检查替换后的词是否有效
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%3:
            return False
        stack=[]
        for c in s:
            stack.append(c)
            while len(stack)>2 and stack[-1]=='c':
                stack.pop()
                if stack.pop()!='b':
                    return False
                if stack.pop()!='a':
                    return False
            
        return len(stack)==0
# @lc code=end
assert Solution().isValid('aabcbabcc')
assert not Solution().isValid('aababcbccabc')
assert not Solution().isValid('abacbc')
assert not Solution().isValid('abccba')
assert not Solution().isValid('abccba')
assert Solution().isValid('abcabcababcc')
assert Solution().isValid('aabcbc')

