#密碼重試程式
#現在程式碼中設定好密碼 password ='a123456'
#讓使用者【最多輸入3次密碼】
#不對的話就印出"密碼錯誤! 還有__次機會"
#對的話，就印出"登入成功!"

password = 'a123456'
N = 2
while N >= 0:
	password2 = input('請輸入密碼: ')
	if password == password2:
		print('登入成功')
		break
	else:
		print('密碼錯誤! 還有', N,'次機會')
		N = N-1
