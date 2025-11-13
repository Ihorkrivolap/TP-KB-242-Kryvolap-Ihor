import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
for elem in response.json():
  if (elem["cc"] == "EUR" or elem["cc"] == "USD" or elem["cc"] == "PLN"):
    print (elem)
    if elem["cc"] == "EUR": 
       eur_rate = elem["rate"]
    elif elem["cc"] == "USD": 
       usd_rate = elem["rate"]
    elif elem["cc"] == "PLN": 
       pln_rate = elem["rate"]

amount = int(input("Введіть Суму"))
valuta = input("Оберіть валюту (EUR, USD, PLN):")
if valuta == "EUR":
    suma = amount * eur_rate
    print(f"Сума у гривнях: {suma} ₴")
elif valuta == "USD" :
    suma = amount * usd_rate
    print(f"Сума у гривнях: {suma} ₴")
elif valuta == "PLN" :
    suma = amount * pln_rate
    print(f"Сума у гривнях: {suma} ₴")
else:
    print("Невірна валюта!")