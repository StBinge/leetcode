#
# @lc app=leetcode.cn id=LCR 139 lang=python3
# @lcpr version=30204
#
# [LCR 139] 训练计划 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        left,right=0,len(actions)-1
        while left<right:
            while left<right and actions[left]&1:
                left+=1
            while right>left and actions[right]&1==0:
                right-=1
            if left<right:
                actions[left],actions[right]=actions[right],actions[left]
                left+=1
                right-=1
        return actions
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

