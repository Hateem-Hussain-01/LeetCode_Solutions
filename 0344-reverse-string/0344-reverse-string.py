class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left = 0
        # right = len(s)-1
        # while left <= right:
        #   s[left],s[right] = s[right],s[left]
        #   left +=1
        #   right -=1


        # s = s.reverse()
        # s[:]=s[::-1]


        
        def reverse_str(left, right):
          if left<right:
            s[left],s[right] = s[right],s[left]
            reverse_str(left+1, right-1)
        reverse_str(0, len(s)-1)

