#
# @lc app=leetcode.cn id=2068 lang=python3
# @lcpr version=30204
#
# [2068] 检查两个字符串是否几乎相等
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt=[0]*26
        orda=ord('a')
        for ch in word1:
            cnt[ord(ch)-orda]+=1
        for ch in word2:
            cnt[ord(ch)-orda]-=1
        
        return all(abs(c)<4 for c in cnt)
# @lc code=end



#
# @lcpr case=start
# "aaaa"\n"bccb"\n
# @lcpr case=end

# @lcpr case=start
# "abcdeef"\n"abaaacc"\n
# @lcpr case=end

# @lcpr case=start
# "cccddabba"\n"babababab"\n
# @lcpr case=end

#

