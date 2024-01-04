#
# @lc app=leetcode.cn id=1092 lang=python3
#
# [1092] 最短公共超序列
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        L1,L2=len(str1),len(str2)
        if L1<L2:
            str1,str2=str2,str1
            L1,L2=L2,L1
        f=[[0]*(L2+1) for _ in range(L1+1)]

        for i in range(L1):
            f[i][L2]=L1-i
        for i in range(L2):
            f[L1][i]=L2-i

        for i in range(L1-1,-1,-1):
            for j in range(L2-1,-1,-1):
                if str1[i]==str2[j]:
                    f[i][j]=f[i+1][j+1]+1
                else:
                    f[i][j]=min(f[i+1][j],f[i][j+1])+1
                # common=max(common,f[i+1][j+1])
        if f[0][0]==L2:
            return str1
        
        t1,t2=0,0
        ret=[]
        while t1<L1 and t2<L2:
            if str1[t1]==str2[t2]:
                ret.append(str1[t1])
                t1+=1
                t2+=1
            else:
                if f[t1+1][t2]==f[t1][t2]-1:
                    ret.append(str1[t1])
                    t1+=1
                elif f[t1][t2+1]==f[t1][t2]-1:
                    ret.append(str2[t2])
                    t2+=1
                # else:
                #     ret.append(str1[t1])
                #     ret.append(str2[t2])
                #     t1+=1
                #     t2+=1

        while t1<L1:
            ret.append(str1[t1])
            t1+=1
        while t2<L2:
            ret.append(str2[t2])
            t2+=1
        return ''.join(ret)
# @lc code=end
ans= Solution().shortestCommonSupersequence(str1 = "aaaaaaaa", str2 = "aaaaaaaa") 
ret='aaaaaaaa'
assert len(ret)==len(ans)
ret= Solution().shortestCommonSupersequence(str1 = "abac", str2 = "cab") #'cabac'
assert len(ret)==5

