import requests
r = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL")
var =r.content
var2 = var.split()
print(var2[6])
