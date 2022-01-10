import random
login=["Lina","Flora"]
password=["10203090","10509060"]
def auto_reg(pas:list):
    """Salasõna genireerimine
    Tagastab salasõna str formaadis
    :param str pas: salasõna genereerimine
    :rtype: str
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    print(str3)
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    pas = ''.join([random.choice(ls) for x in range(12)]) # Извлекаем из списка 12 произвольных значений
    p.append(pas)
    print("Teie parool:", pas)
    print("Registreeritud")
    return pas
def ise_reg (p:int):
    """parooli loomine ise
    :param int pass:uue parooli kasutuselevõtt
    :rtype:int
    """
    pass1=print ("Tule välja oma parool:")
    for i in range(len(pass1)):
        if pass1[i].isupper():
            upper=1
        if pass1[i].isalpha():
            alpha = 1
        if pass1[i].isdigit():
            digit = 1
        if pass1[i] in ls:
            speacial=1
        pass1=True
        return p
