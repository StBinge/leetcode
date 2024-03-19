#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        ret=cnt=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cnt+=1
                ret=max(ret,cnt)
            else:
                # ret=max(ret,cnt)
                cnt=1
        return ret
# @lc code=end
assert Solution().maxPower('cc')==2
assert Solution().maxPower('j')==1
assert Solution().maxPower('leetcode')==2
