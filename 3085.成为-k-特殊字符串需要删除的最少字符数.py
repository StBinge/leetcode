#
# @lc app=leetcode.cn id=3085 lang=python3
#
# [3085] 成为 K 特殊字符串需要删除的最少字符数
#
from sbw import *
# @lc code=start
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        couter=Counter(word)
        cnt=sorted(couter.values())
        # presum=list(accumulate(sorted_values,initial=0))
        max_save=max(sum(min(cnt[i]+k,cnt[j]) for j in range(i,len(cnt))) for i in range(len(cnt)))
        return len(word)-max_save
# @lc code=end
assert Solution().minimumDeletions(word = "aaabaaa", k = 2)==1
assert Solution().minimumDeletions(word = "dabdcbdcdcd", k = 2)==2
assert Solution().minimumDeletions(word = "aabcaba", k = 0)==3
