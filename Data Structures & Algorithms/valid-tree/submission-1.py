class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        graph = defaultdict(list)

        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
                
        visited = [0] * n

        def dfs(node, parent):
            visited[node] = 1

            for child in graph[node]:
                if child == parent:
                    continue
                if visited[child] == 1:
                    return False
                if not dfs(child, node):
                    return False
                
            return True
        
        if not dfs(0, -1):
            return False

        return all(visited)
        
