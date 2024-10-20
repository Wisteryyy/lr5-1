a=str(input("Введите строку"))
dlina=len(a)
glasnii=0
soglasnii=0
for char in a:
    if char.lower() in "аеёиоуыэюя":
        glasnii +=1
    elif char.isalpha():
        soglasnii +=1

print("Длина строки:", dlina)
print("Количество гласных символов:", glasnii)
print("Количество согласных символов:", soglasnii)