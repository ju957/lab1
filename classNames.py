classCount = int(input("How many classes do you have? "))
classList = []

for x in range(classCount):
    classList.append(input("Enter your next class. "))

for x in classList:
    print(x)