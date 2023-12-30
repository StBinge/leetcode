#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#
from sbw import *
# @lc code=start
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(word:str):
            L=len(pattern)
            idx=0
            for ch in word:

                if idx<L and ch==pattern[idx]:
                    idx+=1
                elif ch.isupper():
                    return False
            return idx==len(pattern)
        ret=[]
        for q in queries:
            ret.append(match(q))
        return ret
# @lc code=end
queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaT"
ret='[false,true,false,false,false]'
assert Solution().camelMatch(queries,pattern)==eval_list_str(ret)

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBa"
ret='[true,false,true,false,false]'
assert Solution().camelMatch(queries,pattern)==eval_list_str(ret)

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"
ret='[true,false,true,true,false]'
assert Solution().camelMatch(queries,pattern)==eval_list_str(ret)
