#
# @lc app=leetcode.cn id=828 lang=python3
#
# [828] 统计子串中的唯一字符
#

# @lc code=start
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pos=[[-1] for _ in range(26)]
        for i,c in enumerate(s):
            pos[ord(c)-ord('A')].append(i)
        ret=0
        for ar in pos:
            if len(ar)==1:
                continue
            ar.append(len(s))
            for i in range(1,len(ar)-1):
                ret+=(ar[i]-ar[i-1])*(ar[i+1]-ar[i])
        return ret

# @lc code=end

