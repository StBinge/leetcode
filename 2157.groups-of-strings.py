#
# @lc app=leetcode.cn id=2157 lang=python3
# @lcpr version=30204
#
# [2157] 字符串分组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        N=len(words)
        # words.sort(key=len)
        parents=list(range(N))
        size=[1]*N
        cnt=N
        def find(x):
            if x!=parents[x]:
                parents[x]=find(parents[x])
            return parents[x]
        
        def union(x,y):
            x,y=find(x),find(y)
            if x==y:
                return
            if size[x]>size[y]:
                x,y=y,x
            parents[x]=y
            size[y]+=size[x]
            nonlocal cnt
            cnt-=1
        
        vis={}
        bit_map=defaultdict(list)
        r_bit=1<<26
        for i,word in enumerate(words):
            mask=0
            for ch in word:
                mask|= 1<<(ord(ch)-ord('a'))
            j=vis.setdefault(mask,i)
            if j!=i:
                union(i,j)
            for k in range(26):
                if mask & (1<<k):
                    _mask=mask^(1<<k)|r_bit
                    j=vis.setdefault(_mask,i)
                    if j!=i:
                        union(i,j)
                _mask=mask ^ (1<<k)
                j=vis.get(_mask,-1)
                if j!=-1:
                    union(i,j)

       
        mx_size=max(size)
        return [cnt,mx_size]
        

# @lc code=end
assert Solution().groupStrings(["ghnv","uip","tenv","hvepx","e","ktc","byjdt","ulm","cae","ea"])==[8,3]


#
# @lcpr case=start
# ["a","b","ab","cde"]\n
# @lcpr case=end

# @lcpr case=start
# ["a","ab","abc"]\n
# @lcpr case=end

#

