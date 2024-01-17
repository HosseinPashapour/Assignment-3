first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
Bmm = 0

if first_num > second_num:
    x = second_num

elif first_num < second_num:
    x = first_num

for i in range(1 , x+1):
    if first_num % i == 0 and second_num % i == 0:
        Bmm = i


kmm = int((first_num * second_num)/Bmm)
print("Kmm = " , kmm) 