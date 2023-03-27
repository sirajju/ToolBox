from cryptography.fernet import Fernet
import base64 as bs
import hashlib
import time
import os
import webbrowser
import urllib.request

def InstallUpdate():
    try:
        os.system('git clone https://github.com/sirajju/Cryptography')
        os.system('rm name.txt setup.bat version.txt Cryptography.py')
        return True
    except:
        return False
    
def isConnected():
    try:
        urllib.request.urlopen('https://github.com')
        return True
    except:
        return False
    
def CheckForUpdate():
    if isConnected():
        os.system('curl https://raw.githubusercontent.com/sirajju/Cryptography/main/version.txt>version.txt&&clear')
        with open('version.txt','r') as v:
            version = v.read()
            if version == '1.0\n':
                print('Congratulation, Your version is latest')
            else:
                print('\n\nGood News : An update available \n\nPlease update to latest version from git repo : https://github.com/sirajju/Cryptography')
                print('\nPreparing to update..\n')
                time.sleep(3)
                if InstallUpdate():
                    print('\n\nUpdated succesfully')
                else:
                    print('\n\nUpdation failed\nPlease update manually to get latest features')
    else:
        print('\nCheck for update failed :- No internet available!')
def end():
    os.system("whoami>name.txt")
    with open('name.txt','r') as f:
        name = f.read()
        print('\n<---------------The End--------------->')
        x=input('\nHey '+name+'\nWould you like to visit my repo ? Yes/No : ')
        if x=='Yes' or x=='yes' or x=='Y' or x=='y':
            print("\nYou will be redirected to author's page in 5 Seconds...")
            time.sleep(5)
            webbrowser.open('https://github.com/sirajju')
            print('\nThank you for your support !')
        else:
            print('\nOk Thanks!')
def encrypt():
    text = input('\nEnter text to encrypt : ')
    key = Fernet.generate_key()
    fernet = Fernet(key)
    print('\nOriginal text : '+text)
    print('\nKey used to encrypt : '+key.decode())
    enc_text = fernet.encrypt(text.encode())
    print('\nEncrypted text : '+enc_text.decode())
    end()

def decrypt(): 
    try:
        enc_key = input('\nEnter your key of the algorithm : ')
        enc_text = input('\nEnter your text to decrypt : ')
        fernet = Fernet(enc_key)
        dec_text = fernet.decrypt(enc_text).decode()
        print('\nDecrypted text is : '+dec_text)
        end()
    except:
        print('\n\nSomething went wrong!')
 
def b64encode():
    text = input('\nEnter your text to encode : ')
    encoded_text = text.encode()
    print('\nOriginal text : '+text)
    enc_text = bs.b64encode(encoded_text)
    print('\nBase64 encoded text is : '+enc_text.decode())
    end()


def b64decode():
    try:
        enc_text = input('\nEnter text to decode in base 64 : ')
        dec_text = bs.b64decode(enc_text)
        decoded_text = dec_text.decode()
        print('\nBase64 decoded text is : '+decoded_text)
        end()
    except:
        print('\nPlease enter base64 value !')

def hash(method):
    text = input('\nEnter the text to hash : ')
    enc_text = text.encode()
    if method == '1':
        hash_text = hashlib.md5(enc_text).hexdigest()
    elif method == '2':
        hash_text = hashlib.sha1(enc_text).hexdigest()
    else:
        print('\nInvalid input')
    print('\nHashed text is : '+hash_text)
    end()

def hashCompare(method):

    md5 = input('\nEnter hash : ')
    text = input('\nEnter the text to compare : ')
    text_enc = text.encode()
    if method == '1':
        comp_text = hashlib.md5(text_enc).hexdigest()
    elif method == '2':
        comp_text = hashlib.sha1(text_enc).hexdigest()
    else:
        print('\nSomething went wrong!')
    if (comp_text == md5):
        print('\nThe hash value has been succefully matched :) ')
    else:
        print('\nSorry you have entered the wrong hash value :( ')
    end()
CheckForUpdate()
print('\nDeveloper : @sirajju \n\nSelect an option from below \n\n1.Encrypt \n2.Decrypt \n3.Base64 Encode \n4.Base64 Decode \n5.Hash (md5,sha-1) \n6.Compare hash (md5,sha-1)')
choice = input('\nEnter your choice (1,2,3,4,5,6) : ')
if choice == '1':
    encrypt()
elif choice == '2':
    decrypt()
elif choice == '3':
    b64encode()
elif choice == '4':
    b64decode()
elif choice == '5':
    print('\nSelect hashing method from below \n\n1.Md5 \n2.SHA-1')
    method = input('\nEnter your choice (1,2) : ')
    if method == '1' or method == '2':
        hash(method)
    else:
        print('\nInvalid input')
elif choice == '6':
        print('\nSelect hashed method from below \n\n1.Md5 \n2.SHA-1')
        method = input('\nEnter your choice (1,2) : ')
        if method == '1' or method == '2':
            hashCompare(method)
        else:
            print('Invalid input')
else:
        print('Invalid input')
