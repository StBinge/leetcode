#
# @lc app=leetcode.cn id=2516 lang=python3
# @lcpr version=30204
#
# [2516] 每种字符至少取 K 个
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        N = len(s)
        if N < k * 3:
            return -1
        cnt=Counter(s)
        if any(cnt[c]<k for c in 'abc'):
            return -1
        
        mx=left=0
        for right,ch in enumerate(s):
            cnt[ch]-=1
            while cnt[ch]<k:
                cnt[s[left]]+=1
                left+=1
            mx=max(mx,right-left+1)
        return N-mx
         

# @lc code=end
assert Solution().takeCharacters(s="aabbccca", k=2) == 6
assert Solution().takeCharacters(s="aabaaaacaabc", k=2) == 8
assert Solution().takeCharacters(s="aabaaaacaabc", k=0) == 0
assert Solution().takeCharacters(s="caaa", k=1) == -1
assert Solution().takeCharacters(s="a", k=1) == -1


#
# @lcpr case=start
# "aabaaaacaabc"\n2\n
# @lcpr case=end

# @lcpr case=start
# "a"\n1\n
# @lcpr case=end

#
