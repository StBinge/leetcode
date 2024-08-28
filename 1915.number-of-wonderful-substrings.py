#
# @lc app=leetcode.cn id=1915 lang=python3
# @lcpr version=30204
#
# [1915] 最美子字符串的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask=0
        cnt=defaultdict(int)
        cnt[0]=1
        ret=0
        for ch in word:
            code=ord(ch)-ord('a')
            mask^=1<<code
            ret+=cnt[mask]
            for i in range(10):
                ret+=cnt[mask ^ 1<<i]
            cnt[mask]+=1
        return ret
# @lc code=end
assert Solution().wonderfulSubstrings('he')==2
assert Solution().wonderfulSubstrings('aabb')==9
assert Solution().wonderfulSubstrings('aba')==4


#
# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n
# @lcpr case=end

# @lcpr case=start
# "he"\n
# @lcpr case=end

#

