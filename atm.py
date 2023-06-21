import random

print("welcome to the Bank")
print('''
1.new user  => enter "1"
2.existing user => enter "2"
''')
prename='vasukalyan'
prepass='vasukalyan'
main = int(input('enter the option'))
if main ==1:
    print("create login")
    name = input("enter your username ")
    pasw = input("create your password ")
    print('your login was created ')
    print("you want to use your login press 'y' you want close enter 'n'")
    opt = input('enter your option : ')
    if opt=='y':
        NAME=input("enter the username : ")
        password=input('enter your password :')
        if NAME ==name and password ==pasw:
            print("welcome")
            print('''
            1.balance enquary
            2.money withdrow
            3.money diposit 
            4.mini statment
            ''')
            balence = 10000
            check = int(input("enter your opton "))
            if check ==1:
                print(f'your balence is =  {balence}')
            elif check==2:
                withdr=int(input('enter the emount :'))
                otp = random.randint(1111,9999)
                print('plese verify with this otp ', otp)
                otpck=int(input('enter the otp :'))
                if otp==otpck:
                    if withdr <=balence:
                        balence-=withdr
                        print('monney withdrow is successfull')
                        bal=input('you want to show the remaining balance enter (y/n)  :')
                        if bal=='y':
                            print('your money withdrow is successfully your current balence is Rs:',balence)
                    else:
                        print("in sufficient balence")
                else:
                    print('invalied otp')
            elif check==3:
                dipos = int(input('enter the money :'))
                balence+=dipos
                print(
                f'''diposite is successfull
                your current balence is {balence}''')
            elif check ==4:
               print(
               f'''=======================
               name is {NAME} 
               your current balence is : {balence}
               =================================
               ''')
        else:
            print('you entered wrong username and password')
            print('plese try again ')
    else:
        print('you entered wrong input')


if main==2:
    NAME = input("enter the username : ")
    password = input('enter your password :')
    if NAME == prename and password == prepass:
        print("welcome")
        print('''
            1.balenc enquary
            2.money withdrow
            3.money diposit 
            4.mini statment
            ''')
        balence = 10000
        check = int(input("enter your opton "))
        if check == 1:
            print(f'your balence is =  {balence}')
        elif check == 2:
            withdr = int(input('enter the emount :'))
            otp = random.randint(1111, 9999)
            print('plese verify with this otp ', otp)
            otpck = int(input('enter the otp :'))
            if otp == otpck:
                if withdr <= balence:
                    balence -= withdr
                    print('monney withdrow is successfull')
                    bal = input('you want to show the remaining balance enter (y/n)  :')
                    if bal == 'y':
                        print('your money withdrow is succesfully your current balence is Rs:', balence)
                else:
                    print("in sufficient balence")
            else:
                print('invalied otp')
        elif check == 3:
            dipos = int(input('enter the money :'))
            balence += dipos
            print(
f'''diposite is complated 
your current balence is {balence}''')
        elif check == 4:
            print(
f'''=======================
name is {NAME} 
your current balence is : {balence}
=================================
''')
    else:
        print('you entered wrong username and password')
        print('plese try again ')
else:
    print('you entered wrong input')