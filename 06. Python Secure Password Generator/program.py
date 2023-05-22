import string
import secrets

letters= string.ascii_letters
numbers= string.digits
symbols= string.punctuation

alphabeth= letters+numbers+symbols

def generate_password(leng=12):
    print("This password will be show, but no stored in the program. copy and clean the console for more security")
    password=""
    for i in range(leng):
        password+= secrets.choice(alphabeth)
    return password

while True:

    while True:
        passpromt=input("Select the password length or press ENTER")
        if passpromt=="":
            break
        else:
            try:
                passpromt=int(passpromt)
                break
            except:
                print("non valid length")
                continue
    if passpromt:
        print(generate_password(passprompt))
    else:
        print(generate_password())
    print("PASSWORD GENERATED PRESS ENTER TO MAKE MORE OR WRITE exit")
    response= input()
    if response=="exit":
        break