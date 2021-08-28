name=input("enter the name")
if name=="anjali singh":
    print("it is your account")
    email_id=input("enter the email id")
    if email_id=="anjalisingh@gmail.com":
        print("email id is correct")
        mobile_number=input("enter the mobile number")
        if mobile_number=="1234567890":
            print("it is your mobile number")
            password=input("enter the password")
            if password=="123456":
                print("your login in sucessfull")
            else:
                print("wrong password give strong password")
        else:
            print("wrong number")
    else:
        print("it is not your email")
else:
    print("it is not your account")
                                
    

