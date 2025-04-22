import random
def generate_password(length, chars):
    password = ' '.join(random.choices(chars, k=length))
    return password
print(generate_password(8, "abcde"))