class Solution:
    def isHappy(self, n: int) -> bool:
        def square_of_digits(n):
            s=0
            num=n
            while num!=0:
                digit=num%10
                s+=digit**2
                num//=10
            return s
        
        num_tracker=set()
        while n!=1 and (n not in num_tracker):
            num_tracker.add(n)
            n=square_of_digits(n)
            print("each",n,num_tracker)
        print("final",n)
        if n==1:
            return True
        else:
            return False

        