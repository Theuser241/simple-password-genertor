import random
from random import shuffle
print("\n\nthe program will capitalize the first letter\n\n")
list1=["a","e","y","u","i","o"]
f_name=input('Enter your first name\n')
f_name=f_name[0].upper()
l_name=input('Enter your last name\n')
l_name=l_name[0].upper()
while len(l_name)>10:
    print('retype your last name')
    l_name = input('Enter your last name\n')
symbole=input("type any symbole you want to add\n")


date_of_birth=input('Enter your birth date DD/MM/YYYY\n')
while int(date_of_birth[0:1])>31:
    print('retype your birth date DD/MM/YYYY')
while int(date_of_birth[3:4])>12:
    print('retype your birth date DD/MM/YYYY')

dob_clean1 = date_of_birth.replace("/", "")
while not (len(date_of_birth)==10 and dob_clean1.isdecimal()==True and date_of_birth.find(".")==-1):
    print('retype youre date of birth')
    date_of_birth = input('Enter your birth date DD/MM/YYYY\n')
l_name=l_name+"."
l_name_list= list(l_name)


def password_generator(f_name,l_name,date_of_birth):
    password=""
    poss=l_name.find(".")
    random.shuffle(l_name_list)
    shuffled_name = ''.join(l_name_list)
    for i in range(len(f_name) - 1, -1, -1):
        if f_name[i] in list1:
            password=password + str(ord(f_name[i]))
        if f_name[i] not in list1:
            password=password+f_name[i]
    password=password+shuffled_name
    dob_clean = date_of_birth.replace("/", "")
    password = password + dob_clean
    password=str(password)
    password_list = list(password+symbole)
    random.shuffle(password_list)
    password = "".join(password_list)



    return password
password_generator(f_name,l_name,date_of_birth)
print("the password=>",password_generator(f_name,l_name,date_of_birth))


