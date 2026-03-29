import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_lenght = + int(input("şifrenin uzunluğunu girin"))

password = ""

for i in range(password_lenght):
    char = random.choice(chars)
    password += chars

print(password)

