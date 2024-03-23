#
# @lc app=leetcode.cn id=1371 lang=python3
#
# [1371] 每个元音包含偶数次的最长子字符串
#

# @lc code=start
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        masks={0:-1}
        mask=0
        vows='aeiou'
        ret=0
        for i,c in enumerate(s):
            idx=vows.find(c)
            if idx>=0:
                mask^=(1<<idx)
            if mask not in masks:
                masks[mask]=i
            else:
                ret=max(ret,i-masks[mask])
        return ret
# @lc code=end
assert Solution().findTheLongestSubstring('bcbcbc')==6
assert Solution().findTheLongestSubstring('leetcodeisgreat')==5
assert Solution().findTheLongestSubstring('eleetminicoworoep')==13
