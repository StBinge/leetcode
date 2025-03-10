#
# @lc app=leetcode.cn id=2730 lang=python3
# @lcpr version=30204
#
# [2730] 找到最长的半重复子字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        same=0
        ret=0
        left=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                same+=1
                if same==2:
                    ret=max(i-left,ret)
                while same==2:
                    if s[left]==s[left+1]:
                        same-=1
                    left+=1
        return max(ret,len(s)-left)

# @lc code=end
assert Solution().longestSemiRepetitiveSubstring('1111111')==2
assert Solution().longestSemiRepetitiveSubstring('5494')==4
assert Solution().longestSemiRepetitiveSubstring('52233')==4


#
# @lcpr case=start
# "52233"\n
# @lcpr case=end

# @lcpr case=start
# "5494"\n
# @lcpr case=end

# @lcpr case=start
# "1111111"\n
# @lcpr case=end

#

