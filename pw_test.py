# 密碼重試程式
# 現在程式碼中 設定好密碼 password = 'a123456'
# 讓使用者[最多輸入3次密碼]
# 不對的話,就進出"密碼錯誤! 還有_次機會"
# 對的話,就印出"登入成功!"
y = 2
while True:
    pw = input('請出入密碼: ')
    if pw == 'a123456':
	    print('"登入成功!"')
	    break
    elif pw != 'a123456' and y > 0:
        print('"密碼錯誤! 還有', y ,'次機會')
    else:
        print('"密碼錯誤! 請重新啟動"')
        break
    y = y - 1
