Number = input('Введите любое число')
length = len(Number)
sum = 0

for x in range(length):
    sum += int(Number[x])
print(sum)