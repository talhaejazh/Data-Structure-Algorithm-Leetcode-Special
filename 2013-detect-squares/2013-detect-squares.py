class DetectSquares:

    def __init__(self):
        self.pmap=defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        x,y=point
        self.pmap[tuple((x,y))]+=1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        qx, qy = point
        count=0
        for x,y in self.pts:
            if qx==x and qy==y or abs(qx-x)!= abs(qy-y):
                continue
            
            if (x, qy) in self.pmap and (qx,y) in self.pmap:
                count+= self.pmap[(x,qy)] * self.pmap[(qx,y)]
        return count



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)