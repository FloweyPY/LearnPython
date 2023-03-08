Number = []

while True:
    request = int(input('Выберите операцию'))
    if request == 1:
        answer = int(input('Введите новое число в список'))
        Number.append(answer)
    elif request == 2:
        Number.sort()
    elif request == 3:
        print(Number)
    else:
        print('Вы ввели неправильный номер операции, напишите заново')