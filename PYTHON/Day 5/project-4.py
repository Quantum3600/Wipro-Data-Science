from sys import argv
num1 = argv[1].split('-')
num2 = argv[2].split('-')
numbers = argv[3].split('-')

happiness = 0
for num in numbers:
    if num in num1:
        happiness += 1
    elif num in num2:
        happiness -= 1

print(happiness)