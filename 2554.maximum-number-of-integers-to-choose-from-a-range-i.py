#
# @lc app=leetcode.cn id=2554 lang=python3
# @lcpr version=30204
#
# [2554] 从一个范围内选择最多整数 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ret=0
        banned=set(banned)
        for i in range(1,n+1):
            if i in banned:
                continue
            maxSum-=i
            if maxSum<0:
                break
            ret+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,6,5]\n5\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7]\n8\n1\n
# @lcpr case=end

# @lcpr case=start
# [11]\n7\n50\n
# @lcpr case=end

#

