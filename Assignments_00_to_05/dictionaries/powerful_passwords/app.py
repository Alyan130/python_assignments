from hashlib import sha256

def login(email,password,stored_logins):
   if stored_logins[email]==hashpassword(password):
     return True
   else:
    return False


def hashpassword(password):
    return sha256(password.encode()).hexdigest()


def main():
    stored_logins = {
        "alyankhi@gmail.com": "c72ac752f65d259e3801ae9185101015db8c62198efef2d2cd74e13710a13463",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
    }
    
    email_input=input("Enter your email to login: ")
    password=input("Enter your password : ")
    
    print(login(email_input,password,stored_logins))



if __name__ == '__main__':
    main()



