import requests
import json

app_url="http://api.exchangeratesapi.io/v1/latest?****" #(***ALDIĞINIZ APİ ANAHTARI)
Bozdurulmak_istenilen=input("Bozdurulmak istenen döviz türünü giriniz:  ")
Alınan_döviz=input("Almak istediğiniz döviz türünü giriniz:  ")
Miktar=int(input(f"Ne kadar {Bozdurulmak_istenilen} bozdurmak istiyorsunuz: "))
result=requests.get(app_url+Bozdurulmak_istenilen)
result=json.loads(result.text)
print(result)
