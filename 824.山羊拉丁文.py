#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowles='aeiou'
        ret=[]
        start=0
        def handle(word:str):
            if word[0].lower() in vowles:
                return word+'ma'+'a'*(len(ret)+1)
            return word[1:]+word[0]+'ma'+'a'*(len(ret)+1)
        for i,c in enumerate(sentence):
            if c==' ':
                ret.append(handle(sentence[start:i]))
                start=i+1
        ret.append(handle(sentence[start:]))
        return ' '.join(ret)
# @lc code=end
sentence = "I speak Goat Latin"
ret="Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
assert Solution().toGoatLatin(sentence)==ret

sentence = "The quick brown fox jumped over the lazy dog"
ret="heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
assert Solution().toGoatLatin(sentence)==ret
