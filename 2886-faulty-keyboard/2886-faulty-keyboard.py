class Solution:
    def finalString(self, s: str) -> str:
      res = ""
      for j in s:
        if j == "i":
          res = res[::-1]
        else:
          res += j
      return res
      


