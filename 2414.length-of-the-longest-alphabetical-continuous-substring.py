#
# @lc app=leetcode.cn id=2414 lang=python3
# @lcpr version=30204
#
# [2414] 最长的字母序连续子字符串的长度
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        cnt=1
        ret=0
        for x,y in pairwise(map(ord,s)):
            if x+1==y:
                cnt+=1
            else:
                ret=max(ret,cnt)
                cnt=1
        return max(ret,cnt)
# @lc code=end



#
# @lcpr case=start
# "abacaba"\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n
# @lcpr case=end

#

