class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack
        stack = []
        start = {"(": ")", "{": "}", "[": "]"}
        n = len(s)
        for i in range(n):
            if s[i] in start:    #  [{( -> put in stack
                stack.append(s[i])
            else:       # pop from stack, see if they are matched
                if not stack or s[i] != start[stack.pop()]:
                    return False
        return True if not stack else False  # if there are not matched