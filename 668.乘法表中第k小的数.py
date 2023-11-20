#
# @lc app=leetcode.cn id=668 lang=python3
#
# [668] 乘法表中第k小的数
#

# @lc code=start
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left=0
        right=m*n
        while left<right:
            mid=(left+right)//2
            less_cnt=mid//n*n
            for i in range(mid//n+1,m+1):
                less_cnt+=mid//i
            if less_cnt<k:
                left=mid+1
            else:
                right=mid
        return left
# @lc code=end

assert Solution().findKthNumber(3,3,5)==3
assert Solution().findKthNumber(2,3,6)==6