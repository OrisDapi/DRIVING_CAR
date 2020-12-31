driving = input('請問有開車嗎? ')
if driving != '有' and driving != '沒有' :
	raise SystemExit

age = input('請輸入年紀: ')
age = int(age)
if driving == '有' :
	if age < 18 :
		print('你的年紀怎麼可以開車!? ')
	else :
		print('你好車神! ')
elif  driving == '沒有' :
	if age >= 18 :
		print('你可以考照了 怎麼不去考? ')
	elif age < 18 :
		print('很好 再過幾年就可以考了 ')