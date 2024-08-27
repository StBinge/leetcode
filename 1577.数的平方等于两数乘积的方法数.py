#
# @lc app=leetcode.cn id=1577 lang=python3
#
# [1577] 数的平方等于两数乘积的方法数
#
from sbw import *


# @lc code=start
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        counter1=Counter(nums1)
        counter2=Counter(nums2)
        ret=0
        def count(counter1,counter2):
            ret=0
            for n1,c1 in counter1.items():
                square1=n1*n1
                for n2,c2 in counter2.items():
                    if square1%n2==0:
                        n3=square1//n2
                        if n3==n2:
                            ret+=c1*c2*(c2-1)//2
                        elif n3>n2:
                            ret+=c1*c2*counter2[n3]
            return ret
        return count(counter1,counter2)+count(counter2,counter1)
# @lc code=end
assert Solution().numTriplets(nums1 = [7,7,8,3], nums2 = [1,2,9,7]) == 2
assert Solution().numTriplets(nums1=[1, 1], nums2=[1, 1, 1]) == 9
assert Solution().numTriplets([7, 4], [5, 2, 8, 9]) == 1
