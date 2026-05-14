class TimeMap:

    def __init__(self):
        self.key_map: dict[str, list[tuple[int, str]]] = defaultdict(list) # key to list of timestamp,value tuples

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.key_map[key]
        values.append((timestamp, value))
        
    @staticmethod
    def bin_search(values: list[tuple[int,str]], timestamp:int) -> int:
        n = len(values)
        l, r = 0, n-1
        res = -1
        while l<=r:
            m = (l+r)//2
            m_t = values[m][0]
            if m_t==timestamp: return m
            elif m_t>timestamp: r=m-1
            else: res=m; l=m+1
        return res

    def get(self, key: str, timestamp: int) -> str:
        values = self.key_map[key]
        if not values: return ""
        idx = self.bin_search(values, timestamp)
        return values[idx][1] if idx!=-1 else ""