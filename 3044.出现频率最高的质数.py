#
# @lc app=leetcode.cn id=3044 lang=python3
#
# [3044] 出现频率最高的质数
#
from sbw import *
# @lc code=start
import math
class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def is_prime(n:int):
            return all(n%i for i in range(2,math.isqrt(n)+1))
        R,C=len(mat),len(mat[0])
        # Max=10**max(R,C)
        # is_prime=[True]*Max
        # for i in range(2,Max):
        #     for j in range(i+i,Max,i):
        #         is_prime[j]=False
        r_dirs=[-1,-1,0,1,1,1,0,-1]
        c_dirs=[0,1,1,1,0,-1,-1,-1]
        counter=defaultdict(int)
        for r in range(R):
            for c in range(C):
                for i in range(8):
                    n=mat[r][c]
                    dr,dc=r_dirs[i],c_dirs[i]
                    nr,nc=r+dr,c+dc
                    while 0<=nr<R and 0<=nc<C:
                        n=n*10+mat[nr][nc]
                        if n in counter or is_prime(n):
                            counter[n]+=1
                        nr,nc=nr+dr,nc+dc
        max_freg=0
        ret=-1
        for k,v in counter.items():
            if v>max_freg:
                max_freg=v
                ret=k
            elif v==max_freg:
                ret=max(ret,k)
        return ret
# @lc code=end

assert Solution().mostFrequentPrime([[9,7,8],[4,6,5],[2,8,6]])==97
assert Solution().mostFrequentPrime([[7]])==-1
assert Solution().mostFrequentPrime([[1,1],[9,9],[1,1]])==19