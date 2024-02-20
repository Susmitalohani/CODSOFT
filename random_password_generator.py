'''This program generates a random password of user desired length'''
from random import randint

def generate_pass(pass_len, mode):
    '''generates random password of required length'''
    
    if mode == 'easy':
        total_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        total_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[}{;:,<.>/?']"
    random_generation = ""
    char_len = len(total_characters) -1
    for _ in range(pass_len):
        char = total_characters[randint(0,char_len)]
        random_generation += char
    return random_generation

def main():
    while True:
        try:
            difficultly = input('Choose difficulty of password (Easy/Difficult) : ')
            if difficultly.lower() not in  ('easy','difficult'):
                raise ValueError('Please choose [easy] or [difficult]')
            length = int(input('Enter length of password to generate : '))
            if length>100 or length<1:
                raise ValueError('Please enter integers from 1-100')
            password = generate_pass(length, difficultly)
            print(f'Random generated password of length {length} : {password}')
            break
        except ValueError as error:
            print(error)
            print()
main()