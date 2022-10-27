import random
k=0
a=0
b=0
l=["!","@","#","$","%","&","*","(",")","{",":",";","}","[","]",",",".","<",">","?","/","1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","A","B","C","D","E",'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
chars=["!","@","#","$","%","&","*","(",")","{",":",";","}","[","]",",",".","<",">","?","/"]
s=input("Enter your password.")
if len(s)<=10:
    print("Password is too weak as it has ",len(s)," characters. The minimum requirement is 11 characters.")
    k=1
if  s.isalpha()==True:
    print("Password is too weak as it only contains alphabetic characters. ")
    k=1
if s.isdigit()==True:
    print("Password is too weak as it only contains numeric characters. ")
    k=1
for i in range(1,(len(s)+1)):
    if(s[a:i])in chars:
        b=2
        break
    else:
        a+=1
if b!=2:
    print("Your password must contain at least 1 special character. Examples are - !,?,%,& e.t.c")
    k=1
if s.isspace()==True:
    print("Password is too weak as it only contains space as characters. ")
    k=1
if s.islower()==True:
    print("Password is too weak as it only contains lower case characters. ")
    k=1
if s.isupper()==True:
    print("Password is too weak as it only contains upper case characters. ")
    k=1
if k==1:
    c=input("Do you want us to reccomend a strong password to you? Enter Y for yes and N for No")
    if c=="Y" or c=="y":
        for i in range(15):
            print(random.choice(l),end="")
    else:
        print("Please change your password. It is weak. Thank you for using our program.")
else:
    print("You have a strong password. Thank you for using our program.")
