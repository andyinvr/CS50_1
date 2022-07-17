
from lib2to3.pytree import convert


def main():
    sentence = input("what is the sentence? ")
    convert(sentence)
    
    
def convert(words):
    
    emoji = words.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    print(emoji)


if __name__ == "__main__" : main()