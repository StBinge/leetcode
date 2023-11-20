#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre,cur=0,1
        ret=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cur+=1
                continue            
            ret+=min(pre,cur)
            pre=cur
            cur=1
        ret+=min(pre,cur)
        return ret
# @lc code=end
assert Solution().countBinarySubstrings('00110011')==6
assert Solution().countBinarySubstrings('10101')==4
