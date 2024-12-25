#
# @lc app=leetcode.cn id=2843 lang=python3
# @lcpr version=30204
#
# [2843] 统计对称整数的数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def count(n):
            if n<=1000:
                return min(9,n//11)
            ret=9
            h,m=divmod(n,100)
            for i in range(10,h):
                x,y=divmod(i,10)
                z=x+y
                ret+=10-abs(z-9)
            x,y=divmod(h,10)
            z=x+y
            for i in range(max(0,z-9),min(z,9)+1):
                if i*10+z-i<=m:
                    ret+=1
                else:
                    break
            return ret
        
        return count(high)-count(low-1)



# @lc code=end

assert Solution().countSymmetricIntegers(100,7324)==456
assert Solution().countSymmetricIntegers(1200,1230)==4
assert Solution().countSymmetricIntegers(1,100)==9

#
# @lcpr case=start
# 1\n100\n
# @lcpr case=end

# @lcpr case=start
# 1200\n1230\n
# @lcpr case=end

#

