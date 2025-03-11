def check_divisibility(number):
    if 100<=number<1000:
        if number % 9 == 0:
            print (f"Number {number} is divisible by 9")
        else:
            print (f"Number {number} is  not divisible by 9")

number = int(input())
print(check_divisibility(number))