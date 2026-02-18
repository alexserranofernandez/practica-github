dinero=input()
lista=dinero.split()
euros=int(lista[0])
centimos=int(lista[1])
total=euros*100+centimos
billete_500=total//50000
resto_500=total%50000
billete_200=resto_500//20000
resto_200=resto_500%20000
billete_100=resto_200//10000
resto_100=resto_200%10000
billete_50=resto_100//5000
resto_50=resto_100%5000
billete_20=resto_50//2000
resto_20=resto_50%2000
billete_10=resto_20//1000
resto_10=resto_20%1000
billete_5=resto_10//500
resto_5=resto_10%500
moneda_2=resto_5//200
resto_2=resto_5%200
moneda_1=resto_2//100
resto_1=resto_2%100
moneda_50=resto_1//50
resto_50c=resto_1%50
moneda_20=resto_50c//20
resto_20c=resto_50c%20
moneda_10=resto_20c//10
resto_10c=resto_20c%10
moneda_5=resto_10c//5
resto_5c=resto_10c%5
moneda_2c=resto_5c//2
resto_2c=resto_5c%2
moneda_1c=resto_2c//1
resto_1c=resto_2c%1
print(f"Banknotes of 500 euros: {billete_500}")
print(f"Banknotes of 200 euros: {billete_200}")
print(f"Banknotes of 100 euros: {billete_100}")
print(f"Banknotes of 50 euros: {billete_50}")
print(f"Banknotes of 20 euros: {billete_20}")
print(f"Banknotes of 10 euros: {billete_10}")
print(f"Banknotes of 5 euros: {billete_5}")
print(f"Coins of 2 euros: {moneda_2}")
print(f"Coins of 1 euro: {moneda_1}")
print(f"Coins of 50 cents: {moneda_50}")
print(f"Coins of 20 cents: {moneda_20}")
print(f"Coins of 10 cents: {moneda_10}")
print(f"Coins of 5 cents: {moneda_5}")
print(f"Coins of 2 cents: {moneda_2c}")
print(f"Coins of 1 cent: {moneda_1c}")