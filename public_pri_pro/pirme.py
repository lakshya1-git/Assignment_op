num = int(input("Enter the to check prime or not"))
flag = False
if num == 1:
    print(num, "number is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % l) == 0:
            flag =  True
            break
    if flag:
        print(num, "is not a prime number")
    else:
        prime(num," is a prime number")
    