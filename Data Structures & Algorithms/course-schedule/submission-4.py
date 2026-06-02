class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        lets do adjacency matrix instead [src][dst]
        course1][course2] tells you whether course1 has an incoming edge from course2
        '''
        adj_m = [[False]*numCourses for _ in range(numCourses)]
        q = deque()
        for course, prereq in prerequisites:
            adj_m[course][prereq] = True

        res = numCourses
        for i in range(numCourses):
            if not any(adj_m[i]): q.append(i)

        while q:
            for _ in range(len(q)):
                prereq = q.popleft()
                res-=1
                for i in range(numCourses):
                    if adj_m[i][prereq]:
                        adj_m[i][prereq]=False
                        if not any(adj_m[i]): q.append(i)
        
        return True if res==0 else False