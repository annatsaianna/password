password = 'a12345'
i = 3#剩餘機會
while True: 
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登錄成功')
		break
	else:
		i = i - 1
		print('密碼錯誤,您還有', i ,'次機會')
		if i == 0:
			break







