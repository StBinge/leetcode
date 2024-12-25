#
# @lc app=leetcode.cn id=LCR 032 lang=python3
# @lcpr version=30204
#
# [LCR 032] 有效的字母异位词
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        cnt=defaultdict(int)
        same=True
        for x,y in zip(s,t):
            if x!=y:
                same=False
            cnt[x]+=1
            cnt[y]-=1
        return not same and all(v==0 for v in cnt.values())
# @lc code=end
assert Solution().isAnagram('ab','bae')==False


#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

#

