class CountSquares:
    def __init__(self):
        self.points = defaultdict(int)
        self.pts = []
    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        self.pts.append(point)
            
    def count(self, point: List[int]) -> int:
        x0, y0 = point
        res = 0
        for x1, y1 in self.pts:
            if abs(x1-x0)!=abs(y1-y0) or x0==x1 or y0==y1: continue 
            res+= self.points[(x0,y1)]*self.points[(x1,y0)]
        
        return res