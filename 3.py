 #Дан массив размера N. После каждого отрицательного 
 #элемента массива вставьте элемент с нулевым значением.
import random 
number_n= int(input('Введите размерность массива \n'))
rand_list=[]
for i in range(number_n):
    rand_list.append(random.randint(-100,100))
print(rand_list)
result=[]
for element in rand_list:
    result.append(element)
    if element < 0:
        result.append(0)
print(result)
    