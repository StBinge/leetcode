#
# @lc app=leetcode.cn id=906 lang=python3
#
# [906] 超级回文数
#

# @lc code=start
import math
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        _L=int(left)
        _R=int(right)
        magic=10**5
        
        def is_p(x:int):
            y=x
            z=0
            while x>0:
                z=z*10+x%10
                x//=10
            return y==z

        ret=0
        # odd
        for i in range(magic):
            j=i
            i//=10
            while i>0:
                j=j*10+i%10
                i//=10
            jj=j*j
            if jj<_L:
                continue
            if jj>_R:
                break
            if is_p(jj):
                ret+=1

        # even
        for i in range(magic):
            j=i
            while i>0:
                j=j*10+i%10
                i//=10
            jj=j*j
            if jj<_L:
                continue
            if jj>_R:
                break
            if is_p(jj):
                ret+=1
        return ret
# @lc code=end
assert Solution().superpalindromesInRange('4','1000')==4
