number=6458
number_length = len(str(number))
i = 1
number_decomposed = ''
for x in str(number):
    w=f'{x}*{10**(number_length-i)}+'
    number_decomposed+=w
    i+=1
number_decomposed=number_decomposed[:-1]
print(f'number={number}')
print(f'number_decomposed={number_decomposed}')