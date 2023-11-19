#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from typing import List
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        positions={}
        for i,ch in enumerate(s):
            positions[ch]=i
        start=0
        end=0
        ret=[]
        L=len(s)
        for i in range(L):
            end=max(end,positions[s[i]])
            if i==end:
                ret.append(end-start+1)
                start=end+1
        return ret
# @lc code=end
assert Solution().partitionLabels("caedbdedda")==[1,9]

s = "ababcbacadefegdehijhklij"
assert Solution().partitionLabels(s)==[9,7,8]
s = "eccbbbbdec"
assert Solution().partitionLabels(s)==[10]

