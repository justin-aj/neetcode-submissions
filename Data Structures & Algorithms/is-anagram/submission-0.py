class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = [i for i in s]
        t_ = [i for i in t]
        s_.sort()
        t_.sort()
        print(s_, t_)
        if s_ == t_:
            return True
        else:
            return False