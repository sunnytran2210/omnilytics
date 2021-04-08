import string
import re

def is_alphabetnumeric(obj):
    if obj.isalpha() == False and re.search("[a-zA-Z].*[0-9]",obj) != None and re.search("[.]",obj) == None:
        result = True
    else:
        result = False
    return result
def is_float(obj):
    if re.search("[.]",obj) != None:
        result = True
    else:
        result = False
    return result
def is_int(obj):
    if re.search("[a-p]",obj) == None and re.search("[.]",obj) == None:
        result = True
    else:
        result = False
    return result
def check_type(obj):
    if is_alphabetnumeric(obj) == True:
        obj_type = 'alphanumeric'
    elif is_float(obj) == True:
        obj_type = 'real numbers'
    elif is_int(obj) == True:
        obj_type = 'integer'
    elif obj.isalpha():
        obj_type = 'alphabetical strings'
    else:
        obj_type = 'unkown'
    return obj_type
    

with open('generator_file.txt') as txt:
    content = txt.read()

objects = content.split(',')

for obj in objects:
    obj = obj.strip()
    result = obj + ' - ' + check_type(obj)
    print(result)
    with open('final.txt','a') as final:
        final.write(result + '\n')



