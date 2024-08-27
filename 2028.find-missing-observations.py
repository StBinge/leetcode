#
# @lc app=leetcode.cn id=2028 lang=python3
# @lcpr version=30204
#
# [2028] 找出缺失的观测数据
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s1=sum(rolls)
        s=mean*(n+len(rolls))
        s2=s-s1
        if s2<n or s2>n*6:
            return []
        avg=s2//n
        ret=[avg]*n
        for i in range(s2%n):
            ret[i]+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [3,2,4,3]\n4\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,5,6]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n6\n4\n
# @lcpr case=end

# @lcpr case=start
# [1]\n3\n1\n
# @lcpr case=end

#

