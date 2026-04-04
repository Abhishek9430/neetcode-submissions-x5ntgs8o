class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        
        for i in arr:
            if d[i]>1:
                return True

        return False
        

        