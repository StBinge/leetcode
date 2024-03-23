#
# @lc app=leetcode.cn id=1307 lang=python3
#
# [1307] 口算难题
#
from sbw import *
# @lc code=start
import math
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        L=len(result)
        weights=defaultdict(int)
        no_zero_chars=set()
        for word in words:
            if len(word)>L:
                return False
            if len(word)!=1:
                no_zero_chars.add(word[0])
            base=1
            for c in reversed(word):
                weights[c]+=base
                base*=10
        base=1
        for c in reversed(result):
            weights[c]-=base
            base*=10
        if L>1:
            no_zero_chars.add(result[0])
        
        weights=sorted([[k,v] for k,v in weights.items() if v!=0],key=lambda x:-abs(x[1]))
        used=[False]*10
        # chars={k:-1 for k,_ in weights}
        N=len(weights)
        def dfs(idx,total):
            if idx==N:
                return total==0
            mi=ma=total
            mi_start=ma_start=0
            mi_end=ma_end=9
            for i in range(idx+1,N):
                char,weight=weights[i]
                if weight<0:
                    mi+=weight*mi_end
                    mi_end-=1
                    ma+=weight*ma_start
                    ma_start+=1
                else:
                    mi+=weight*mi_start
                    mi_start+=1
                    ma+=weight*ma_end
                    ma_end-=1
            c,w=weights[idx]
            right=-mi/w
            left=-ma/w
            if w<0:
                left,right=right,left
            left=max(0,math.ceil(left))
            right=min(9,math.floor(right))
            for i in range(left,right+1):
                if used[i]:
                    continue
                if i==0 and c in no_zero_chars:
                    continue
                used[i]=True
                if dfs(idx+1,total+i*w):
                    return True
                used[i]=False
            return False
        return dfs(0,0)
            
# @lc code=end
assert  Solution().isSolvable(words = ["SEND","MORE"], result = "MONEY")
assert  Solution().isSolvable(words = ["THIS","IS","TOO"], result = "FUNNY")
assert  Solution().isSolvable(["AB","CD","EF"],
"GHIJ")==False
assert  Solution().isSolvable(words = ["LEET","CODE"], result = "POINT")==False
assert  Solution().isSolvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY")

