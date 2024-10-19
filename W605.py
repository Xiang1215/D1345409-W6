#計算階層
n=int(input('請輸入一個正整數 :'))
a=1

if n>=0 :
    for i in range (n,1,-1):
        a*=i
    print(n,'! =',a)
else:
    print('請輸⼊⼀個有效的正整數。')