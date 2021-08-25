import random

# ============ Word List Gen ============
minimum = 24
maximum = 24
wmaximum = 1000

alphabet = 'abcdefghijklmnopqrstuvwxyz'
angka = '0123456789'
char = alphabet + angka

string = ''
FILE = open("wl.txt", "w")
for count in range(0, wmaximum):
    for x in random.sample(char, random.randint(minimum, maximum)):
        string += x
    FILE.write(string+'\n')
    string = ''
FILE.close()

print ('DONE!')
print(len('dbipvu07ma15hyojtwl8zxn9'))