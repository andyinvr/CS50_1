

def main():
    sen = input('file name: ')
    print(convert(sen))
    
    
def convert(sen):
    while True:
        sen_len = len(sen)
        snake = ""
        try:
            for i in range(0,sen_len,1):
                if sen[i].isupper():
                    snake = snake + "_" + sen[i].lower()
                else:
                    snake = snake + sen[i]
        except ValueError:
            break
          
        return snake
    
if __name__ == "__main__" : main()