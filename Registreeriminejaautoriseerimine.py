from MyModule import* 
import random
user=["libol11","kolfi5471","gbjfh4"]
pasword=["GGFhjKI11","FFbhgr45","geYU47yh"]
print("****Registreerimine või autoriseerimine***")
while True:
	print("1-Registreerimine;2-Autoriseerimine;3-Logi välja")
	n=int(input())
	if n==1:
		print("Registreerimine")
		if n==1:
			login=input("Nimi:")
			if login not in user:
				print("Nimi sobib!")
			break
		else:
			print("Kasutajanimi on juba võetud!!!!")
		m=input("Automaatne parooli loomine(N);Sõltumatu(K)")
		if m.upper()=="N":
			pas=apass()
		if m.upper()=="K":
			pas=input("Sisestage oma parool -> ")
			kont=passkontroll(password)

			
	