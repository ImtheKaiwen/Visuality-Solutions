
def isArmstrong(number):
    b = [digit for digit in number]
    sum = 0
    n = len(b)
    for digit in b:
        iDigit = int(digit)
        sum += (iDigit ** n)

    if sum == int(number):
        print("Armstrong sayısıdır")
    else:
        print("değil")

while True:
    number = input("Enter your number :")
    isArmstrong(number)

