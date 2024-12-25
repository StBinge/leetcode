#
# @lc app=leetcode.cn id=2145 lang=python3
# @lcpr version=30204
#
# [2145] 统计隐藏数组数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mi=lower
        mx=upper
        cur=0
        for i in range(len(differences)):
            cur+=differences[i]
            mi=max(mi,lower-cur)
            mx=min(mx,upper-cur)
            if mi>mx:
                return 0
        return mx-mi+1

# @lc code=end
assert Solution().numberOfArrays(differences = [1,-3,4], lower = 1, upper = 6)==2


#
# @lcpr case=start
# [1,-3,4]\n1\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,-4,5,1,-2]\n-4\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,-7,2]\n3\n6\n
# @lcpr case=end

#

