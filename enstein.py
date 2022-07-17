
import sys

c = 30

def main():
    kg = check()
    energy(kg)

def check():
    while True:
        kilo = input("kilo: ")
        try:
            if float(kilo):
                return float(kilo)
        except ValueError:
            print("value error")
            sys.exit()


def energy(kg):
    if kg >= 0:
        E = kg * c * c 
        print(E)
    else:
        print("negative number")
           
           
if __name__ == "__main__" : main()

