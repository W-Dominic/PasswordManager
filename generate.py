'''
Code for generating a random, secure password
'''
import random
import string

def gen(x):
#generates a password of length 24 with letters, numbers and special chars
    chars = [string.ascii_letters, string.digits, string.punctuation]
    final = ""
    for i in range(x):
        rand = random.choice(random.choice(chars))
        final += rand
    return final

if __name__ == "__main__":
    print(gen(10))
