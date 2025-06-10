def factoriel(number):
    if number == 1:
        return 1
    return number * factoriel(number-1)

while True:
    number = int(input("enter number : "))
    print(factoriel(number))
