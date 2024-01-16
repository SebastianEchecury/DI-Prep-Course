from utils import unzip_with_7z
import string

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!

# WRITE YOUR CODE BELOW
# ----------------------------------------

def listAlphabet():
    return list(string.ascii_lowercase)

letters = listAlphabet()

for x in letters:
    for y in letters:
        find_me = x + y
        secret_password = find_me + 'bcmpda' 
        found = unzip_with_7z(zip_file_path, dest_path, secret_password)
        if(found):
            print("Unearthed image")
            print("The password was: {}".format(secret_password))
            break
    if found : break
