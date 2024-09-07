class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff=float('inf')
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum ==target:
                    return target
                elif abs(target-sum) < diff:
                    diff=abs(target-sum)
                    ans=sum
                elif sum> target:
                    right-=1
                else:
                    left+=1        
        return ans






        