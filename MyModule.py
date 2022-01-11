import random
login=["Lina","Flora"]
password=["10203090","10509060"]
def men():
    while True:
        print("1-Autoriseerimine,2-Registreerimine,3-Logi välja")
        a=int(input())
            if a==1:
                user=print("введи логин:")
                pasword=print("введи пароль:")
                v = v_aut(u,p)
            if v==True and v1==True:
                print("Успешный вход")
            else:
                print("Попробуйте ещё раз:")
                print()
                
def v_aut(u,p):
    if user in login:
        v=True  
    else:
        v=False
    if pasword in password:
        v1=True
    else:
        v1=False
                
def nimi(n:str,l:list):
    """otsib sisselogimist
    :param str n:otsib sisselogimist
    :rtype:str 
    """
    b=0
    for b in l:
        if b == l:
            print("sisselogimine on õige!!!!")
        else:
            print("Oooops.Proovige uuesti!!!!!!!!")
    return b
def auto_reg(psword:list):
    """Salasõna genireerimine
    Tagastab salasõna str formaadis
    :param str pas: salasõna genereerimine
    :rtype: str
    """
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
