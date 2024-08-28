#
# @lc app=leetcode.cn id=1894 lang=python3
#
# [1894] 找到需要补充粉笔的学生编号
#
from sbw import *
# @lc code=start
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        presums=[0]
        for i,n in enumerate(chalk):
            presums.append(presums[i]+n)
            if presums[-1]>k:
                return i
        k%=presums[-1]
        return bisect_right(presums,k)-1

# @lc code=end
assert Solution().chalkReplacer(chalk = [3,4,1,2], k = 25)==1
assert Solution().chalkReplacer(chalk = [5,1,5], k = 22)==0
