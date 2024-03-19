#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        if len(s)<2:
            return s
        nums=sum(c.isnumeric() for c in s)
        chars=len(s)-nums
        if abs(nums-chars)>1:
            return ''
        L=len(s)

        s=list(s)
        j=1
        alpha_first=chars>nums
        for i in range(0,L,2):
            if s[i].isalpha()!=alpha_first:
                while s[j].isalpha()!=alpha_first:
                    j+=2
                s[i],s[j]=s[j],s[i]
        return ''.join(s)
# @lc code=end

