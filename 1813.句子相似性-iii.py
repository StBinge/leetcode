#
# @lc app=leetcode.cn id=1813 lang=python3
#
# [1813] 句子相似性 III
#


# @lc code=start
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")
        head = 0
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        for i in range(len(words1)):
            if words1[i] != words2[i]:
                break
            else:
                head += 1
        else:
            return True

        tail = 0
        for i in range(1, len(words1) + 1):
            if words1[-i] != words2[-i]:
                break
            else:
                tail += 1
        else:
            return True

        return head + tail >= len(words1)


# @lc code=end
assert Solution().areSentencesSimilar("A B C D B B","A B B")
assert Solution().areSentencesSimilar(sentence1="Luky", sentence2="Lucccky") == False
assert Solution().areSentencesSimilar(sentence1="Eating right now", sentence2="Eating")
assert (
    Solution().areSentencesSimilar(sentence1="of", sentence2="A lot of words") == False
)
assert Solution().areSentencesSimilar(
    sentence1="My name is Haley", sentence2="My Haley"
)
