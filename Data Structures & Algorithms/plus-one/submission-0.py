class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1,-1,-1):
            s=1+digits[i]
            if s<10:
                digits[i]=s
                break
            else:
                digits[i]=0
        if s==10:
            return [1]+digits
        return digits

