import string
import random
alphabets = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

length = int(input("No of characters you want in your password"))
no_len = int(input("no of characters which are to be numeric in your password"))
sym_len = int(input("no of symbols you want in password"))

chars = random.choices(alphabets, k=length-no_len-sym_len)
nos= random.choices(numbers, k=no_len)
sym = random.choices(symbols, k=sym_len)
password = chars + nos + sym
print(password)
random.shuffle(password)
print(password)
password = ''.join(password)
print(password)