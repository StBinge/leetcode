#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
#     pass
class Solution:
    def guessNumber(self, n: int) -> int:
        left,right=0,n
        while left<=right:
            mid=(left+right)//2
            r=guess(mid)
            if r<0:
                right=mid-1
            elif r>0:
                left=mid+1
            else:
                return mid
# @lc code=end

