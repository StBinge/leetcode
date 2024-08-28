#
# @lc app=leetcode.cn id=2227 lang=python3
# @lcpr version=30204
#
# [2227] 加密解密字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys=dict(zip(keys,values))
        self.dicts=Counter(map(self.encrypt,dictionary))

    def encrypt(self, word1: str) -> str:
        ret=''
        for ch in word1:
            if ch not in self.keys:
                return ''
            ret+=self.keys.get(ch)
        return ret
    
    def decrypt(self, word2: str) -> int:
        return self.dicts[word2]



# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
# @lc code=end
encrypter = Encrypter(['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])#
assert encrypter.encrypt("abcd")=='eizfeiam'
assert encrypter.decrypt("eizfeiam")==2


#
# @lcpr case=start
# ["Encrypter", "encrypt", "decrypt"][[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]],["abcd"], ["eizfeiam"]]\n
# @lcpr case=end

#

