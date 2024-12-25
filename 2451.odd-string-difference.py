#
# @lc app=leetcode.cn id=2451 lang=python3
# @lcpr version=30204
#
# [2451] 差值数组不同的字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def oddString(self, words: List[str]) -> str:
        def get_dif(word:str):
            dif=[]
            for x,y in pairwise(word):
                dif.append(ord(x)-ord(y))
            return dif
        
        dif0=get_dif(words[0])
        dif1=get_dif(words[1])
        if dif0==dif1:
            for word in words[2:]:
                if get_dif(word)!=dif0:
                    return word
        dif2=get_dif(words[2])
        return words[0] if dif1==dif2 else words[1]

                
            
                    

# @lc code=end
assert Solution().oddString(["aaa","bob","ccc","ddd"])=='bob'
assert Solution().oddString(["ddd","poo","baa","onn"])=='ddd'
assert Solution().oddString(["adc","wzy","abc"])=='abc'


#
# @lcpr case=start
# ["adc","wzy","abc"]\n
# @lcpr case=end

# @lcpr case=start
# ["aaa","bob","ccc","ddd"]\n
# @lcpr case=end

#

