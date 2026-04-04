class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(arr,target,l,r):
            res=[]
            while l<r:
                if arr[l]+arr[r]<target:
                    l+=1
                elif arr[l]+arr[r]>target:
                    r-=1
                else:
                    res.append([arr[l],arr[r]])
                    l+=1
                    r-=1
                    while arr[l]==arr[l-1] and l<r:
                        l+=1
            return res

        nums.sort()
        print(nums)
        res=[]
        for idx,val in enumerate(nums):
            target=-1*val
            if idx>0 and val==nums[idx-1]:
                continue # duplicate move ahead
            if val>0:
                break
            small_res=twoSum(nums,target,idx+1,len(nums)-1)
            if small_res:
                for r in small_res:
                    res.append([val,r[0],r[1]])
        return res
            
            

            