country = input('你從哪個國家來 :')
age = input('你幾歲 :')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不能考駕照')