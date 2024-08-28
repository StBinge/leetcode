#
# @lc app=leetcode.cn id=1998 lang=python3
# @lcpr version=30204
#
# [1998] 数组的最大公因数排序
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        N = len(nums)
        Mx=max(nums)
        p = list(range(Mx+1))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            x, y = find(x), find(y)
            p[x] = y

        group=[[] for _ in range(Mx+1)]
        for i in range(2,Mx+1):
            if not group[i]:
                for j in range(i,Mx+1,i):
                    group[j].append(i)

        for i,n in enumerate(nums):
            for x in group[n]:
                union(n,x)

        for x,y in zip(nums,sorted(nums)):
            if find(x) != find(y):
                return False
        return True


# @lc code=end
assert Solution().gcdSort( [10,5,9,3,15])
assert not Solution().gcdSort([5,2,6,2])
assert Solution().gcdSort([7, 21, 3])


#
# @lcpr case=start
# [7,21,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,2,6,2]\n
# @lcpr case=end

# @lcpr case=start
# [10,5,9,3,15]\n
# @lcpr case=end

#
