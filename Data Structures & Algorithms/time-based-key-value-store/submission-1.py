class TimeMap:

    def __init__(self):
        self.mem = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mem:
            self.mem[key] = []
        self.mem[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mem:
            return ""
        
        keyArr = self.mem[key]
        
        l, r = 0, len(keyArr) - 1
        val = ""
        while l <= r:
            mid = (l + r) // 2

            if keyArr[mid][1] == timestamp:
                return keyArr[mid][0]
            elif keyArr[mid][1] > timestamp:
                r = mid - 1
            else:
                val = keyArr[mid][0]
                l = mid + 1
        return val
