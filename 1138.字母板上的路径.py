#
# @lc app=leetcode.cn id=1138 lang=python3
#
# [1138] 字母板上的路径
#

# @lc code=start
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pos=[None]*26
        for i in range(26):
            r,c=i//5,i%5
            pos[i]=[r,c]
        
        cur=[0,0]
        ret=[]
        for ch in target:
            r,c=pos[ord(ch)-ord('a')]
            dr,dc=r-cur[0],c-cur[1]
            h_dir='L' if dc < 0 else 'R'
            v_dir='U' if dr < 0 else 'D'
            vert=v_dir * abs(dr)
            hori=h_dir * abs(dc)
            if ch=='z':
                ret.append(hori)
                ret.append(vert)
            else:
                ret.append(vert)
                ret.append(hori)
            ret.append('!')
            cur=[r,c]
        return ''.join(ret)
# @lc code=end
ans=Solution().alphabetBoardPath('zdz')
print(ans)
assert len(ans)==len("DDDDD!UUUUURRR!DDDDLLLD!")

ans=Solution().alphabetBoardPath('code')
print(ans)
assert len(ans)==len("RR!DDRR!UUL!R!")

ans=Solution().alphabetBoardPath('leet')
print(ans)
assert len(ans)==len("DDR!UURRR!!DDD!")
