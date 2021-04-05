num = int(input("Give a number: "))
check = int(input("Give a second number: "))
if num % 4 == 0:
    print("Multiple of 4")
elif num % 2 == 0:
    print("The first num is Even")
else:
    print("The first num is Odd")

if check % num == 0:
    print("The second num divides evenly into the first")
