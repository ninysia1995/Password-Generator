import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

if __name__ == '__main__':
    length = int(input('Введите длину пароля: '))
    password = generate_password(length)
    print('Ваш пароль: ' + password)
