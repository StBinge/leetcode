#
# @lc app=leetcode.cn id=678 lang=python3
#
# [678] 有效的括号字符串
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        L=len(s)
        if L==0:
            return True
        min_cnt,max_cnt=0,0
        for c in s:
            if c=='(':
                min_cnt+=1
                max_cnt+=1
            elif c==')':
                min_cnt=max(0,min_cnt-1)
                max_cnt-=1
                if max_cnt<0:
                    return False
            else:
                min_cnt=max(0,min_cnt-1)
                max_cnt+=1
        return min_cnt==0

# @lc code=end

assert Solution().checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()")
assert Solution().checkValidString('(*)')
assert Solution().checkValidString('()')
assert Solution().checkValidString('(*))')