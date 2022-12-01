# Напишите программу, которая принимает на вход число N 
# выдает набор произведений (набор - это список) чисел от 1 до N.
number_n= int(input("Введите число N \n"))
number=1
for i in range (1,number_n+1):
    number=i*number
    print(number, end=' ')
