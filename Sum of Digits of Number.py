#find the sum of Digits of Number
#number ->245 ->2+4+5
number = 12345
sum1 =0
for i in range(len(str(number))):
    remainder = number%10
    sum1 = sum1+remainder
    number  = number//10
print(sum1)
    
#HW
'''
*
**
***
****
*****
'''
#CHECK WETHER NUMBER IS ARMSTRONG OR NOT ->153 ->1^3+5^3+3^3->3+125+27 ->153
