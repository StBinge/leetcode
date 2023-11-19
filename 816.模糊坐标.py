#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#
from typing import List
# @lc code=start
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:

        def parse(start,end):
            l=end-start+1
            if l==1:
                return [s[start]]
            prefix=s[start]=='0'
            suffix=s[end]=='0'
            if prefix and suffix:
                return []
            ret=[]
            if not prefix:
                ret.append(s[start:end+1])
                if not suffix:
                    for i in range(1,l):
                        ret.append(s[start:start+i]+'.'+s[start+i:end+1])
            elif not suffix:
                ret.append('0.'+s[start+1:end+1])
            return ret

        s=s[1:-1]
        L=len(s)
        ret=[]
        for i in range(1,L):
            left_parts=parse(0,i-1)
            if not left_parts:
                continue
            right_parts=parse(i,L-1)
            if not right_parts:
                continue
            for left in left_parts:
                for right in right_parts:
                    ret.append(f'({left}, {right})')
        return ret
# @lc code=end
print(Solution().ambiguousCoordinates("(00011)"))
print(Solution().ambiguousCoordinates("(123)"))
print(Solution().ambiguousCoordinates("(0123)"))
print(Solution().ambiguousCoordinates("(100)"))
