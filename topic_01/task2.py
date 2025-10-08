import string
<<<<<<< HEAD
a = "abcdefg123! "
=======

# Строка з буквами, цифрами, символами і пробілом
a = "abcdefg123! "

>>>>>>> c5769db (add tasks for topic 02)
# strip() — забирає символи з початку і кінця рядка
# тут ми вказали: "a" + всі знаки пунктуації + пробіл
# тобто буде прибрано "a", "!" і пробіли з початку/кінця
print(a.strip("a" + string.punctuation + " "))
<<<<<<< HEAD
b = "hello world!"
# capitalize() — робить першу літеру великою, решту малими
c = b.capitalize()
print(c)   # Hello world!
# title() — кожне слово починається з великої літери
d = b.title()
print(d)   # Hello World!
# upper() — всі символи переводяться у верхній регістр
g = b.upper()
print(g)   # HELLO WORLD!
=======

# ====================

b = "hello world!"

# capitalize() — робить першу літеру великою, решту малими
c = b.capitalize()
print(c)   # Hello world!

# title() — кожне слово починається з великої літери
d = b.title()
print(d)   # Hello World!

# upper() — всі символи переводяться у верхній регістр
g = b.upper()
print(g)   # HELLO WORLD!

>>>>>>> c5769db (add tasks for topic 02)
# lower() — всі символи переводяться у нижній регістр
k = "Hello World!"
h = k.lower()
print(h)   # hello world!
