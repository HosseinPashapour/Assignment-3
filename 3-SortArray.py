Length = int(input("please enter the length of your list: "))
Array =[]
for i in range(Length):
    x = int(input("enter numper: "))
    Array.append(x)
if Array != sorted(Array):
    print("Your list is NOT sorted.")
else:
    print("Your list is sorted")
