#
# @lc app=leetcode.cn id=1702 lang=python3
#
# [1702] 修改后的最大二进制字符串
#

# @lc code=start
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        N=len(binary)
        ones=0
        zeros=0
        idx=0
        while idx<N and binary[idx]=='1':
            ones+=1
            idx+=1
        for i in range(idx,N):
            if binary[i]=='0':
                zeros+=1
        if zeros<=1:
            return binary
        tail_ones=N-ones-zeros

        return '1'*(ones+zeros-1)+ '0' +'1'*tail_ones           
# @lc code=end
assert Solution().maximumBinaryString('01')=='01'
assert Solution().maximumBinaryString('000110')=='111011'
