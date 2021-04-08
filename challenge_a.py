import random
import string
from pathlib import Path

def random_alphabet():
    size = random.randint(5,50)
    letters = ''
    for i in range(size):
        letters = letters + random.choice(string.ascii_letters)
    return letters

def random_int():
    return random.randint(1,1000)

def random_float():
    return random.uniform(1,1000)

def random_spaces():
    spaces = ''
    size = random.randint(1,10)
    for i in range(size):
        spaces = spaces + ' '
    return spaces
    
def random_alphabetnumeric():
    mix_len = random.randint(5,50)
    mix = random_spaces() #spaces before alphabetnumeric
    for i in range(5,50):
        mix = mix + random.choice(string.ascii_letters + string.digits)
    mix = mix + random_spaces()
    return mix

filename = open('generator_file.txt','w')

random_options = ['random_alphabet()','random_int()','random_float()','random_alphabetnumeric()']
random.choice(random_options)
obj_number = random.randint(100,1000)

objects = ''
i = 1
file_size = Path('generator_file.txt').stat().st_size/1024/1024

while i <= obj_number and file_size <= 10:
    random_option = random.choice(random_options)
    obj = eval(random_option)
    if objects == '':
        objects = str(obj)
    else:
        objects = objects + ',' + str(obj)
    with open('tmp_file.txt','w') as tmp:
        tmp.write(objects)
    file_size = Path('tmp_file.txt').stat().st_size/1024/1024
    if file_size <= 10:
        with open('generator_file.txt','w') as txt:
            txt.write(objects)
    i = i + 1
file_size = Path('generator_file.txt').stat().st_size/1024/1024    

if i > obj_number:
    print('There are {} objects to be saved in generator_file.txt with size = {}'.format(obj_number, file_size))
else:     
    print('There are {} objects to be saved in generator_file.txt with size = {}'.format(i, file_size))






