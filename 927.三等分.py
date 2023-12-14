#
# @lc app=leetcode.cn id=927 lang=python3
#
# [927] 三等分
#
from sbw import *
# @lc code=start
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        one_cnt=sum(bit==1 for bit in arr)
        if one_cnt % 3:
            return [-1,-1]
        if one_cnt==0:
            return [0,2]
        avg=one_cnt//3
        first,second,third=0,0,0
        l=len(arr)
        cur=0
        for i in range(l):
            if arr[i]:
                if cur==avg*2:
                    third=i
                    break
                elif cur==avg:
                    second=i
                elif cur==0:
                    first=i
                cur+=1
        bit_len=l-third
        if first+bit_len>second or second+bit_len>third:
            return [-1,-1]
        for k in range(bit_len):
            if arr[first+k]!=arr[third+k] or arr[second+k]!=arr[third+k]:
                return [-1,-1]
        return [first+bit_len-1,second+bit_len]
# @lc code=end
arr=[1,1,1,1,1,1,0,1,1,1]
assert Solution().threeEqualParts(arr)==[2,6]

arr = [1,1,0,0,1]
assert Solution().threeEqualParts(arr)==[0,2]

arr = [1,0,1,0,1]
assert Solution().threeEqualParts(arr)==[0,3]
arr = [1,1,0,1,1]
assert Solution().threeEqualParts(arr)==[-1,-1]
