import re

def is_username(username):
    # username = "Siska"
    pattern = re.compile("^[a-z]{5,9}$")
    m = pattern.match(username)
    
    if(m):
        print("true")
    else:
        print("false")

def is_password(password):
    # username = "passW0rd="
    pattern = re.compile("(?=^.{8,}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&amp;*()_+}{&quot;:;'?/&gt;.&lt;,])(?!.*\s).*$")
    m = pattern.match(username)
    
    if(m):
        print("true")
    else:
        print("false")

username = input("Masukkan username")
password = input("Masukkan password")

is_username(username)
is_password(password)