#
# @lc app=leetcode.cn id=LCR 186 lang=python3
# @lcpr version=30204
#
# [LCR 186] 文物朝代判断
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        places.sort()
        zero=0
        for i in range(4):
            if places[i]==0:
                zero+=1
            elif places[i]==places[i+1]:
                return False
        return places[-1]-places[zero]<5
# @lc code=end
assert Solution().checkDynasty([0,0,6,7,9])
assert Solution().checkDynasty([0,0,2,2,5])==False


#
# @lcpr case=start
# [0, 6, 9, 0, 7]\n
# @lcpr case=end

# @lcpr case=start
# [7, 8, 9, 10, 11]\n
# @lcpr case=end

#

