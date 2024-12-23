#
# @lc app=leetcode.cn id=3270 lang=python3
# @lcpr version=30204
#
# [3270] 求出数字答案
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ret=0
        for i in (1000,100,10,1):
            m1,num1=divmod(num1,i)
            m2,num2=divmod(num2,i)
            m3,num3=divmod(num3,i)
            ret+=i*min(m1,m2,m3)
        return ret
# @lc code=end
assert Solution().generateKey(987,879,798)==777
assert Solution().generateKey(num1 = 1, num2 = 10, num3 = 1000)==0


#
# @lcpr case=start
# 1\n10\n1000\n
# @lcpr case=end

# @lcpr case=start
# 987\n879\n798\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n3\n
# @lcpr case=end

#

