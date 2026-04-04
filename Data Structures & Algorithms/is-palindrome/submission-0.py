class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=''
        for char in s:
            if char.isalnum():
                string+=char.lower()
        i=0
        j=len(string)-1
        print(i,j)
        while i<j:
            print(i,j)
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        return True
        