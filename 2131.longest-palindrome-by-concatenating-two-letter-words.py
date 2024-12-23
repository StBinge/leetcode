#
# @lc app=leetcode.cn id=2131 lang=python3
# @lcpr version=30204
#
# [2131] 连接两字母单词得到的最长回文串
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ret=0
        mid=False
        counter=Counter(words)
        for word,cnt in counter.items():
            rev=word[::-1]
            if rev==word:
                if cnt&1:
                    mid=True
                ret+=cnt//2*2*2
            elif word>rev:
                c=min(cnt,counter[rev])
                ret+=4*c
        return ret+2*mid




# @lc code=end



#
# @lcpr case=start
# ["lc","cl","gg"]\n
# @lcpr case=end

# @lcpr case=start
# ["ab","ty","yt","lc","cl","ab"]\n
# @lcpr case=end

# @lcpr case=start
# ["cc","ll","xx"]\n
# @lcpr case=end

#

