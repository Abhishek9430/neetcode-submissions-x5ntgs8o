class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        partitions=[]

        def dfs(i):
            if i>=len(s):
                res.append(partitions.copy())
                return

            for j in range(i,len(s)):
                string=s[i:j+1]
                if ispal(string):
                    partitions.append(s[i:j+1])
                    dfs(j+1)
                    partitions.pop()

        def ispal(string):
            i=0
            j=len(string)-1

            while i<j:
                if string[i]!=string[j]:
                    return False
                i+=1
                j-=1
            return True
        dfs(0)
        return res
        
        