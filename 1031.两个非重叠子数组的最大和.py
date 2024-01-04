#
# @lc app=leetcode.cn id=1031 lang=python3
#
# [1031] 两个非重叠子数组的最大和
#
from sbw import *
# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def slide(len1,len2):
            L=len(nums)
            cur=sum1=sum(nums[:len1])
            sum2=sum(nums[len1:len1+len2])
            ret=sum1+sum2

            for i in range(len1+len2,L):
                sum2+=nums[i]-nums[i-len2]
                cur+=nums[i-len2]-nums[i-len1-len2]
                sum1=max(sum1,cur)
                ret=max(ret,sum1+sum2)
            return ret
        return max(slide(firstLen,secondLen),slide(secondLen,firstLen))
# @lc code=end
assert Solution().maxSumTwoNoOverlap([87,42,40,86,93,4,18,28,59,30,6,51,99,46,40,24,19,98,40,41],1,10)==586
assert Solution().maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4,3)==31

assert Solution().maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0],3,2)==29

nums = [0,6,5,2,2,5,1,9,4]
firstLen = 1
secondLen = 2
assert Solution().maxSumTwoNoOverlap(nums,firstLen,secondLen)==20

