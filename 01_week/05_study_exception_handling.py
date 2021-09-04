try:
    arr = [1, 2]
    print(arr[3])
    4 / 0
except (IndexError, ZeroDivisionError) as e:
    print('Index or ZeroDivision Error 발생!', e)
