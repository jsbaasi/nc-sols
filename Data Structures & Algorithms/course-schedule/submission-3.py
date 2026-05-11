class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        this is about checking for cycles.
        if one course depends on another course that is behind it AND there's no other
        path to that course then it's a failure. we build a graph from the dependencies

        adjacency matrix or list? deffo list, i don't want quick checking for edges
        i want to get a nodes all edges quickly
        > we make map of number_course to list
        > 
        '''
        adjacency_list = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjacency_list[course].append(prereq)
        
        visit = set()
        def dfs(course: int) -> bool:
            if not adjacency_list[course]: return True
            if course in visit: return False
            prereqs = adjacency_list[course]
            visit.add(course)
            for prq in prereqs:
                if not dfs(prq): return False
            visit.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True


