#
# @lc app=leetcode.cn id=1299 lang=python3
#
# [1299] 将每个元素替换为右侧最大元素
#
from sbw import *
# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ma=-1
        for i in range(len(arr)-1,-1,-1):
            ma,arr[i]=max(arr[i],ma),ma
        return arr
# @lc code=end
assert Solution().replaceElements(arr = [17,18,5,4,6,1])==[18,6,6,6,1,-1]
