#
# @lc app=leetcode.cn id=1952 lang=python3
# @lcpr version=30204
#
# [1952] 三除数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isThree(self, n: int) -> bool:
        for i in range(2,n):
            if n%i==0:
                if i*i==n:
                    return True
                else:
                    return False
            if i*i>n:
                return False
        return False
# @lc code=end
assert Solution().isThree(12)==False
assert Solution().isThree(4)==True
assert Solution().isThree(1)==False
assert Solution().isThree(2)==False


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

