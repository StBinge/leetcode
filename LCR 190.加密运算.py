#
# @lc app=leetcode.cn id=LCR 190 lang=python3
# @lcpr version=30204
#
# [LCR 190] 加密运算
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        mask=0xffffffff
        dataA&=mask
        dataB&=mask
        while dataB:
            dataA,dataB=dataA^dataB,((dataB&dataA)<<1)&mask
        return dataA if dataA<=0x7fffffff else ~(dataA^mask)
# @lc code=end
assert Solution().encryptionCalculate()


#
# @lcpr case=start
# 5\n-1\n
# @lcpr case=end

#

