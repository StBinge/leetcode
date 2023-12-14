#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#
from typing import List
# @lc code=start
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        cnt={}
        for word in words:
            odd_mask=''.join(sorted(word[::2]))
            even_mask=''.join(sorted(word[1::2]))
            h=hash((odd_mask,even_mask))
            cnt[h]=cnt.get(h,0)+1
        return len(cnt)
# @lc code=end
words = ["abc","acb","bac","bca","cab","cba"]
assert Solution().numSpecialEquivGroups(words)==3

words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
assert Solution().numSpecialEquivGroups(words)==3
