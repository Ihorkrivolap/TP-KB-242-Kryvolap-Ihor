
# початковий список
my_list = [1, 3, 2]
print("Початковий список:", my_list)

# append() - додає елемент в кінець списку
my_list.append(5)
print("Після append(4):", my_list)

# insert(index, val) - вставляє елемент на вказану позицію
my_list.insert(2, 5)  # Вставляємо 5 на позицію 1
print("Після insert(1, 5):", my_list)

# extend() - розширює список іншим списком
my_list.extend([6, 7])
print("Після extend([6, 7]):", my_list)

# remove(val) - видаляє перше входження значення
my_list.remove(3)
print("Після remove(3):", my_list)

# sort() - сортує список за зростанням
my_list.sort()
print("Після sort():", my_list)

# reverse() - перевертає список
my_list.reverse()
print("Після reverse():", my_list)

# copy() - створює копію списку
copied_list = my_list.copy()
print("Копія списку:", copied_list)

# clear() - очищає список
my_list.clear()
print("Після clear():", my_list)

# Перевіряємо, що копія не змінилася
print("Копія після clear оригіналу:", copied_list)