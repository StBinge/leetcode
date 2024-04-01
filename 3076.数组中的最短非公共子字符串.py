#
# @lc app=leetcode.cn id=3076 lang=python3
#
# [3076] 数组中的最短非公共子字符串
#
from sbw import *
# @lc code=start
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        max_len=max(map(len,arr))
        L=len(arr)
        ret=[""]*L
        cnt=0
        # def get_code(s:str):
        #     return ord(s)-ord('a')
        not_comleted=set(range(L))
        for l in range(1,max_len+1):
            counter=defaultdict(set)
            for idx,word in enumerate(arr):
                for i in range(len(word)-l+1):
                    counter[word[i:i+l]].add(idx)

            for k,v in counter.items():
                if len(v)!=1:
                    continue
                idx=v.pop()
                if not ret[idx]:
                    ret[idx]=k
                elif len(ret[idx])<len(k):
                    continue
                else:
                    ret[idx]=min(ret[idx],k)
            for i in range(L):
                if ret[i]:
                    not_comleted.discard(i)
            if not not_comleted:
                break
        return ret

# @lc code=end
assert Solution().shortestSubstrings(["mlwy","hnlkg","f","itk","nbxks","jot","swl","qskj"])==["m","g","f","i","b","o","sw","q"]
assert Solution().shortestSubstrings(["vbb","grg","lexn","oklqe","yxav"])==["b","g","n","k","a"]
assert Solution().shortestSubstrings(["abc","bcd","abcd"])==["","","abcd"]
assert Solution().shortestSubstrings(["cab","ad","bad","c"])==["ab","","ba",""]
