import random
#Cоздаем функции
def passautomat()->str:
	"""Пароль создается машиной
	"""	
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper() # 'QWERTYUIOPASDFGHJKLZXCVBNM'
	str4 = str0+str1+str2+str3
	ls = list(str4) # список [".",",",":"...]
	random.shuffle(ls) #перемешаем
# Извлекаем из списка 12 произвольных значений
	psword = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
	return psword