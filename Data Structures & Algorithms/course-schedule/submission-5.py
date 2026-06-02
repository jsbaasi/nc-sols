class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        lets do adjacency matrix instead [src][dst]
        course1][course2] tells you whether course1 has an incoming edge from course2
        '''
        adj_m = [[False]*numCourses for _ in range(numCourses)]
        ins = [0]*numCourses
        q = deque()
        for course, prereq in prerequisites:
            adj_m[course][prereq] = True
            ins[course]+=1

        for i in range(numCourses):
            if not ins[i]: q.append(i)

        while q:
            for _ in range(len(q)):
                prereq = q.popleft()
                for i in range(numCourses):
                    if adj_m[i][prereq]:
                        adj_m[i][prereq]=False
                        ins[i]-=1
                        if not ins[i]: q.append(i)
        
        return True if all(ins[i]==0 for i in range(numCourses)) else False