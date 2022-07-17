#create a blank dictionary

def main():
    shop()
    
    
def shop():
    list = dict()
    while True: 
        try:
            food = input().upper()
            if food in list:
                list[food] += 1
            else:
                list[food] = 1
        except EOFError:
            break
   
    new_list = sorted(list)
   
    for i in new_list:
       print(f"{list[i]} {i}")


if __name__ == '__main__' : main()
    
    
    
    
