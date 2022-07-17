import re

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    print(convert())
    
def convert():
    while True:
        date = input("date: ")
        new_date = re.split('/|, | ', date)
        try:
            if new_date[0] in month:
                mm = month.index(new_date[0]) + 1
            elif int(new_date[0]) in range(1,13): 
                mm = int(new_date[0])

            if int(new_date[1]) in range(1,32) and int(new_date[2]):
                dd = int(new_date[1])
                yyyy = new_date[2]
            
            return (f"{yyyy}-{mm:02}-{dd:02}")
                
        except (UnboundLocalError, ValueError):
            continue
        

                
    
        #take number
        
        #check condition
        
        


if __name__ == '__main__' : main()
    