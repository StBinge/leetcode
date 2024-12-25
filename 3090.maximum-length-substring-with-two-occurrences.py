#
# @lc app=leetcode.cn id=3090 lang=python3
# @lcpr version=30204
#
# [3090] 每个字符最多出现两次的最长子字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt=defaultdict(int)
        left=0
        ret=0
        for i,ch in enumerate(s):
            cnt[ch]+=1
            if cnt[ch]<=2:
                continue
            ret=max(ret,i-left)
            while s[left]!=ch:
                cnt[s[left]]-=1
                left+=1
            cnt[ch]-=1
            left+=1
        return max(ret,len(s)-left)
# @lc code=end



#
# @lcpr case=start
# "bcbbbcba"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n
# @lcpr case=end

#

