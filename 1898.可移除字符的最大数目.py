#
# @lc app=leetcode.cn id=1898 lang=python3
#
# [1898] 可移除字符的最大数目
#
from sbw import *
# @lc code=start
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        N=len(s)
        M=len(p)
        # counter_s=Counter(s)
        # counter_p=Counter(p)
        # ss=list(s)

        def check(k):
            removed=[False]*N
            for i in range(k):
                removed[removable[i]]=True
            idx=0
            for i in range(N):
                if not removed[i] and s[i]==p[idx]:
                    idx+=1
                    if idx==M:
                        return True
            return False

        left=0
        right=min(len(removable),N-M)
        ret=0
        while left<=right:
            mid=(left+right)>>1
            if check(mid):
                ret=mid
                left=mid+1
            else:
                right=mid-1
        return ret

# @lc code=end
assert Solution().maximumRemovals(s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6])==1
assert Solution().maximumRemovals(s = "abcab", p = "abc", removable = [0,1,2,3,4])==0
assert Solution().maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0])==2
