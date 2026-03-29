import random

def gen_pass(password_lenght)

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

for i in range(password_lenght):
    char = random.choice(chars)
    password += chars

print(password)



