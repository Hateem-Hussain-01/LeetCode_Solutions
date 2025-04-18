class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) # assigning indexes for low and high
        while low < high: # the loop will run until low is less than high
            mid = (low + high)// 2 # calculating mid point
            if nums[mid] == target: # if the value of mid is equal to target
                return mid # returning mid ie index
            elif nums[mid] < target: #if the value of mid is less than target
                low = mid + 1 # assigning low to be mid + 1
            else: # if the value of mid is greater than target
                high = mid # assigning high to be mid
        return low # returning low as output