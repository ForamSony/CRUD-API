# def square(num):
#     return num*num
# for i in [1,2,3,4,5]:
#     result = square(i)
#     print("square of" ,i ,"i=", result )
  
def getSum(n):
 sum = 0
 while (n != 0):
  sum =  (n % 10) + sum
  n = n // 10
 return sum
n = 123
print(getSum(n))