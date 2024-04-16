#
# @lc app=leetcode.cn id=1520 lang=python3
#
# [1520] 最多的不重叠子字符串
#
from sbw import *
# @lc code=start
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        L=len(s)
        # char : [left,right]
        segs={}
        for i in range(L):
            segs.setdefault(s[i],[0,0])
            segs.setdefault(s[L-i-1],[0,0])
            segs[s[i]][1]=i
            segs[s[L-i-1]][0]=L-i-1
        for ch,[left,right] in segs.items():
            i=left+1
            while i<=right:
                l,r=segs[s[i]]
                if left<=l and right>=r:
                    i+=1
                    continue
                left=min(left,l)
                right=max(right,r)
                i=left+1
            segs[ch]=[left,right]
        segs=sorted(segs.values(),key= lambda x:(x[1],-x[0]))
        ret=[]
        end=-1
        for left,right in segs:
            if left>end:
                ret.append(s[left:right+1])
                end=right
        return ret
# @lc code=end
assert sorted(Solution().maxNumOfSubstrings('abab'))==sorted(['abab'])
assert sorted(Solution().maxNumOfSubstrings('abbaccd'))==sorted(["d","bb","cc"]),Solution().maxNumOfSubstrings('abbaccd')
assert sorted(Solution().maxNumOfSubstrings('adefaddaccc'))==sorted(["e","f","ccc"])
