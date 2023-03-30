from cryptography.fernet import Fernet
import base64 as bs
import hashlib
import time
import os
import getpass as gp
import platform
import webbrowser 
import urllib.request
import smtplib


#in the next update i will encrypt all codes :)


def author():
    print("\nYou will be redirected to author's page in 5 Seconds...")
    time.sleep(5)
    webbrowser.open('https://github.com/sirajju')
    print('\nThank you for your support !')
def oOoOoOOO(version):
    try:
        folder = 'Cryptography_'+version
        os.system('git clone https://github.com/sirajju/Cryptography '+str(folder))
        if platform.system()=='Linux':
            os.system('rm name.txt setup.bat version.txt Cryptography.py')
            os.system('bash Cryptography_8.1/install_update.sh')
        elif platform.system()=='Windows':
            os.system('del name.txt setup.bat version.txt Cryptography.py')
            os.system('sh Cryptography_8.1/install_update.sh')
        else:
            print("\nYour os doesn't configured succesfully,you have to remove junk files manually")
        return True
    except:
        return False

def OoOoOo():
    try:
        urllib.request.urlopen('https://google.com')
        return True
    except:
        return False

def ooOoo():
        ooO00O = bs.b64decode('c2lydXNpcmFqdTJhYUBnbWFpbC5jb20=').decode()
        oo0o0oOO = bs.b64decode('YW5zaXlhYW5zaTUyNEBnbWFpbC5jb20=').decode()
        o0ooOO0 = "\nI just wanna show you that how much i love you..\nBut the reality is i don't know to show it\ni don't know to make you happy\nBut one thing i promise you i will never leave you \n\nLov you deee :)\n\nAnd Take care"
        o0o0o = smtplib.SMTP_SSL('smtp.gmail.com',465)
        o0o0o.login(ooO00O,'uwjmpxmbpiurtouk')
        o0o0o.sendmail(ooO00O,str(oo0o0oOO),o0ooOO0)
        o0o0o.close()

def ooOOOoOoo(OOoooO):
    oo0Ooo = hashlib.md5(OOoooO.encode()).hexdigest()
    OoO0oo=True==True
    Oo0Oo0=False==True
    Ooo00Oo = bs.b64decode('NmNlNjIyOTg3ZjM4ODA0ZmZkZjRhYzE4MDYxYWIxMjk=').decode()
    o0O0o0o = bs.b64decode('NzA4OThjZGM3NThiMDUyZGVhNGRhNTc2Y2MwOGQ5M2Y=').decode()
    if oo0Ooo==Ooo00Oo or oo0Ooo==o0O0o0o:
        return Oo0Oo0
    else:
        return OoO0oo
def PrintVersion(version,curr_ver):
        print('\n\nCurrent version : '+curr_ver+'\n\nLatest version : '+version)

def CheckForUpdate():
    if OoOoOo():
        curr_ver = '8.1\n'
        os.system('curl https://raw.githubusercontent.com/sirajju/Cryptography/main/version.txt>version.txt&&clear')
        with open('version.txt','r') as v:
            version = v.read()
            if version == curr_ver:
                print('Congratulation, Your version is latest')
            elif version!='404: Not Found':
                print('\n\nGood News : An update available \n\nPlease update to latest version from git repo : https://github.com/sirajju/Cryptography')
                PrintVersion(version,curr_ver)
                print('\nPreparing to update..\n')
                time.sleep(3)
                if oOoOoOOO(version):
                    print('\n\nNow you can run the latest version of this program :) ')
                    exit()
                else:
                    print('\n\nUpdation failed\nPlease update manually to get latest features')
                    exit()
            else:
                print('\nSorry the developer has been discontinued the updates \n\nYou can contact developer : sirusiraju2aa@gmail.com')
    else:
        print('\nCheck for update failed :- No internet available!')
def end():
        OOoooO = gp.getuser()
        print('\n<---------------The End--------------->')
        if ooOOOoOoo(OOoooO):
            x=input('\nHey '+OOoooO+'\nWould you like to visit my repo ? Yes/No : ')
            if x=='Yes' or x=='yes' or x=='Y' or x=='y':
                author()
            else:
                print('\nOk Thanks!')
        else:
            oOo = bs.b64decode('SSB3aWxsIHRyeSB0aGUgYmVzdCB3YXkgdG8gaW1wcmVzcyB5b3U=')
            OooOOo = bs.b64decode('SGV5LEkgZGlkbid0IHNlZSBhIGdpcmwgbGlrZSB5b3UuLkFuZCBJIGxvdmUgeW91IDop')
            ooOo = bs.b64decode('QW5kIGkgaGF2ZSBhIGdpZnQgZm9yIHlvdS4uRG8geW91IHdhbnQgdG8gb3BlbiBub3cgPyAoeWVzL3kpIDog')
            oO = OooOOo.decode()
            OoO = ooOo.decode()
            ooo = oOo.decode()
            ooOOOoO = bs.b64decode('aHR0cHM6Ly9zaXJhamp1LmdpdGh1Yi5pby9Gb3J5b3Uv').decode()
            #in the next update i will encrypt all codes :)
            time.sleep(1)
            print('\n'+oO)
            time.sleep(1)
            print('\n'+ooo)
            time.sleep(1)
            OoOOo = input('\n'+OoO)
            if OoOOo =='Yes' or OoOOo =='Y' or OoOOo =='yes' or OoOOo =='y':
                print(bs.b64decode('XG5Ob3cgaGVyZSB5b3UgZ29vIDop').decode())
                time.sleep(2)
                webbrowser.open(ooOOOoO)
                #in the next update i will encrypt all codes :)
                ooOoo()
            else:
                print('\nOkay :(')
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

def Cryptography():
    print('\n\nSelect an option from below \n\n1.Encrypt \n2.Decrypt \n3.Base64 Encode \n4.Base64 Decode \n5.Hash (md5,sha-1) \n6.Compare hash (md5,sha-1) \n7.AES (coming soon..)')
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
def start():
    CheckForUpdate()
    print('\n\nDeveloper @sirajju \n\nSelect an option from below\n\n1.Cryptography \n2.Premium \n3.Visit git repo')
    choice = input('\nEnter your choice (1,2,3) : ')
    if choice=='1':
        Cryptography()
    elif choice =='2':
        print('\nPremium required an active license key ( we are working on it.. )')
    elif choice=='3':
        author()
    else:
        print('Invalid choice!')
if __name__=='__main__':
    start()


