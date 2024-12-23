#
# @lc app=leetcode.cn id=LCR 069 lang=python3
# @lcpr version=30204
#
# [LCR 069] 山脉数组的峰顶索引
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right=1,len(arr)-2
        while left<right:
            mid=(left+right)//2
            if arr[mid]<arr[mid+1]:
                left=mid+1
            elif arr[mid]<arr[mid-1]:
                right=mid-1
            else:
                return mid
        return left
# @lc code=end
assert Solution().peakIndexInMountainArray([3,4,5,1])==2
assert Solution().peakIndexInMountainArray([1,3,5,4,2])==2


#
# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,10,5,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1]\n
# @lcpr case=end

# @lcpr case=start
# [24,69,100,99,79,78,67,36,26,19]\n
# @lcpr case=end

#

