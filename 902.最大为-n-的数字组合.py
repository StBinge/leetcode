#
# @lc app=leetcode.cn id=902 lang=python3
#
# [902] 最大为 N 的数字组合
#
from sbw import *
# @lc code=start
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        m=len(digits)
        s=str(n)
        k=len(s)

        bits=[]
        is_limited=True
        for c in s:
            if not is_limited:
                bits.append(m)
                continue
            
            select_idx=-1
            for i,d in enumerate(digits):
                if d>c:
                    break
                select_idx=i+1
            if select_idx<1:
                sz=len(bits)
                while bits and bits[-1]==1:
                    bits.pop()
                if bits:
                    bits[-1]-=1
                else:
                    sz-=1
                while len(bits)<=sz:
                    bits.append(m)
                # bits.append(m)
                is_limited=False
                continue
            bits.append(select_idx)
            if digits[select_idx-1]<c:
                is_limited=False


        ret=0
        for b in bits:
            ret=ret*m+b
        return ret

# @lc code=end
digits = ["1","3","5","7"]
n = 100
assert Solution().atMostNGivenDigitSet(digits,n)==20
digits = ["9"]
n = 55
assert Solution().atMostNGivenDigitSet(digits,n)==1

