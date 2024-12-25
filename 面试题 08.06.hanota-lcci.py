#
# @lc app=leetcode.cn id=面试题 08.06 lang=python3
# @lcpr version=30204
#
# [面试题 08.06] 汉诺塔问题
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        N=len(A)
        def move(n,a,b,c):
            if n==1:
                c.append(a.pop())
                return
            move(n-1,a,c,b)
            c.append(a.pop())
            move(n-1,b,a,c)
        
        move(N,A,B,C)
# @lc code=end



#
# @lcpr case=start
# [2, 1, 0]\n[]\n[]\n
# @lcpr case=end

# @lcpr case=start
# [1, 0]\n[]\n[]\n
# @lcpr case=end

#

