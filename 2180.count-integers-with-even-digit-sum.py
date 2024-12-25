#
# @lc app=leetcode.cn id=2180 lang=python3
# @lcpr version=30204
#
# [2180] 统计各位数字之和为偶数的整数个数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        d=num//10
        ret=d*5-1
        for i in range(d*10,num+1):
            s=0
            while i:
                i,m=divmod(i,10)
                s+=m
            ret+= 1-(s&1)
        return ret



# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 30\n
# @lcpr case=end

#

