
# початковий словник
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Початковий словник:", my_dict)

# update() - оновлює словник іншим словником 
my_dict.update({'d': 4, 'e': 5})
print("Після update({'d': 4, 'e': 5}):", my_dict)

# del - видаляє елемент за ключем
del my_dict['b']
print("Після del my_dict['b']:", my_dict)

# keys() - повертає перегляд ключів словника
print("Ключі:", list(my_dict.keys()))

# values() - повертає перегляд значень словника
print("Значення:", list(my_dict.values()))

# items() - повертає перегляд пар ключ-значення
print("Пари ключ-значення:", list(my_dict.items()))

# clear() - очищає словник, видаляючи всі елементи
my_dict.clear()
print("Після clear():", my_dict)