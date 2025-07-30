class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_num = set(nums)
        if len(nums)!= len(new_num):
            return True
        else:
            return False
        