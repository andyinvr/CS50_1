vowel = ['a', 'i', 'e', 'o', 'u', 'A', 'I', 'E', 'O', 'U']


def main():
    twitter = input("What do you want to twitt? ") 
    print(short(twitter))
    
    
def short(sen):
    while True:
        sen_len = len(sen)
        twt = ""
        try:
            for i in range(0,sen_len):
                if sen[i] in vowel:
                    twt = twt + ""
                else:
                    twt = twt + sen[i]
        except ValueError:
            continue
        return twt

    
if __name__ == "__main__" : main()