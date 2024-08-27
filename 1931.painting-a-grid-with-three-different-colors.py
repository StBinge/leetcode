#
# @lc app=leetcode.cn id=1931 lang=python3
# @lcpr version=30204
#
# [1931] 用三种不同颜色为网格涂色
#

from sbw import *

def covert(mask:int,m):
    ret=''
    for i in range(m):
        ret+=str(mask%3)
        mask//=3
    return ret
# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod=10**9+7
        Mask=3**m

        valid_masks=[]

        for mask in range(Mask):
            pre=-1
            _mask=mask
            for i in range(m):
                cur=mask%3
                mask//=3
                if cur==pre:
                    break
                pre=cur
            else:
                valid_masks.append(_mask)

        
        M=len(valid_masks)
        adjcent=[list() for _ in range(M)]
        for i in range(M):
            _mask=valid_masks[i]
            for j in range(i+1,M):
                mask=_mask
                mask2=valid_masks[j]
                for _ in range(m):
                    if mask%3==mask2%3:
                        break
                    mask//=3
                    mask2//=3
                else:
                    adjcent[i].append(j)
                    adjcent[j].append(i)
                    # print(covert(valid_masks[i],m))
                    # print(covert(valid_masks[j],m))
                    # print()
        f0=[1]*M
        f1=[0]*M
        for i in range(1,n):
            for j in range(M):
                f1[j]=sum(f0[k] for k in adjcent[j])
                f1[j]%=mod
            f0,f1=f1,f0
        return sum(f0)%mod


# @lc code=end
# assert Solution().colorTheGrid(2, 2) == 18
assert Solution().colorTheGrid(5, 5) == 580986
assert Solution().colorTheGrid(1, 2) == 6
assert Solution().colorTheGrid(1, 1) == 3


#
# @lcpr case=start
# 1\n1\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n
# @lcpr case=end

# @lcpr case=start
# 5\n5\n
# @lcpr case=end

#
