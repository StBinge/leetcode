#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter=Counter(s1.split(' '))
        counter.update(s2.split(' '))
        ret=[]
        for k,v in counter.items():
            if v==1:
                ret.append(k)
        return ret
# @lc code=end

