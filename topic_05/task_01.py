import random
user_choise = input("Введіть один з варіантів: камінь, ножиці або папір.")
с_choise = random.choice(["камінь", "ножиці", "папір"])
print(f"Комп’ютер обрав: {с_choise}")
if user_choise == с_choise:
    print("Нічия")
elif (
    (user_choise == "камінь" and с_choise == "ножиці") or
    (user_choise == "ножиці" and с_choise == "папір") or
    (user_choise == "папір" and с_choise == "камінь")
):
    print("Ви перемогли")
else: 
    print("Ви програли")