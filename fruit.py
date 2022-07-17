fruit = {
    'apple': '130',
    'avocado' : '50',
    'banana' : '110',
    'cantalope' : '50'
    }


def main():
    name = input('Item: ').lower()
    
    if name in fruit:
        print(f'Calories: {fruit[name]}')
    else:
        print('no data')
            


   
    
if __name__ == "__main__" : main()