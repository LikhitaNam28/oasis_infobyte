import string
import random
length=int(input("Enter the length of password you want"))
numb=int(input("Enter the total digits you want in the password:"))
symbol=int(input("Enter the total symbols you want in the password:"))
characters=int(input("Enter the total characters you want in the password:"))
char_List=list(string.ascii_letters)
symbol_list=list(string.punctuation)
number_list=list(string.digits)
password=""
for i in range(0,numb):
    a=random.choice(number_list)
    password=password+a
for i in range(0,symbol):
    a=random.choice(symbol_list)
    password=password+a
for i in range(0,characters):
    a=random.choice(char_List)
    password=password+a   
password=list(password)
random.shuffle(password)
password1=""
for i in password:
    password1=password1+i
print(password1)
