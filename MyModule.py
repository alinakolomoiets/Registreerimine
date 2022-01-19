import random
login=[]
password=[]
def failist_lugemine(f:str,l:list):
	"""Info failist f listisse l
	"""
	fail=open(f,'r')#,encoding="utf-8-sig"
	for rida in fail:
		l.append(rida.strip())#'\n'
	fail.close()
	return l

def failist_lugemine(f:str,l:list):
	"""Info pasword
	"""	
	fail=open(f,'r')
	for rid in fail:
		l.append(rid.strip())
	fail.close()
	return l

def failisse_salvestamine(f:str,l:list):
	"""Loetelu salvaestame failisse
	"""	
	fail=open(f,'w')#перезапись
	for el in l:
		fail.write(el+'\n')
	fail.close()

def rida_salvestamine(f:str,rida:str):
	"""Üks sõna või lause (rida) salvestame failisse
    :param str f:fail kuku salvastame
    :param str rida :sõna , mis vaja salvestada failisse
    """
	fail=open(f,'a')#до записываем остается то что было и добавляется новое 
	fail.write(rida+'\n')
	fail.close()
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
            print("Как вы хотите создать пароль:")
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
                while:
                    if h==True:
                    login.append(user)
                    password.append(pswr)
                else:
                    print()
                    print("Попробуй снова:")
                    print()
                        
                       
        if a==2:
            user=print("Введи логин:")
            pswr=print("Введи пароль:")
                #print("Успешный вход")
                #print("Попробуйте ещё раз:")
                #print()
           
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
    q=False
    for pas in s :
        if pas.isdigit(): # Состоит ли строка из цифр 
            q=True
        if pas.isalpha(): # Состоит ли строка из букв
            q=True
        if pas.isupper(): # Состоит ли строка из символов в верхнем регистре
            q=True 
        if pas.islower(): # Состоит ли строка из символов в нижнем регистре
            q=True
        if pas in list (">","!","#","¤","%","&","/","(",")","=","?","$","€"): #Состоит ли строка из символов
            q=True 
    return q
