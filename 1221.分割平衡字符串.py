#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l=0
        ret=0
        for c in s:
            if c=='L':
                l+=1
            else:
                l-=1
            if l==0:
                ret+=1
        return ret
# @lc code=end
assert Solution().balancedStringSplit('RLRRRLLRLL')==2
