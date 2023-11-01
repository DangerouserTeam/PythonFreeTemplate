import random

# Символы, из которых может состоять пароль пользователя
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Запрос у пользователя длины пароля
password_length = int(input("Password Lengthpyt: "))

# Переменная для хранения сгенерированного пароля
generated_password = ""

# Генерация пароля
for _ in range(password_length):
    random_char = random.choice(characters)
    generated_password += random_char

# Вывод сгенерированного пароля
print("Password:", generated_password)
