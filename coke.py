

def main():
    n = int(input("How many bottles of Coke you want? "))
    price = n * 50
    print(f"Total is: {price}")
    pay(price)

def pay(coin):
    while coin > 0:
        pay = int(input("Insert Coin: "))
        coin = coin - pay
        if coin > 0:
            print(f"Amount due: {coin}")
        else:
            print(f"Changes: {coin}")
    
if __name__ == "__main__" : main()