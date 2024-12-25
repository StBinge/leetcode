#
# @lc app=leetcode.cn id=面试题 16.11 lang=python3
# @lcpr version=30204
#
# [面试题 16.11] 跳水板
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k==0:
            return []
        if shorter==longer:
            return [k*shorter]
        ret=[]
        for i in range(k+1):
            ret.append(i*longer+(k-i)*shorter)
        return ret
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

#

