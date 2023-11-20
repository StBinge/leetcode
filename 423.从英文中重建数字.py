#
# @lc app=leetcode.cn id=423 lang=python3
#
# [423] 从英文中重建数字
#

# @lc code=start
from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        count=Counter(s)
        ret=[0]*10
        ret[0]=count.get('z',0)
        ret[2]=count.get('w',0)
        ret[4]=count.get('u',0)
        ret[6]=count.get('x',0)
        ret[8]=count.get('g',0)
        ret[3]=count.get('h',0)-ret[8]
        ret[7]=count.get('s',0)-ret[6]
        ret[5]=count.get('v',0)-ret[7]
        ret[1]=count.get('o',0)-ret[0]-ret[2]-ret[4]
        ret[9]=count.get('i',0)-ret[5]-ret[6]-ret[8]
        return ''.join([str(i)*ret[i] for i in range(10) if ret[i]>0])
# @lc code=end

assert Solution().originalDigits("nnei")=='9'
assert Solution().originalDigits("esnve")=='7'
assert Solution().originalDigits("owoztneoer")=='012'
assert Solution().originalDigits("fviefuro")=='45'