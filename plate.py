number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    while True:
        s_len = len(s)
        if s_len == 2 and s[0:1] in number:
            return True
        elif 2 < s_len <=6:
            if s[0:1] in number or s[2] == 0 or s[s_len-1] not in number:
                return False
            else:
                return True
        else:
            return False
    
    
    
if __name__ == "__main__" : main()