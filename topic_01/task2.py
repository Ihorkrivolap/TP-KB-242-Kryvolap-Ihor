import string
a = "abcdefg123! "
# strip() — забирає символи з початку і кінця рядка
# тут ми вказали: "a" + всі знаки пунктуації + пробіл
# тобто буде прибрано "a", "!" і пробіли з початку/кінця
print(a.strip("a" + string.punctuation + " "))
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
# lower() — всі символи переводяться у нижній регістр
k = "Hello World!"
h = k.lower()
print(h)   # hello world!
