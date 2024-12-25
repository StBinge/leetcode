#
# @lc app=leetcode.cn id=LCR 006 lang=python3
# @lcpr version=30204
#
# [LCR 006] 两数之和 II - 输入有序数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while left<right:
            s=numbers[left]+numbers[right]
            if s==target:
                return [left,right]
            elif s<target:
                left+=1
            else:
                right-=1
        
# @lc code=end



#
# @lcpr case=start
# [1,2,4,6,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#

