

def main():
    convert()
    
def convert():
    while True:
        n = input("Fraction: ")
        try:
            f0, f1 = n.split("/")
            new_f0 = int(f0)
            new_f1 = int(f1)
            frac = new_f0 / new_f1
            if 0 <= frac <=1:
                break
        except(ValueError, ZeroDivisionError):
            pass
    print(frac)
    
if __name__ == "__main__" : main()