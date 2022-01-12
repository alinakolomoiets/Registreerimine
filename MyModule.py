import random
login=["Lina","Flora"]
password=["10203090","10509060"]
v=""
def men():
    while True:
        print("1-Registreerimine")
        print("2-Autoriseerimine")
        print("3-Logi välja")
        a=int(input())
        if a==1:
            print("Hеобходимо создать логин и пароль")
            print()
            while 1:
                user=input("Введи логин:")
                if user not in login:
                    print("Вы использовали логин",user)
                    break
                else:
                    print("Логин уже используется:")
                    print()
            print("Как вы хотите создать логин:")
            print("1- Сгенирировать пароль автоматичечки")
            print("2-Cделать самому")
            o=int(input())
            if o==1:
                psword=auto_reg()
                password.append(psword)
            else:
                print()                      
            if o==2:
                print(" пароль должен содержать: знаки, большие символы а так же цифры.")
                pswr=input("Введите пароль:")
                h=ise_reg(password)
                if h==True:
                    login.append(user)
                    password.append(pswr)
                else:
                    print("Попробуй снова")
        if a==2:
            user=print("Введи логин:")
            v= v_aut(user)
        if v==True:
            print("Успешный вход")
        else:
            print("Попробуйте ещё раз:")
            pasword=print("Введи пароль:")
            v1=v_auto(pasword)
        if v1==True:
            print("Успешный вход")
        else:
            print("Попробуйте ещё раз:")
           
        if a==3:
            print("Досвидания!!")
            print()
            break
def auto_reg():
    import random
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)
    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    print(psword)

def ise_reg(password:str):
    s=list(password)
    for pas in s :
        if pas.isdigit():  
            q=True
        if pas.isupper():
            q=True 
        if pas.islower():
            q=True
        if pas in list ("!#¤%&/()=?$€"):
            q=True 
        else:
            pas=False
        return pas
def v_aut(user):
    if user in login:
        v=True  
    else:
        v=False
    return v
def  v_auto(pasword):
    if pasword in password:
        v1=True
    else:
        v1=False
    return v1
