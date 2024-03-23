#
# @lc app=leetcode.cn id=3016 lang=python3
#
# [3016] 输入单词需要的最少按键次数 II
#
from sbw import *
# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:
        counter=Counter(word)
        L=len(counter)
        if L<=8:
            return len(word)
        cnt_sorted=sorted(counter.values(),reverse=True)
        return sum(v*(i//8 +1) for i,v in enumerate(cnt_sorted))
# @lc code=end
# assert Solution().minimumPushes('aabbccddeeffgghhiiiiii')==24
assert Solution().minimumPushes('aabbccddeeffgghhiiiiii')==24
assert Solution().minimumPushes('xyzxyzxyzxyz')==12
assert Solution().minimumPushes('abcde')==5
