#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#
from typing import List
# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        codes_mask=[]
        for code in codes:
            n=len(code)
            mask=0
            for c in code:
                mask=(mask<<1)|(1 if c=='-' else 0)
            codes_mask.append([mask,n])

        visited=set()

        for word in words:
            trans=1
            for c in word:
                mask,n=codes_mask[ord(c)-ord('a')]
                trans=(trans<<n)|mask
            visited.add(trans)
        return len(visited)
# @lc code=end

words=["vurk","ilck","sdck","anayg","ppon"]
assert Solution().uniqueMorseRepresentations(words)==2