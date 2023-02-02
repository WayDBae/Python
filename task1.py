num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
action = str(input('Выберите действие:  Сложить(a), Вычесть(b), Разделить(c), Умножить(d)->'))
print("Результат: ", end="");
if action == "a":
    print(num1+num2)
elif action=="b":
    print(num1-num2)
elif action=="c":
    print(num1/num2)
else:
    print(num1*num2)



