#
# @lc app=leetcode.cn id=2452 lang=python3
# @lcpr version=30204
#
# [2452] 距离字典两次编辑以内的单词
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ret=[]
        for q in queries:
            for d in dictionary:
                dif=0
                for x,y in zip(q,d):
                    if x!=y:
                        dif+=1
                        if dif==3:
                            break
                else:
                    ret.append(q)
                    break
        return ret
# @lc code=end



#
# @lcpr case=start
# ["word","note","ants","wood"]\n["wood","joke","moat"]\n
# @lcpr case=end

# @lcpr case=start
# ["yes"]\n["not"]\n
# @lcpr case=end

#

