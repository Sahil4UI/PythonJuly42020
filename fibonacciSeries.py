




#Fibonacci Series- 0 1 1 2 3 5 8 ....
first = 0
second = 1
print(first)
print(second)

for i in range(1,9):
    third = first+second
    print(third)
    first = second
    second = third
    

