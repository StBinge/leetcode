#
# @lc app=leetcode.cn id=2115 lang=python3
# @lcpr version=30204
#
# [2115] 从给定原材料中找到所有可以做出的菜
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies=set(supplies)
        indeg={}
        recipes={name:idx for idx,name in enumerate(recipes)}
        prevs=defaultdict(list)

        q=[]
        for name in recipes:
            valid=True
            for g in ingredients[recipes[name]]:
                if g in supplies:
                    continue
                if g in recipes:
                    indeg[name]=indeg.get(name,0)+1
                    prevs[g].append(name)
                valid=False
            if valid:
                q.append(name)
        
        ret=[]

        
        while q:
            cur=q.pop()
            ret.append(cur)
            for nxt in prevs[cur]:
                indeg[nxt]-=1
                if indeg[nxt]==0:
                    q.append(nxt)
        
        return ret
# @lc code=end
assert Solution().findAllRecipes()


#
# @lcpr case=start
# ["bread"]\n[["yeast","flour"]]\n["yeast","flour","corn"]\n
# @lcpr case=end

# @lcpr case=start
# ["bread","sandwich"]\n[["yeast","flour"],["bread","meat"]]\n["yeast","flour","meat"]\n
# @lcpr case=end

# @lcpr case=start
# ["bread","sandwich","burger"]\n[["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]\n["yeast","flour","meat"]\n
# @lcpr case=end

# @lcpr case=start
# ["bread"]\n[["yeast","flour"]]\n["yeast"]\n
# @lcpr case=end

#

