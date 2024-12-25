#
# @lc app=leetcode.cn id=2194 lang=python3
# @lcpr version=30204
#
# [2194] Excel 表中某个范围内的单元格
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1,r1,_,c2,r2=s
        ret=[]
        for col in range(ord(c1),ord(c2)+1):
            for row in range(ord(r1),ord(r2)+1):
                ret.append(chr(col)+chr(row))
        return ret
# @lc code=end



#
# @lcpr case=start
# "K1:L2"\n
# @lcpr case=end

# @lcpr case=start
# "A1:F1"\n
# @lcpr case=end

#

