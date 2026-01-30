import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/eur/"

response = requests.get(url)

data = response.json()
print(data)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
# 'rates': [{'no': '020/A/NBP/2026', 'effectiveDate': '2026-01-30', 'mid': 4.2131}]}

print(data['rates'])  # [{'no': '020/A/NBP/2026', 'effectiveDate': '2026-01-30', 'mid': 4.2131}]
print(data['rates'][0])  # {'no': '020/A/NBP/2026', 'effectiveDate': '2026-01-30', 'mid': 4.2131}
print(data['rates'][0]['mid'])  # 4.2131

# https://github.com/public-api-lists/public-api-lists
