#
# @lc app=leetcode.cn id=2019 lang=python3
# @lcpr version=30204
#
# [2019] 解出数学表达式的学生分数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:

        st=[]
        for ch in s:
            if ch=='+':
                continue
            elif ch=='*':
                st.append('*')
            else:
                if st and st[-1]=='*':
                    st.pop()
                    st.append(st.pop()*int(ch))
                else:
                    st.append(int(ch))
        answer=sum(st)
        
        N=len(s)
        # digits=[]
        # ops=[]
        # for ch in s:
        #     if ch.isdigit():
        #         digits.append(int(ch))
        #     elif ch=='*':
        #         ops.append('*')
        #     else:
        #         if ops and ops[-1]==


        add=lambda x,y:x+y
        mul=lambda x,y:x*y
        
        f=[[None for _ in range(N)] for _ in range(N)]
        for i in range(N-1,-1,-2):
            f[i][i]=[int(s[i])]
            for j in range(i+2,N,2):
                vals=set()
                for k in range(i+1,j,2):
                    op=add if s[k]=='+' else mul
                    for v1 in f[i][k-1]:
                        for v2 in f[k+1][j]:
                            v=op(v1,v2)
                            if v>1000:
                                continue
                            vals.add(v)
                f[i][j]=vals

        values=f[0][-1]
        ret=0
        for n in answers:
            if n==answer:
                ret+=5
            elif n in values:
                ret+=2
        return ret
    
# @lc code=end

assert Solution().scoreOfStudents(s = "3+5*2", answers = [13,0,10,13,13,16,16])==19
assert Solution().scoreOfStudents(s = "7+3*1*2", answers = [20,13,42])==7

#
# @lcpr case=start
# "7+3*1*2"\n[20,13,42]\n
# @lcpr case=end

# @lcpr case=start
# "3+5*2"\n[13,0,10,13,13,16,16]\n
# @lcpr case=end

# @lcpr case=start
# "6+0*1"\n[12,9,6,4,8,6]\n
# @lcpr case=end

#

