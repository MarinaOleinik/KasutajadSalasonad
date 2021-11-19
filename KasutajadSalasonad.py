from Funktsioonid import *
users=["Marina"]
passwords=["12345"]

while True:
	print("Reg-1,Avt-2,Välja-3")
	v=int(input())
	if v==1:
		print("Registreerimine")
		while 1:
			log=input("Kasutajatunnus")
			if log not in users:
				print("Tunnus soobib")
				break
			else:
				print("See nimi juba on olemas listis")	
		v=input("Arvuti-A või ise-I loob parool")
		if v.upper()=="A":
			pas=passautomat()
		elif v.upper()=="I":			
			while 1:
				pas=input("Sisesta oma parool")
				tulemus=paskontroll(pas)
				if tulemus==True:
					users.append(log)
					passwords.append(pas)
					break

		
	elif v==2:
		print("Avtoriseerimine")
		#
	elif v==3:
		print("Välja")
		break
		#valmis
	else:
		print("On vaja valida 1,2 või 3")# kõik on olemas
