
def main():
    time = input("what time is it? ")
    meal(convert(time))


def convert(time):
    
    hour = int(time.split(":")[0])
    minute = time.split(":")[1]
    if "am" in minute or "pm" in minute:
        min = int(minute.split(" ")[0])
        m = minute.split(" ")[1]
        
        if m == "pm":
            if hour != 12:
                time = hour + min/60 + 12
            else:
                time = hour + min/60
        elif m == "am":
            if hour != 12:
                time = hour + min/60
            else:
                time = hour + min/60 - 12
    else:
        min = int(minute)
        time = hour + min/60
        
    return time

def meal(time):
    if 6<= time <10:
        print("you should have breakfast")
    elif 11 <= time <14:
        print("lunch time")
    elif 17 <= time < 21:
        print("dinner time")
    else:
        print("it's not time to eat. Reduce your weight!")
    

if __name__ == "__main__" : main()