def main():
    while True:
        try:
            num = input("Deep Thought number? ")
            if num == "42" or num == "forty two" or num == "forty-two":
                print(f'Yes, the answer is {num}')
                break
            else:
                print("wrong, try again")
        except ValueError: 
            continue
    
    
    
if __name__ == "__main__" : main()