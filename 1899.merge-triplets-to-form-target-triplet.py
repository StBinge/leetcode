#
# @lc app=leetcode.cn id=1899 lang=python3
# @lcpr version=30204
#
# [1899] 合并若干三元组以形成目标三元组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z=target
        A=False
        B=False
        C=False
        for a,b,c in triplets:
            if a>x or b>y or c>z:
                continue
            if a==x:
                A=True
            if b==y:
                B=True
            if c==z:
                C=True
        return A and B and C
    

# @lc code=end
assert Solution().mergeTriplets(triplets = [[3,4,5],[4,5,6]], target = [3,2,5])==False
assert Solution().mergeTriplets(triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5])


#
# @lcpr case=start
# [[2,5,3],[1,8,4],[1,7,5]]\n[2,7,5]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,4],[2,5,8]]\n[2,5,8]\n
# @lcpr case=end

# @lcpr case=start
# [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]\n[5,5,5]\n
# @lcpr case=end

# @lcpr case=start
# [[3,4,5],[4,5,6]]\n[3,2,5]\n
# @lcpr case=end

#

