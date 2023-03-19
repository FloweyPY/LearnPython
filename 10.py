for number in range(100, 10000):
    if len(str(number)) == 3:
        x = number % 10
        y = number % 100 // 10
        z = number // 100
        if x ** 3 + y ** 3 + z ** 3 == number:  
            print(number)
    if len(str(number)) == 4:
        x = number % 10
        y = number % 100 // 10
        z = number % 1000 // 100
        w = number // 1000
        if x ** 4 + y ** 4 + z ** 4 + w ** 4 == number:  
            print(number)