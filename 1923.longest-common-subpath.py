#
# @lc app=leetcode.cn id=1923 lang=python3
# @lcpr version=30204
#
# [1923] 最长公共子路径
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        Mod=(10**9+7)*(10**9+9)
        k1,k2=randint(10**6,10**7),randint(10**7,10**8)
        def get_hash(path:list,l:int):
            h1=h2=0
            mul1=pow(k1,l,Mod)
            mul2=pow(k2,l,Mod)
            for i in range(l):
                h1=(h1*k1+path[i])%Mod
                h2=(h2*k2+path[i])%Mod
            # s1=set()
            # s2=set()
            # s1.add(h1)
            # s2.add(s2)
            yield [h1,h2]
            for i in range(l,len(path)):
                h1=(h1*k1-path[i-l]*mul1+path[i])%Mod
                # s1.add(h1)
                h2=(h2*k2-path[i-l]*mul2+path[i])%Mod
                # s2.add(h2)
                yield [h1,h2]

        left=0
        right=min(map(len,paths))
        ret=0
        while left<=right:
            mid=(left+right)>>1
            valid=True
            s1=set()
            s2=set()
            for h1,h2 in get_hash(paths[0],mid):
                s1.add(h1)
                s2.add(h2)

            for i in range(1,len(paths)):
                t1=set()
                t2=set()
                for h1,h2 in get_hash(paths[i],mid):
                    if h1 in s1:
                        t1.add(h1)
                    if h2 in s2:
                        t2.add(h2)
                if not t1 or not t2:
                    valid=False
                    break
                s1,s2=t1,t2
            if valid:
                left=mid+1
                ret=mid
            else:
                right=mid-1
        return ret

# @lc code=end
assert Solution().longestCommonSubpath(n = 5, paths = [[0,1,2,3,4],
                     [4,3,2,1,0]])==1
assert Solution().longestCommonSubpath(n = 3, paths = [[0],[1],[2]])==0
assert Solution().longestCommonSubpath(n = 5, paths = [[0,1,2,3,4],
                     [2,3,4],
                     [4,0,1,2,3]])==2


#
# @lcpr case=start
# 5\n[[0,1,2,3,4],[2,3,4],[4,0,1,2,3]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0],[1],[2]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,1,2,3,4],[4,3,2,1,0]]\n
# @lcpr case=end

#

