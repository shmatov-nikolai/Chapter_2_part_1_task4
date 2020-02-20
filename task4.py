'''
Minimal positive integer:
//Find minimal positive integer that is not in list. If list contains only n
Example: [1,2,3,4,6] - Answer 5
Example: [1,2,3] - Answer 4
Example: [-1, -2, -6] - Answer 1
Create effective algorithm
'''

def min_positive_int(some_list):
   maximum = max(some_list)
   if maximum > 0:
       for i in range(1,maximum):
           if i not in some_list:
              return i
       else:
          return maximum+1
   else:
       return 1

string_num = input('введите ряд чисел через пробел: ').split()
list_num = []
for i in range(len(string_num)):
    list_num.append(int(string_num[i]))


itog = min_positive_int(list_num)

print(itog)
