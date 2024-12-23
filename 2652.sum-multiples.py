#
# @lc app=leetcode.cn id=2652 lang=python3
# @lcpr version=30204
#
# [2652] 倍数求和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def getk(k):
            cnt=n//k
            return (1+cnt)*cnt//2*k
        return getk(3)+getk(5)+getk(7)-getk(15)-getk(21)-getk(35)+getk(105)


# @lc code=end



#
# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 9\n
# @lcpr case=end

#

