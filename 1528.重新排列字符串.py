#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#
from sbw import *
# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ret=list(s)
        for i in range(len(indices)):
           while i!=indices[i]:
               ret[i],ret[indices[i]]=ret[indices[i]],ret[i]
               indices[indices[i]],indices[i]=indices[i],indices[indices[i]]
        return ''.join(ret)

# @lc code=end

assert Solution().restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3])=='leetcode'