class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        results = []

        elements = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(i, current):
            if i == len(digits):
                results.append(current)
                return
            
            for letter in elements[digits[i]]:
                backtrack(i + 1, current + letter)
        
        backtrack(0, "")
        return results
            
