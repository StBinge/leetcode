#
# @lc app=leetcode.cn id=1545 lang=python3
#
# [1545] 找出第 N 个二进制字符串中的第 K 位
#

# @lc code=start
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k==1:
            return '0'
        mid=2**(n-1)
        if k==mid:
            return '1'
        if k<mid:
            return self.findKthBit(n-1,k)
        else:
            k=mid*2-k
            bit=self.findKthBit(n-1,k)
            return '0' if bit=='1' else '1'
# @lc code=end
assert Solution().findKthBit(2,3)=='1'
assert Solution().findKthBit(3,2)=='1'
assert Solution().findKthBit(4,11)=='1'
assert Solution().findKthBit(3,1)=='0'
