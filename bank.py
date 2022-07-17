

def main():
    greet = input("Greeting: ")
    if greet == "Hello" or greet == "hello":
        print("$0")
    elif greet[0] == "h" or greet[0] == "H":
        print("$20")
    else:
        print("$100")
    

    
if __name__ == "__main__" : main()