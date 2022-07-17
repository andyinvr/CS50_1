menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
}

import sys


def main():
    bill()
    
def bill():
    bill = 0
    while True:
        food = input("Item: ").title()
        try:
            if food in menu:
                bill = bill + menu[food]
                print(f"Order: {bill:.2f}")
            elif food == "Done":
                print(f"Please pay in total: {bill:.2f}")
                sys.exit()
        except ValueError:
            pass


    
if __name__ == "__main__" : main()