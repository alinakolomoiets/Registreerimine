import random
def apass()->str:
	"""loo juhuslik parool
	:rtype:str
	"""
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper()
    # 'QWERTYUIOPASDFGHJKLZXCVBNM'
	str4 = str0+str1+str2+str3
	ls = list(str4)
	random.shuffle(ls)
	psword="".join([random.choice(ls) for x in range(12)])
	print("See on sinu password -> ",psword)
	return psword
def passw(password:str):
	"""oma parooli loomine
	:param str passsword:parool, mille kasutaja sisestas
	:rtype:str
	"""
	d=list(psword)
	for v in d :
		if(v.isdigit())==True:
			v=int(v)
		