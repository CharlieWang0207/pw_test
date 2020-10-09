# 密碼重試程式
# 現在程式碼中 設定好密碼 password = 'a123456'
# 讓使用者[最多輸入3次密碼]
# 不對的話,就進出"密碼錯誤! 還有_次機會"
# 對的話,就印出"登入成功!"
password = 'a123456'
y = 3 # 剩餘機會
while y > 0:
    pw = input('請出入密碼: ')
    if pw == password:
        print('登入成功!')
        break # 逃出迴圈
    else:
        y = y -1
        print('密碼錯誤! 還有', y, '次機會')