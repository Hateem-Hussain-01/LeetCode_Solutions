class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 ==0:
                answer.append("FizzBuzz")
            elif i%3 ==0:
                answer.append("Fizz")
            elif i%5==0:
                answer.append("Buzz")   #wh
            else:
                answer.append(str(i))
        return answer



        # #1.42 MB Beats 22.39% hl
        # result =[]
        # for i in range(1,n+1):
        #     if not i % 15 :
        #         result.append("FizzBuzz")
        #     elif not i % 3:
        #         result.append("Fizz")
        #     elif not i % 5:         
        #         result.append("Buzz")
        #     else:
        #         result.append(str(i))
        
        # return result


        # more pythonic
        #18.56 MB  Beats 22.39%
        # return [
        #     "FizzBuzz" if i % 15 == 0 else 
        #     "Fizz" if i % 3 == 0 else 
        #     "Buzz" if i % 5 == 0 else 
        #     str(i) 
        #     for i in range(1, n + 1)
        # ]
        

    #     print("fuck")

    #  return ou