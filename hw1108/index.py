print('Homework 20161108 cycles')
number_list = [-4325.235, 13, 2134123.234, 1, 11, 44, 200]
max_number = min_number = number_list[0]
for i in number_list:
    current = i
    if current > max_number:
        max_number = current
    elif current < min_number:
        min_number = current
print("max = ", max_number)
print("min = ", min_number)
#####################################
for i in number_list:
    if i % 2 == 0:
        print(i, " - это четное")
    else:
        print(i, " - это нечетное")
#####################################
for multi in range(1, 10):
    for factor in range(1, 10):
        print(multi,' * ', factor, ' = ', multi*factor)
        if factor == 9 and multi != 9:
            print('-------------')
#####################################
step = '*'
for by_step in range(1,6):
    print(step*by_step)
#####################################
step = 1
for by_step in range(1,6):
    print(str(step)*by_step)
    step += 1
#####################################
composit_list = [-4325, 13, 'sdgf', 2134123.436, 1, 11, 44, "sdgsdfgsdfg", 200]
result_amount = 0
for current_item in composit_list:
 if isinstance(current_item, int) or isinstance(current_item, float):
     result_amount += current_item
print('Сумма всех чисел в строке = ',result_amount)
#####################################
print(composit_list)
for current_item in composit_list:
 if len(str(current_item)) > 5:
     print(current_item)
     composit_list.remove(current_item)
print(composit_list)
#####################################
result_string = ''
for curr_number in range(1,10):
    if curr_number%3 == 0:
        result_string += str(curr_number) + '\n'
    else:
        result_string += str(curr_number) + '   '
    curr_number += 1
print(result_string)
