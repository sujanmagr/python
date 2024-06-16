import random
number="1234567890"
length=4
OTP=''.join(random.sample(number, length))
print("your OTP is: ", OTP)
