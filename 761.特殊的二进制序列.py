#
# @lc app=leetcode.cn id=761 lang=python3
#
# [761] 特殊的二进制序列
#

# @lc code=start
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s)<3:
            return s
        left=cnt=0
        parts=[]
        for i in range(len(s)):
            if s[i]=='1':
                cnt+=1
            else:
                cnt-=1
                if cnt==0:
                    parts.append('1'+self.makeLargestSpecial(s[left+1:i])+'0')
                    left=i+1
        parts.sort(reverse=True)
        return ''.join(parts)
# @lc code=end

assert Solution().makeLargestSpecial('11011000')=='11100100'