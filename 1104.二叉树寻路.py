#
# @lc app=leetcode.cn id=1104 lang=python3
#
# [1104] 二叉树寻路
#
from sbw import *
# @lc code=start
import math
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level=int(math.log(label,2))+1
        ret=[]        
        if level % 2==0:
            tot=2**(level-1)
            label=3*tot-label-1

        while label:
            if level %2==0:
                tot=2**(level-1)
                _label=3*tot-label-1
                ret.append(_label)
            else:
                ret.append(label)
            label//=2
            level-=1
        return ret[::-1]

# @lc code=end
assert Solution().pathInZigZagTree(label = 14)==[1,3,4,14]
assert Solution().pathInZigZagTree(label = 26)==[1,2,6,10,26]
