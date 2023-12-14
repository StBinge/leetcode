#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ret=list(s)
        l,r=0,len(s)-1
        while l<r:
            while l<r and not s[l].isalpha():
                l+=1
            while l<r and not s[r].isalpha():
                r-=1
            ret[l],ret[r]=ret[r],ret[l]
            l+=1
            r-=1
        return ''.join(ret)
# @lc code=end

s = "Test1ng-Leet=code-Q!"
ret="Qedo1ct-eeLg=ntse-T!"
assert Solution().reverseOnlyLetters(s)==ret