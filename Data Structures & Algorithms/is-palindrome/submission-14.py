class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(list(s))
        a = []
        for i in list(s):
            if i.isalnum():
                a.append(i.lower())
        
        a = "".join(a)

        print(a)

        left = 0
        right = len(a) - 1

        while left < right:
            print(a[left], a[right])
            if a[left] != a[right]:
                return False
            left += 1
            right -= 1
        
        return True

        