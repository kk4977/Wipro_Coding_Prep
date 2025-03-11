# l = list(map(str,input().split(' ')))
# inputString = "null"
# inputLenght = -1
# for i in l:
#     if len(str(i)) > inputLenght:
#         inputLenght = len(str(i))
#         inputString = str(i)

# print (inputString)
# print (inputLenght)

def answer(stringx):
    inputString = "null"
    inputLenght = -1
    l = list(map(str, stringx.split(" ")))
    for i in l:
        if len(str(i)) > inputLenght:
            inputLenght = len(str(i))
            inputString = str(i)
    return inputString
stringx = input()
print(answer(stringx))
