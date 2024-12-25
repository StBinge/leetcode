#
# @lc app=leetcode.cn id=2928 lang=python3
# @lcpr version=30204
#
# [2928] 给小朋友们分糖果 I
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def c2(x):
            return (x+1)*(x+2)//2 if x+2>1 else 0
        tot=c2(n)
        l1=3*c2(n-limit-1)
        l2=3*c2(n-2*limit-2)
        l3=c2(n-3*limit-3)
        return tot-(l1-l2+l3)



# @lc code=end
assert Solution().distributeCandies(2,1) == 3
assert Solution().distributeCandies(3, 3) == 10
assert Solution().distributeCandies(5, 2) == 3


#
# @lcpr case=start
# 5\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n
# @lcpr case=end

#
