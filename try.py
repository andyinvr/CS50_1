
import re

date = input("date: ")
new_date = re.split('/|, | ', date)
print(new_date)
