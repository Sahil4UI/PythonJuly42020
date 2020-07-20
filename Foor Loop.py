#FOOR LOOP
#->print 1to10
'''
for i in range(1,11):
    print(i)

for i in range(1,11):
    print(i)



for i in range(1,11):
    print(i*2-1)


for i in range(1,11,4):
    print(i)
'''
#STEP SIZE->+ve -ending range -> n-1
#STEp SIZE->-ve -endding range -> n+1
'''for i in range(10,0,-1):
    print(i)

for i in reversed(range(1,11)):
    print(i)
'''
#Check wether No is Prime or Not
number = int(input("Enter Number to Check wether it is Prime or Not"))

for i in range(2,number):
    if number%i ==0:
        print("Not Prime")
        break
else:
    print("Prime")
# 0 1 1 2 3 5 8 13 21 34->FIbonacci Series
#->Find sum of Digits of Number -> number 123->1+2+3=6
          
