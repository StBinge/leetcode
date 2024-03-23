#
# @lc app=leetcode.cn id=1404 lang=python3
#
# [1404] 将二进制表示减到 1 的步骤数
#

# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        L=len(s)
        ret=0
        idx=L-1
        while idx>0 and s[idx]=='0':
            ret+=1
            idx-=1
        if idx>0:
            ret+=2

        while idx>0:
            if s[idx]=='0':
                ret+=2
            else:
                ret+=1
            idx-=1
        return ret
# @lc code=end
assert Solution().numSteps('1101')==6
