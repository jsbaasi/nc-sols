class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjacency_list[course].append(prereq)

        order = []
        visit = set()
        def dfs(course: int) -> bool:
            if course in order: return True
            if course in visit: return False

            prereqs = adjacency_list[course]
            visit.add(course)
            for prq in prereqs:
                if not dfs(prq): return False
            visit.remove(course)
            order.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return order