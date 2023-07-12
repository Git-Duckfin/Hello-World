try : 
    first = int(input('첫번째 숫자 입력 : '))
    second = int(input('두번째 숫자 입력 : '))
    print('{} / {} = {}'.format(first, second, first/second))
except : 
    print('Exception is raised.')
