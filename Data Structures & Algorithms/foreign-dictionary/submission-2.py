class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        for word in words:
            for letter in word:
                adj[letter]
        
        # ---------------------------------------------

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            found_diff = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    found_diff = True
                    break
            
            if not found_diff and len(w1) > len(w2):
                return ""
        
        # ---------------------------------------------

        visited = {ch : 0 for ch in adj}
        result = []
        self.cycle = False

        def dfs(word):
            if visited[word] == 1:
                self.cycle = True
                return 
            
            if visited[word] == 2:
                return 
            
            visited[word] = 1
            for val in adj[word]:
                dfs(val)
            
            visited[word] = 2
            result.append(word)

        for word in adj:
            if visited[word] == 0:
                dfs(word)
                if self.cycle:
                    return ""
        
        return "".join(result[::-1])