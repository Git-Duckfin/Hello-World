def myfunction(start, last):
    hap = 0
    for i in range(start, last+1) :
        hap = hap + i

    print(f'{start}부터 {last}까지 합은 {hap}입니다.')

#myfunction() # Call By Name
myfunction(10, 50)    # Call By Value

def modify(value):
    print('Before change {value}')
    value *= 1000
    print(f'After change value = {value}')

origin = 'Hello'
modify(origin)
print(f'origin = {origin}')