driving = input ('請問你有沒有開過車:')
if driving != '有' and driving != '沒有' :
	print ('只能輸入有或沒有')
	raise SystemExit

age = input ('請問你的年齡:')
age = int (age)
if driving == ('有'):
    if age >= 18 :
        print ('你通過測驗了')
    else :
    	print ('你不應該開車')
elif driving == ('沒有'):
	if age >= 18 :
		print ('建議你可以去考駕照')
	else :
		print ('過幾年就可以去考駕照囉')