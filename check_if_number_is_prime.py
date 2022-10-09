x = input("Enter a integer number: ")
dividend = []
myList = range(1, int(x) + 1)
print ("my list is => ", myList)
for y in myList:
    if (int(x) % y) == 0:
        dividend.append(y)
print("List of divisors of provided nubmer", x, " is =>  ", dividend)
