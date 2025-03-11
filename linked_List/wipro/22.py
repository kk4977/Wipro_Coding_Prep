def check_prediction(N):
    product = 1
    for i in range(len(N)):
        product = int(N[i]) * product  # Convert N[i] to integer
    if product == int(N):  # Compare the product with the number itself
        print("Right")
    else:
        print("Wrong")

# Sample Input
N = input("Enter a number: ")  # Take input from the user
check_prediction(N)