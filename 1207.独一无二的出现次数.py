#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#
from sbw import *
# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=Counter(arr)
        s=set()
        for v in counter.values():
            if v in s:
                return False
            s.add(v)
        return True
# @lc code=end
assert Solution().uniqueOccurrences([1,2])==False
assert Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
