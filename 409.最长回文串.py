#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt=Counter(s)
        ret=0
        # single=False
        for v in cnt.values():
            if v%2==0:
                ret+=v
            elif ret%2==0:
                ret+=v
            else:
                ret+=v-1
        return ret
# @lc code=end
assert Solution().longestPalindrome('abccccdd')==7
assert Solution().longestPalindrome('a')==1
assert Solution().longestPalindrome('aaaaaccc')==7
