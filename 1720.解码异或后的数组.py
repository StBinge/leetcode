#
# @lc app=leetcode.cn id=1720 lang=python3
#
# [1720] 解码异或后的数组
#
from sbw import *
# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ret=[first]
        for e in encoded:
            ret.append(ret[-1]^e)
        return ret
# @lc code=end
assert Solution().decode([1,2,3],1)==[1,0,2,1]
