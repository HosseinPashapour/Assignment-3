print (" 🐍 PRINT SNAKE 🐍 ")
length = int(input("please enter size of the snake : "))
snake = ""
for i in range(length):
    if i % 2 == 0:
        snake += "*"
    else:
        snake += "#"
print(snake)
