import sys


def main():
    ext = extension()
    system(ext)
    
   
def extension(): 
    file = input("file name: ")
    if "." in file:
        extension = file.split(".")
        return(extension[-1])
    else:
        print("application/octet-stream")
        sys.exit()


def system(ext):
    if ext == "gif" or ext == "jpg" or ext == "jpge":
        print(f"media/{ext}")
    elif ext == "pdf" or ext == "txt":
        print(f"adobe/{ext}")
    else:
        print("no suitable app")

if __name__ == "__main__" : main()