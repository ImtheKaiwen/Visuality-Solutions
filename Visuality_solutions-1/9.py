
def isArmstrong(number):
    b = [digit for digit in number]
    sum = 0
    n = len(b)
    for digit in b:
        iDigit = int(digit)
        sum += (iDigit ** n)

    if sum == int(number):
        print(f"{number} Armstrong sayısıdır")
    # else:
    #     print(f"{number} değil")

while True:
    a = int(input("Enter start :"))
    b = int(input("Enter end :"))
    for i in range(a,b+1,1):
        number = str(i)
        isArmstrong(number)
    

