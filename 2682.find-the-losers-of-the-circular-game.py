#
# @lc app=leetcode.cn id=2682 lang=python3
# @lcpr version=30204
#
# [2682] 找出转圈游戏输家
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        catched=[False]*n
        cur=0
        i=1
        while catched[cur]==False:
            catched[cur]=True
            cur=(cur+k*i)%n
            i+=1
        return [i+1 for i in range(n) if catched[i]==False]
# @lc code=end



#
# @lcpr case=start
# 5\n2\n
# @lcpr case=end

# @lcpr case=start
# 4\n4\n
# @lcpr case=end

#

