class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = [0] * n

        print(visited)

        graph = defaultdict(list)

        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)
        
        print(graph)

        def dfs(node):
            visited[node] = 1

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
                
        output = 0

        for node in range(n):
            if not visited[node]:
                dfs(node)
                output += 1
        
        return output

        
        