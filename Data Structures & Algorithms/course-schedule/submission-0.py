from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

        def dfs(course):
            if visited[course] == 1:  # cycle detected
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited[course] = 2
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
