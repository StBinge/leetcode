#
# @lc app=leetcode.cn id=2148 lang=python3
# @lcpr version=30204
#
# [2148] 元素计数
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countElements(self, nums: List[int]) -> int:
        mi=float('inf')
        mx=float('-inf')
        mi_cnt=mx_cnt=0
        for n in nums:
            if n<mi:
                mi=n
                mi_cnt=1
            elif n==mi:
                mi_cnt+=1
            
            if n>mx:
                mx=n
                mx_cnt=1
            elif mx==n:
                mx_cnt+=1
        
        return max(len(nums)-mi_cnt-mx_cnt,0)
# @lc code=end



#
# @lcpr case=start
# [11,7,2,15]\n
# @lcpr case=end

# @lcpr case=start
# [-3,3,3,90]\n
# @lcpr case=end

#

