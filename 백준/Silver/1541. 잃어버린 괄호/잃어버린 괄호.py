ex = input()

ex_list = ex.split('-')
result = 0

for i in range(len(ex_list)):
    oper_list = list(map(int, ex_list[i].split('+')))
    if i == 0:
        result += sum(oper_list)
    else:
        result -= sum(oper_list)
                         
print(result)
        