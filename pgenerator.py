import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="!#%&/()=?-,.><"

all_char=lower+upper+number+symbol
length=int(input("enter lenght of password: "))
password=''.join(random.sample(all_char, length))
print("your generated password is: ", password)