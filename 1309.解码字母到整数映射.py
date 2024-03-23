#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        ret=[]
        idx=len(s)-1
        orda=ord('a')-1
        while idx>=0:
            if s[idx]!='#':
                ret.append(chr(ord(s[idx])-ord('0')+orda))
            else:
                idx-=2
                code=int(s[idx:idx+2])
                ret.append(chr(code+orda))
            idx-=1
        return ''.join(reversed(ret))
# @lc code=end
assert Solution().freqAlphabets("1326#")=='acz'
assert Solution().freqAlphabets("10#11#12")=='jkab'
