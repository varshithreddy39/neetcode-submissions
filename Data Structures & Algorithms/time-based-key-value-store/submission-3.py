class TimeMap:

    def __init__(self):
        self.store_values={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store_values:
            self.store_values[key]=[]
        self.store_values[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        ans=""
        if key not in self.store_values:
            return ""
        else:
            values=self.store_values[key]
        l=0
        r=len(values)-1

        while l<=r:
            mid=(l+r)//2
            if values[mid][1]<=timestamp:
                ans=values[mid][0]
                l=mid+1
            else:
                r=mid-1
        return ans

        
