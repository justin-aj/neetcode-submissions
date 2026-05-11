class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        for parent, neighbor in edges:
            graph[parent].append(neighbor)
            graph[neighbor].append(parent)
                
        visited = [0] * n

        def dfs(node, parent):
            visited[node] = 1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if visited[neighbor] == 1:
                    return False
                if not dfs(neighbor, node):
                    return False
                
            return True
        
        if not dfs(0, -1):
            return False

        return all(visited)
        
